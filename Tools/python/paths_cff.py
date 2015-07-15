class HltPathConfig :
    """Configuration class for paths of which efficiency has to be studied"""

    def __init__(self) :    
        self.TRIGNAME = "DUMMY"
        self.PROBEDEN = [ ] 
        self.PROBENUM = [ ] 
        self.NAMEPLOT = [ ] 

    def __init__(self, TRIGNAME, PROBEDEN, PROBENUM, NAMEPLOT) :
        self.TRIGNAME = TRIGNAME 
        self.PROBEDEN = PROBEDEN 
        self.PROBENUM = PROBENUM 
        self.NAMEPLOT = NAMEPLOT
    

# CB extend the path list, may be make paths cff per menu

IsoMu20 = HltPathConfig("IsoMu20",
                       [ "",     "",                     "hltL1sL1SingleMu16",                  "hltL2fL1sMu16L1f0L2Filtered10Q",       "hltL3fL1sMu16L1f0L2f10QL3Filtered20Q"                  ],
                       [ "",     "hltL1sL1SingleMu16", "hltL2fL1sMu16L1f0L2Filtered10Q",  "hltL3fL1sMu16L1f0L2f10QL3Filtered20Q", "hltL3crIsoL1sMu16L1f0L2f10QL3f20QL3trkIsoFiltered0p09" ],
                       [ "Full", "L1",                   "L2overL1",                              "L3overL2",                                   "ISOoverL3"                                                   ])

Mu20 = HltPathConfig("Mu20",
                     [ "",     "",                   "hltL1sL1SingleMu16",               "hltL2fL1sMu16L1f0L2Filtered10Q",      ],
                     [ "",     "hltL1sL1SingleMu16", "hltL2fL1sMu16L1f0L2Filtered10Q",   "hltL3fL1sMu16L1f0L2f10QL3Filtered20Q" ],
                     [ "Full", "L1",                 "L2overL1",                         "L3overL2",                            ])

IsoMu17_eta2p1 = HltPathConfig("IsoMu17_eta2p1",
                     [ "",     "",                   "hltL1sSingleMu16er",			"hltL2fL1sSingleMu16erL1f0L2Filtered10Q",	"hltL3fL1sSingleMu16erL1f0L2f10QL3Filtered17Q"			],
                     [ "",     "hltL1sSingleMu16er", "hltL2fL1sSingleMu16erL1f0L2Filtered10Q",	"hltL3fL1sSingleMu16erL1f0L2f10QL3Filtered17Q", "hltL3crIsoL1sSingleMu16erL1f0L2f10QL3f17QL3trkIsoFiltered0p09"	],
                     [ "Full", "L1",                 "L2overL1",				"L3overL2",					"ISOoverL3"							])

Mu50 = HltPathConfig("Mu50",
                     [ "",     "",                   			"hltL1sL1SingleMu16ORSingleMu25",	"hltL2fL1sMu16orMu25L1f0L2Filtered16Q",		],
                     [ "",     "hltL1sL1SingleMu16ORSingleMu25",	"hltL2fL1sMu16orMu25L1f0L2Filtered16Q",	"hltL3fL1sMu16orMu25L1f0L2f16QL3Filtered50Q"	],
                     [ "Full", "L1",                 			"L2overL1",                         	"L3overL2",					])

