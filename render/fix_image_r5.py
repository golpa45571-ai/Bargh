"""Round 5: kill the two visible matte boxes with REAL background texture.

Cause: rounds 1-4 rebuilt brightness correctly but with synthetic smooth
gradients — uniform rectangles inside a photographic texture read as "matte".

Fix: texture transplantation.
  1. Take a clean real-bg donor tile next to each wound (x1352-1400 for the
     meters zone, x1230-1242 for the breaker zone).
  2. resid = donor - box_blur(donor)  (dark pixels inpainted first).
  3. Mirror-tile resid across the wound on top of the verified base field.
Result stats match real bg: std ~10.6 vs ~11, adj-diff ~3.6 vs ~3.1,
local contrast within real-bg range, zero flat clusters.

Also removed the orphaned wire remnants of the deleted 4th 125A breaker
(band y605-645, rebuilt with same technique; CT4/CT5 top terminals kept —
verified identical to CT2/CT3/CT6 terminals).
"""
