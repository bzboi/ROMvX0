const videoZ = &h100
const startVideo = &h103
const vBlankStart = &h104
const vblankExpansion = &h12e
const vPulseInit = &h135
const sound1 = &h158
const vBlankNormal = &h191
const vBlankSample = &h198
const videoA = &h201
const pixels = &h20a
const sound3 = &h2ae
const sound2 = &h2b1
const videoB = &h2ca
const videoC = &h2d3
const videoD = &h2dc
const videoE = &h2e9
const videoF = &h2ec
const nopixels = &h2f6
const ENTER = &h2ff
const NEXTY = &h300
const NEXT = &h301
const EXIT = &h30b
const RESYNC = &h30c
const LDWI = &h311
const DEC = &h314
const MOVQB = &h316
const LSRB = &h318
const LD = &h31a
const ADDBI = &h31c
const SPARE0 = &h31f
const LDW = &h321
const POKEI = &h325
const LSLV = &h327
const ADDVB = &h329
const STW = &h32b
const CNVXY = &h32d
const PREFX2 = &h32f
const MOVWA = &h332
const BCC = &h335
const SUBBI = &h338
const DEEKV = &h33b
const ARRVW = &h33d
const LDARRW = &h33f
const ADDVI = &h342
const SUBVI = &h344
const SUBVB = &h348
const DJGE = &h34a
const MOVQW = &h34d
const STWM = &h34f
const STARRW = &h351
const LDARRB = &h353
const STARRB = &h355
const STARRI = &h357
const LDI = &h359
const PEEKV = &h35b
const ST = &h35e
const POP = &h363
const MOVB = &h365
const PEEKA = &h367
const POKEA = &h369
const TEQ = &h36b
const TNE = &h36d
const DEEKA = &h36f
const LDWM = &h372
const PUSH = &h375
const DOKEI = &h377
const ARRW = &h379
const SCRLHR = &h37b
const DOKEA = &h37d
const LUP = &h37f
const ANDI = &h382
const CALLI = &h385
const ORI = &h388
const XORI = &h38c
const DBGE = &h38e
const BRA = &h390
const INC = &h393
const INCWA = &h395
const SPARE1 = &h397
const ADDW = &h399
const LDNI = &h39c
const DBNE = &h39e
const DEEKR = &h3a0
const PACKAW = &h3a2
const DJNE = &h3a4
const CMPI = &h3a7
const ADDVW = &h3a9
const SUBVW = &h3ab
const PEEK = &h3ad
const PREFX1 = &h3b1
const SYS = &h3b4
const SUBW = &h3b8
const JEQ = &h3bb
const JNE = &h3bd
const JLT = &h3bf
const JGT = &h3c1
const JLE = &h3c3
const JGE = &h3c5
const PREFX3 = &h3c7
const REENTER = &h3cb
const DEF = &h3cd
const CALL = &h3cf
const TGE = &h3d5
const TLT = &h3d7
const TGT = &h3d9
const TLE = &h3db
const DECWA = &h3dd
const ALLOC = &h3df
const PACKVW = &h3e1
const ADDI = &h3e3
const SUBI = &h3e6
const LSLW = &h3e9
const STLW = &h3ec
const LDLW = &h3ee
const POKE = &h3f0
const DOKE = &h3f3
const DEEK = &h3f6
const ANDW = &h3f8
const ORW = &h3fa
const XORW = &h3fc
const RET = &h3ff
const shiftTable = &h500
const font32up = &h700
const font82up = &h800
const notesTable = &h900
const noteTrampoline = &h9c0
const STB2 = &h2211
const STW2 = &h2214
const XCHGB = &h2217
const MOVW = &h2219
const ADDWI = &h221b
const SUBWI = &h221d
const ANDWI = &h221f
const ORWI = &h2221
const XORWI = &h2223
const FNT6X8 = &h2225
const FNT4X6 = &h2228
const CONDII = &h222a
const CONDBB = &h222c
const CONDIB = &h222f
const CONDBI = &h2232
const XCHGW = &h2234
const OSCPX = &h2237
const SWAPB = &h2239
const SWAPW = &h223c
const NEEKA = &h223f
const NOKEA = &h2242
const ADDVL = &h2245
const SUBVL = &h2248
const ANDVL = &h224b
const ORVL = &h224e
const XORVL = &h2251
const JEQL = &h2254
const JNEL = &h2257
const JLTL = &h225a
const JGTL = &h225d
const JLEL = &h2260
const JGEL = &h2263
const ANDBI = &h2266
const ORBI = &h2269
const XORBI = &h226c
const ANDBK = &h226f
const ORBK = &h2272
const XORBK = &h2275
const JMPI = &h2278
const SUBIW = &h227b
const VADDBW = &h227d
const VSUBBW = &h2280
const VADDBL = &h2283
const VSUBBL = &h2286
const CMPII = &h2289
const IMIDI = &h228b
const PMIDI = &h228e
const PMIDIV = &h2291
const MERGE4 = &h2294
const MOVL = &h22cd
const MOVF = &h22d0
const NROL = &h22d3
const NROR = &h22d6
const LSLN = &h2311
const SEXT = &h2313
const NOTW = &h2315
const NEGW = &h2317
const ANDBA = &h2319
const ORBA = &h231c
const XORBA = &h231f
const FREQM = &h2322
const FREQA = &h2324
const FREQI = &h2327
const VOLM = &h2329
const VOLA = &h232c
const MODA = &h232f
const MODI = &h2332
const SMPCPY = &h2334
const CMPHS = &h2337
const CMPHU = &h233a
const LEEKA = &h233d
const LOKEA = &h233f
const FEEKA = &h2341
const FOKEA = &h2343
const MEEKA = &h2345
const MOKEA = &h2347
const LSRVL = &h2349
const LSLVL = &h234c
const INCL = &h234f
const DECL = &h2352
const STPX = &h2354
const PRN4X6 = &h2357
const VTBL = &h2359
const OSCZ = &h235c
const LSL8 = &h235e
const ADDBA = &h2360
const SUBBA = &h2362
const NOTB = &h2364
const ABSVW = &h2367
const INCW = &h236a
const DECW = &h236c
const WAITVV = &h236e
const LSRV = &h2373
const DEEKRI = &h2375
const SCRLH = &h2377
const MULB = &h237a
const NCOPY = &h23cd
const STLU = &h23d0
const STLS = &h23d3
const NOTL = &h23d5
const NEGL = &h23d8
const NOTE = &h2411
const MIDI = &h2414
const XLA = &h2417
const ADDLP = &h241a
const SUBLP = &h241d
const ANDLP = &h2420
const ORLP = &h2423
const XORLP = &h2426
const CMPLPU = &h2429
const CMPLPS = &h242c
const RANDW = &h242f
const LDPX = &h2431
const ABSW = &h2433
const SGNW = &h2436
const MULB3 = &h2439
const MULB5 = &h243b
const MULB6 = &h243d
const MULB7 = &h243f
const MULB8 = &h2441
const MULB9 = &h2443
const MULB10 = &h2445
const WAITVB = &h2447
const MULW3 = &h2449
const MULW5 = &h244b
const MULW6 = &h244d
const MULW7 = &h244f
const MULW8 = &h2451
const MULW9 = &h2453
const MULW10 = &h2455
const prn4x6Return = &h3585
const memSize = &h1
const entropy0 = &h6
const entropy1 = &h7
const videoY = &h9
const frameCount = &he
const serialRaw = &hf
const buttonState = &h11
const xoutMask = &h14
const vPC = &h16
const vAC = &h18
const vACH = &h19
const vLR = &h1a
const vSP = &h1c
const vTmp = &h1d
const romType = &h21
const sysFn = &h22
const sysArgs0 = &h24
const sysArgs1 = &h25
const sysArgs2 = &h26
const sysArgs3 = &h27
const sysArgs4 = &h28
const sysArgs5 = &h29
const sysArgs6 = &h2a
const sysArgs7 = &h2b
const soundTimer = &h2c
const userVars = &h30
const videoTable = &h100
const userCode = &h200
const soundTable = &h700
const screenMemory = &h800
const vReset = &h1f0
const wavA = &hfa
const wavX = &hfb
const keyL = &hfc
const keyH = &hfd
const oscL = &hfe
const oscH = &hff
const maxTicks = &hf
const qqVgaWidth = &ha0
const qqVgaHeight = &h78
const buttonRight = &h1
const buttonLeft = &h2
const buttonDown = &h4
const buttonUp = &h8
const buttonStart = &h10
const buttonSelect = &h20
const buttonB = &h40
const buttonA = &h80
const Credits = &h500e
const Clock = &h54f9
const Invader = &h61de
const VideoPoker = &h850e
const TinyBASIC = &ha30e
const Statements2 = &h500
const Hexnum = &h5ce
const GetLine2 = &h6e8
const Statements5 = &hdeb
const Print = &h13a0
const Statements3 = &h14a0
const Statements4 = &h15a0
const Statements6 = &h16a0
const Save = &h17a0
const Newline = &h18a0
const Line = &h19a0
const Line2 = &h1aa0
const Buffer = &h1ba0
const BasicProgram = &h1bc0
const Egg = &haf96
const SDCard = &hb484
const Loader = &hbf56
const Boot = &hbf7e
const Main = &hcaf1
const Reset = &hdc0e
const Command = &h81
