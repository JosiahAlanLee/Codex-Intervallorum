# Validation of the first divergent edition

- The build produced 46 PDF pages and 12 new SVG plates, with no text-flow
  overflow reported by the typesetting engine.
- All 46 pages were inspected in rendered contact sheets. Diagram pages were
  re-rendered after converting PDF lettering to real embedded text; selected
  diagrams were inspected at larger size.
- PDF text lies within page bounds. Internal link destinations resolve. The
  PDF includes a linked index, source links, and an outline.
- Every standalone SVG's glyph reference resolves to a definition inside the
  same file. No online font or image request is needed.
- A fresh build run from another working directory reproduced all 16 build
  products byte for byte with the same dependency versions.
- Nine source/model tests and five inherited plotter tests pass.
- `git diff --check` passes.

The scheduling model has not been empirically validated as an institutional
audit method. No new field or historical trial is reported. The new plates
have not been converted or tested for physical plotting. Original XI retains
its earlier digital-only test status.

The dependency lock records the successful Python 3.12 environment. Other
Python versions and operating systems have not been exercised here.
