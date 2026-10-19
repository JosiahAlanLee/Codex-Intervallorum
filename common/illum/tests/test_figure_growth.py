"""Guard the reading-order, protected-pixel and carrier boundaries."""
import copy
import hashlib
import io
from pathlib import Path
import sys
import tempfile
import unittest

import numpy as np
from PIL import Image, ImageDraw
from reportlab.pdfgen.canvas import Canvas

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import figure_growth as fg
import platekit as pk


class FigureGrowthTests(unittest.TestCase):
    def fixture(self):
        im=Image.new("RGB",(80,120),"white");d=ImageDraw.Draw(im)
        d.rectangle((20,10,60,110),fill=(70,70,65))
        d.ellipse((34,44,46,56),fill=(163,43,36))
        return np.asarray(im),dict(source="test-figure-raster-reference-v01.png",
            source_sha256=hashlib.sha256(im.tobytes()).hexdigest(),figure_bbox_px=[20,10,60,110])

    def test_monotone_mask_and_clear_protected_cores(self):
        rgb,meta=self.fixture();field=fg.simulate(1-rgb.mean(2)/255,17)
        previous=np.zeros(rgb.shape[:2])
        for amount in [0,.2,.4,.6,.86]:
            mask,core=fg.masks(rgb,meta,field,amount)
            self.assertTrue(np.all(mask>=previous))
            self.assertTrue(np.all(mask[core]==0))
            previous=mask
        self.assertGreater(previous.sum(),30)
        self.assertTrue(np.array_equal(field,fg.simulate(1-rgb.mean(2)/255,17)))

    def test_zero_is_exact_and_appearance_keeps_red_pixels(self):
        rgb,meta=self.fixture()
        with tempfile.TemporaryDirectory() as td:
            path=Path(td)/"source.png";Image.fromarray(rgb).save(path)
            c=Canvas(io.BytesIO());fg.configure(c,"III",0,3)
            result,info=fg.appearance(c,str(path),meta)
            self.assertEqual(result,str(path));self.assertTrue(info['unchanged'])
            self.assertEqual(c._figure_growth['index'],1)
            fg.configure(c,"IV",10,12)
            original_cache=fg.CACHE;fg.CACHE=Path(td)/"cache"
            try:
                result,info=fg.appearance(c,str(path),meta)
                output=np.asarray(Image.open(result))
                _,core=fg.protection(rgb,fg.subject(meta),meta['figure_bbox_px'])
                self.assertTrue(np.array_equal(output[core],rgb[core]))
                self.assertTrue(info['protected_pixels_equal'])
            finally:fg.CACHE=original_cache

    def test_material_tag_never_applies_to_text_or_carriers(self):
        for layer,attrs,expected in [('art',' data-material="cornmeal"',True),
            ('text',' data-material="cornmeal"',False),
            ('art',' data-material="cornmeal" data-cell="1"',False),
            ('art',' data-blade="1"',False)]:
            doc=pk.plotkit.PlotDoc(20,20)
            doc.layers[layer].append((pk.INK_HEX,.12,'M2,2 L12,12',attrs))
            before=copy.deepcopy(doc.layers)
            c=Canvas(io.BytesIO());fg.configure(c,"IV",5,12)
            pk.draw_doc(c,doc,pk.Map((0,0,20,20),(0,0,100,100)))
            self.assertEqual(bool(getattr(c,'_cornmeal_grains',0)),expected)
            self.assertEqual(doc.layers,before)


if __name__=='__main__':unittest.main()
