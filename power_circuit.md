# Power-circuit drawing inventory

This is a drawing-faithful transcription of `totall.pdf` and its six detail sheets.  Text in code formatting preserves the identifier, label, rating, terminal marking, or wire-size notation printed on the drawings.  A component is not given a function beyond the text printed beside its symbol, and a connection is listed only where a line is drawn to it.

## Source drawings

| Drawing | Content transcribed in this document |
|---|---|
| `totall.pdf` | One-sheet composite/master drawing. It contains the regions enlarged in `001.pdf` through `006.pdf`. |
| `001.pdf` | Q0, CT1–CT6, DATA LOGGER, KWH1, and `F.KWH1&SIG`. |
| `002.pdf` | Lighting wiring, `F.CONTROL`, `F.SOCKET`, `F.LIGHTING`, S0/S1/S2, KWH1 auxiliary contact, and Q0 control wiring. |
| `003.pdf` | Q1, Q2, and Q3. |
| `004.pdf` | Q5, CT7–CT9, KWH2, `F.CONTROL`, and the 16 A MCB. |
| `005.pdf` | TIMER/temperature-controller graphic, KWH2 auxiliary contact, S1 contact, relay R2, and Q5 control wiring. |
| `006.pdf` | Three untagged 125 A, single-phase MCCBs. |

## Complete component inventory

The counts below are counts of separately drawn instances.  Repeated appearances of a component's control/auxiliary contact are retained in the sheet-level connection tables rather than counted as an invented additional device.

| Reference or printed name | Drawn quantity | Literal label/specification beside the symbol | Drawing(s) |
|---|---:|---|---|
| Q0 | 1 | `MCCB WITH MOTOR`; `3 PHASE 250A`; motor symbol `M` | `001.pdf`, `totall.pdf` |
| CT1 | 1 | `400/5A`; `SVA`; terminals `P1`, `P2` | `001.pdf`, `totall.pdf` |
| CT2 | 1 | `400/5A`; `SVA`; terminals `P1`, `P2` | `001.pdf`, `totall.pdf` |
| CT3 | 1 | `400/5A`; `SVA`; terminals `P1`, `P2` | `001.pdf`, `totall.pdf` |
| CT4 | 1 | `400/5A`; `SVA`; terminals `P1`, `P2` | `001.pdf`, `totall.pdf` |
| CT5 | 1 | `400/5A`; `SVA`; terminals `P1`, `P2` | `001.pdf`, `totall.pdf` |
| CT6 | 1 | `400/5A`; `SVA`; terminals `P1`, `P2` | `001.pdf`, `totall.pdf` |
| DATA LOGGER | 1 | `DATA LOGGER` | `001.pdf`, `totall.pdf` |
| KWH1 | 1 | `KWH1` | `001.pdf`, `totall.pdf` |
| F.KWH1&SIG | 1 | `F.KWH1&SIG`; `6A 3PHASE`; `Type:C` | `001.pdf`, `totall.pdf` |
| Lighting | 1 | `Lighting` | `002.pdf`, `totall.pdf` |
| F.CONTROL | 1 | `F.CONTROL` | `002.pdf`, `totall.pdf` |
| F.SOCKET | 1 | `F.SOCKET` | `002.pdf`, `totall.pdf` |
| F.LIGHTING | 1 | `F.LIGHTING` | `002.pdf`, `totall.pdf` |
| S0 | 1 | `S0` | `002.pdf`, `totall.pdf` |
| S1 | 1 tag shown in the lighting/control wiring | `S1`; a separate contact depiction is marked `23`, `24` | `002.pdf`, `005.pdf`, `totall.pdf` |
| S2 | 1 | `S2`; markings `2`, `3` | `002.pdf`, `totall.pdf` |
| Q1 | 1 | `MCCB`; `3PHASE`; `100A` | `003.pdf`, `totall.pdf` |
| Q2 | 1 | `MCCB`; `3PHASE`; `100A` | `003.pdf`, `totall.pdf` |
| Q3 | 1 | `MCCB`; `3PHASE`; `100A` | `003.pdf`, `totall.pdf` |
| Q5 | 1 | `MCCB WITH MOTOR`; `3PHASE 100A`; motor symbol `M` | `004.pdf`, `totall.pdf` |
| CT7 | 1 | `400/5A`; `SVA`; terminals `P1`, `P2` | `004.pdf`, `totall.pdf` |
| CT8 | 1 | `400/5A`; `SVA`; terminals `P1`, `P2` | `004.pdf`, `totall.pdf` |
| CT9 | 1 | `400/5A`; `SVA`; terminals `P1`, `P2` | `004.pdf`, `totall.pdf` |
| KWH2 | 1 | `KWH2` | `004.pdf`, `totall.pdf` |
| F.CONTROL | 1 additional drawn instance | `F.CONTROL`; `6A/32A`; `1PHASE` | `004.pdf`, `totall.pdf` |
| MCB | 1 | `MCB`; `3PHASE 16A`; `Type:C` | `004.pdf`, `totall.pdf` |
| TIMER / controller graphic | 1 | `TIMER`; `TEMPERATURE CONTROLLER`; `TRB-900`; `180-250 VAC`; `MAX 5A` | `005.pdf`, `totall.pdf` |
| KWH1 auxiliary contact | 1 contact depiction | `KWH1`; terminals `13`, `14`; connection marks `X.KWH1 11`, `X.KWH1 12` | `002.pdf`, `totall.pdf` |
| KWH2 auxiliary contact | 1 contact depiction | `KWH2`; terminals `13`, `14`; connection marks `X.KWH2 11`, `X.KWH2 12` | `005.pdf`, `totall.pdf` |
| R2 | 1 relay depiction | `RELAY`; `R2`; coil terminals `A1`, `A2`; contact terminals `13`, `14` | `005.pdf`, `totall.pdf` |
| 125 A MCCB, first | 1 | `MCCB`; `1PHASE 125A` | `006.pdf`, `totall.pdf` |
| 125 A MCCB, second | 1 | `MCCB`; `1PHASE 125A` | `006.pdf`, `totall.pdf` |
| 125 A MCCB, third | 1 | `MCCB`; `1PHASE 125A` | `006.pdf`, `totall.pdf` |

## `001.pdf` — Q0, CT1–CT6, DATA LOGGER, KWH1

### Incoming conductors and Q0

| Item as drawn | Printed marking |
|---|---|
| Five incoming conductors | `L1`, `L2`, `L3`, `N`, `PE`; each is marked `25*5Mm² CU` |
| Q0 | `MCCB WITH MOTOR`, `3 PHASE 250A`, and symbol `M` |
| Three Q0 outgoing phase conductors | Each is marked `25*5Mm² CU` |

### Current-transformer paths

Every CT in this sheet is printed with `400/5A`, `SVA`, `P1`, and `P2`.  The following wire numbers, sizes, and meter/logger terminal legends are drawn:

| CT | P1 path | P2 path | Destination terminal legends |
|---|---|---|---|
| CT1 | `17`, `1*2.5 mm²` | `18`, `1*2.5 mm²` | DATA LOGGER `I1+`, `I1-` |
| CT2 | `19`, `1*2.5 mm²` | `20`, `1*2.5 mm²` | DATA LOGGER `I2+`, `I2-` |
| CT3 | `21`, `1*2.5 mm²` | `22`, `1*2.5 mm²` | DATA LOGGER `I3+`, `I3-` |
| CT4 | `11`, `1*2.5 mm²` | `12`, `1*2.5 mm²` | KWH1 `I1+`, `I1-` |
| CT5 | `13`, `1*2.5 mm²` | `14`, `1*2.5 mm²` | KWH1 `I2+`, `I2-` |
| CT6 | `15`, `1*2.5 mm²` | `16`, `1*2.5 mm²` | KWH1 `I3+`, `I3-` |

### DATA LOGGER and KWH1 terminal markings

| Drawn block | Terminal text and adjacent wire number(s) |
|---|---|
| DATA LOGGER | `I1+`/`I1-`: `17`/`18`; `I2+`/`I2-`: `19`/`20`; `I3+`/`I3-`: `21`/`22` |
| DATA LOGGER power/voltage side | Vertical label `POWER SUPPLY`; visible numbers `23`, `24`; `N 25`; `L1 26`; `L2 27`; `L3 28` |
| KWH1 | `I1+`/`I1-`: `11`/`12`; `I2+`/`I2-`: `13`/`14`; `I3+`/`I3-`: `15`/`16` |
| KWH1 voltage side | `N 29`; `L1 30`; `L2 31`; `L3 32`; visible numbers `33`, `34` |

### F.KWH1&SIG and terminals

| Item | Text/numbering drawn |
|---|---|
| Three-pole protective symbol | `F.KWH1&SIG`; `6A 3PHASE`; `Type:C` |
| Line side | `35`, `36`, `37`; each conductor is marked `1*1.5mm²` |
| Load side | `38`, `39`, `40`; a fourth parallel conductor is numbered `41` |
| Bottom terminal group | `42`, `43`, `44`; the three conductors are marked `1*1.5mm²`; the printed terminal/phase markings are `R H1`, `S H2`, `T H3` |

## `002.pdf` — lighting and Q0 control wiring

### Supply, fuses, switches, and Lighting

| Drawn path/item | Literal markings |
|---|---|
| Incoming five conductors | `R`, `S`, `T`, `N`, `E` |
| F.CONTROL path | wire `9` → `F.CONTROL` → wire `10`; `1*1.5mm²` |
| F.SOCKET path | wire `7` → `F.SOCKET` → wire `8` → `S0`; `1*1.5mm²` |
| F.LIGHTING path | wire `6` → `F.LIGHTING` → wire `5`; `1*1.5mm²` |
| Lighting path | wire `1` → `S1` → wire `4` → `Lighting`; `1*1.5mm²` |
| Parallel switch path at S1 | `S2` is shown between markings `2` and `3` |

### KWH1 contact, S1 contact, and Q0 box

| Item | Literal markings and drawn connection details |
|---|---|
| KWH1 contact | `KWH1`, terminals `13`, `14`; line markings `X.KWH1 11` and `X.KWH1 12` |
| S1 contact | `S1`, terminals `23`, `24` |
| Q0 control box | `Q0`; `AC 230V`; `POWER SUPPLY`; `P1`, `P2`; terminals `N`, `O` |
| Continuation/net label at the bottom of the Q0 path | `N0`; conductor marking `1*1.5mm²` |

## `003.pdf` — Q1, Q2, Q3

| Device | Literal label beside device | Output conductors as drawn |
|---|---|---|
| Q1 | `MCCB`; `3PHASE`; `100A` | `R`, `S`, `T`, `N`, `E`; the three phase conductors are marked `20*5Mm² CU` |
| Q2 | `MCCB`; `3PHASE`; `100A` | `R`, `S`, `T`, `N`, `E`; the three phase conductors are marked `20*5Mm² CU` |
| Q3 | `MCCB`; `3PHASE`; `100A` | `R`, `S`, `T`, `N`, `E`; the three phase conductors are marked `20*5Mm² CU` |

## `004.pdf` — Q5, CT7–CT9, KWH2, MCB

### Q5 and the control fuse

| Item | Literal label and connection numbering |
|---|---|
| F.CONTROL | `F.CONTROL`; `6A/32A`; `1PHASE`; wire numbers `45`, `46` |
| Q5 | `MCCB WITH MOTOR`; `3PHASE 100A`; motor symbol `M` |
| Q5 line side | `47`, `48`, `49`; each marked `1*2.5mm²` |
| Q5 load side | `50`, `51`, `52`; the two parallel conductors beside them are numbered `53`, `54` |

### CT7–CT9 and KWH2

Every CT in this sheet is printed with `400/5A`, `SVA`, `P1`, and `P2`.

| CT | P1 path | P2 path | KWH2 terminal legends |
|---|---|---|---|
| CT7 | `55`, `1*2.5 mm²` | `56`, `1*2.5 mm²` | `I1+`, `I1-` |
| CT8 | `57`, `1*2.5 mm²` | `58`, `1*2.5 mm²` | `I2+`, `I2-` |
| CT9 | `59`, `1*2.5 mm²` | `60`, `1*2.5 mm²` | `I3+`, `I3-` |

The lower two KWH2 terminals are connected to continuation arrows `61` and `62` and are marked `I3+` and `I3-`.  The KWH2 voltage-terminal legends are `N`, `L1`, `L2`, `L3`; the N conductor is numbered `63` and marked `1*2.5mm²`.

### MCB

| Item | Literal label and connection numbering |
|---|---|
| Three-pole protective symbol | `MCB`; `3PHASE 16A`; `Type:C` |
| Line side | `64`, `65`, `66` |
| Load side | `67`, `68`, `69`; each conductor is marked `1*2.5mm²` and connects to KWH2 `L1`, `L2`, `L3` respectively |

## `005.pdf` — TIMER/controller and Q5 control wiring

### TIMER/controller graphic: all printed face and terminal text

| Area of the graphic | Literal text/marking |
|---|---|
| Graphic title | `TIMER` |
| Face title | `TEMPERATURE CONTROLLER` |
| Model/face label | `TRB-900` |
| Top power labels | `PH`, `N`, `180-250 VAC` |
| Face indicators/marks | `PV`, `SV`, `REL`, `+`, `-` |
| Face text | `SHIVA`, `AMVAJ`, `CODE : 15B2` |
| Bottom terminal strip | `18`, `15`, `16`, `MAX 5A` |

### Contacts, relay, and Q5 control box

| Item | Literal markings and drawn terminals |
|---|---|
| KWH2 contact | `KWH2`, terminals `13`, `14`; line markings `X.KWH2 11`, `X.KWH2 12` |
| S1 contact | `S1`, terminals `23`, `24` |
| R2 coil | `RELAY`, `R2`, `A1`, `A2` |
| R2 contact | `RELAY`, `R2`, terminals `13`, `14` |
| Q5 control box | `Q5`; `AC 230V`; `POWER SUPPLY`; `P1`, `P2`; terminals `C`, `NC` |
| Wire-size marking on this sheet | `1*1.5mm²` |
| Bottom continuation/net label | `N0` |

## `006.pdf` — three 125 A MCCBs

All three symbols are printed `MCCB` and `1PHASE 125A`; no Q reference designator is printed beside them.

| Drawn MCCB | Line-side number | Load-side number and conductor marks |
|---|---:|---|
| First | `70` | `71 R`, `72 N`, `73 E`; each marked `1*2.5mm²`; all three output arrows carry `148` |
| Second | `74` | `75 R`, `76 N`, `77 E`; each marked `1*2.5mm²`; all three output arrows carry `148` |
| Third | `78` | `79 R`, `80 N`, `81 E`; each marked `1*2.5mm²`; all three output arrows carry `148` |

A separate left-side conductor is marked `1*1.5mm²` and terminates at a point labelled `NC`.

## Master-drawing reconciliation

`totall.pdf` is the composite of the six detailed regions above.  It shows the same Q0/CT1–CT6, Lighting/Q0-control, Q1–Q3, Q5/CT7–CT9/KWH2/MCB, TIMER/controller/Q5-control, and three 125 A MCCB regions.  In the master, the two face labels that are separated as `SHIVA` and `AMVAJ` in `005.pdf` appear as the single rendered string `SHIVAAMVAJ`.  The master has no additional labelled component not transcribed in the six sheet sections above.
