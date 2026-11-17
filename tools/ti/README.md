# TI-84 Plus CE programs

Source for the calculator programs in `/downloads`.

- `p1.py` builds P1MOTION (Unit 1), `p2.py` builds P2FORCE (Unit 2), `build_ti.py` builds PHYSNOTE (Unit 3; run `add_work.py` first).
- `tilib.py` has the shared pieces: guided solvers, the work-and-answer screen, notes slides, and build checks (labels, menus, line lengths, token audit).
- `tisim.py` is a small TI-BASIC interpreter used by `test_p1.py` and `test_p2.py` to run every solver with known answers.

Requires `pip install tivars`.
