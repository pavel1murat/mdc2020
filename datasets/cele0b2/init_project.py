#!/usr/bin/python

from local_classes import *
from mixing_inputs import *

class Project:
#------------------------------------------------------------------------------
# no need to have config files, can do initialization in python directly
#------------------------------------------------------------------------------
    def new_stage(self,name):
        self.fStage[name]            = Stage(name,self);
        return self.fStage[name]

    def dataset(self,dsid):
        return self.fDataset[dsid];

    def __init__(self):

        project                      = 'mdc2020'
        familyID                     = 'cele0b2'

        self.fProjectName            = project;
        self.fFamilyID               = familyID;
        self.fStage                  = {}
        self.fDataset                = {};
#------------------------------------------------------------------------------
# init datasets
# 'r01'-'r09' datasets reconstructed with reco_01 - reco_09 fcl's
#------------------------------------------------------------------------------        
        self.fDataset['cele0b2s41r00'] = Dataset('dig.mu2e.CeEndpointMix2BBSignal.MDC2020r_perfect_v1_0.art'     ,'cele0b2s41r00','local')    # 
        self.fDataset['cele0b2s45r00'] = Dataset('dig.mu2e.CeEndpointMix2BBUntriggered.MDC2020r_perfect_v1_0.art','cele0b2s45r00','local')    # 

        self.fDataset['cele0b2s51r01'] = Dataset('mcs.mu2e.cele0b2s51r01.mdc2020.art'                            ,'cele0b2s51r01','local')    # 
        self.fDataset['cele0b2s51r0104'] = Dataset('mcs.mu2e.cele0b2s51r0104.mdc2020.art'                            ,'cele0b2s51r0104','local')    # 
        self.fDataset['cele0b2s51r02'] = Dataset('mcs.mu2e.cele0b2s51r02.mdc2020.art'                            ,'cele0b2s51r02','local')    # 
        self.fDataset['cele0b2s51r03'] = Dataset('mcs.mu2e.cele0b2s51r03.mdc2020.art'                            ,'cele0b2s51r03','local')    # 
        self.fDataset['cele0b2s51r04'] = Dataset('mcs.mu2e.cele0b2s51r04.mdc2020.art'                            ,'cele0b2s51r04','local')    # 
        self.fDataset['cele0b2s51r05'] = Dataset('mcs.mu2e.cele0b2s51r05.mdc2020.art'                            ,'cele0b2s51r05','local')    # 
        self.fDataset['cele0b2s51r06'] = Dataset('mcs.mu2e.cele0b2s51r06.mdc2020.art'                            ,'cele0b2s51r06','local')    # 
        self.fDataset['cele0b2s51r07'] = Dataset('mcs.mu2e.cele0b2s51r07.mdc2020.art'                            ,'cele0b2s51r07','local')    # 
        self.fDataset['cele0b2s51r08'] = Dataset('mcs.mu2e.cele0b2s51r08.mdc2020.art'                            ,'cele0b2s51r08','local')    # 
        self.fDataset['cele0b2s51r0905'] = Dataset('mcs.mu2e.cele0b2s51r0905.mdc2020.art'                            ,'cele0b2s51r0905','local')    # 
        self.fDataset['cele0b2s51r0a05'] = Dataset('mcs.mu2e.cele0b2s51r0a05.mdc2020.art'                            ,'cele0b2s51r0a05','local')    # 
                                                                                                                 
        self.fDataset['cele0b2s55r01'] = Dataset('mcs.mu2e.cele0b2s55r01.mdc2020.art'                            ,'cele0b2s55r01','local')    # 
        self.fDataset['cele0b2s55r02'] = Dataset('mcs.mu2e.cele0b2s55r02.mdc2020.art'                            ,'cele0b2s55r02','local')    # 
        self.fDataset['cele0b2s55r03'] = Dataset('mcs.mu2e.cele0b2s55r03.mdc2020.art'                            ,'cele0b2s55r03','local')    # 
        self.fDataset['cele0b2s55r04'] = Dataset('mcs.mu2e.cele0b2s55r04.mdc2020.art'                            ,'cele0b2s55r04','local')    # 
        self.fDataset['cele0b2s55r05'] = Dataset('mcs.mu2e.cele0b2s55r05.mdc2020.art'                            ,'cele0b2s55r05','local')    # 
        self.fDataset['cele0b2s55r06'] = Dataset('mcs.mu2e.cele0b2s55r06.mdc2020.art'                            ,'cele0b2s55r06','local')    # 
        self.fDataset['cele0b2s55r07'] = Dataset('mcs.mu2e.cele0b2s55r07.mdc2020.art'                            ,'cele0b2s55r07','local')    # 
        self.fDataset['cele0b2s55r08'] = Dataset('mcs.mu2e.cele0b2s55r08.mdc2020.art'                            ,'cele0b2s55r08','local')    # 
        self.fDataset['cele0b2s55r0904'] = Dataset('mcs.mu2e.cele0b2s55r0904.mdc2020.art'                            ,'cele0b2s55r0904','local')    # 
        self.fDataset['cele0b2s55r0905'] = Dataset('mcs.mu2e.cele0b2s55r0905.mdc2020.art'                            ,'cele0b2s55r0905','local')    # 
        self.fDataset['cele0b2s55r0a04'] = Dataset('mcs.mu2e.cele0b2s55r0a04.mdc2020.art'                            ,'cele0b2s55r0a04','local')    # 
        self.fDataset['cele0b2s55r0a05'] = Dataset('mcs.mu2e.cele0b2s55r0a05.mdc2020.art'                            ,'cele0b2s55r0a05','local')    # 
#------------------------------------------------------------------------------
# init first stage. a Stage can have one or several jobs associated with it
#------------------------------------------------------------------------------        
        s                            = self.new_stage('s5');
#------------------------------------------------------------------------------
# s5:reco_s51r01 : default reco
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        job                          = s.new_job('reco_01','cele0b2s41r00');

        job.fRunNumber               = 1210;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_reco_01_'+familyID+'.fcl'
        job.fRecoVersion             = '01';

        job.fNInputFiles             = -1                                        # placeholder, 
        job.fMaxInputFilesPerSegment =  1                                        # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        odsid                        = self.fFamilyID+'s51'+'r'+job.fRecoVersion;

        job.fOutputStream            = [ 'defaultOutput'                            ]
        job.fOutputDsID              = [ odsid                                      ]
        job.fOutputFnPattern         = [ 'mcs.mu2e.'+job.fOutputDsID[0]+'.'+project ]
        job.fOutputFormat            = [ 'art'                                      ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:cele0b2s41r00:reco_02 : reco with FlagBkgHits+TZFinder+PhiClusterFinder
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        job                          = s.new_job('reco_02','cele0b2s41r00');

        job.fRunNumber               = 1210;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_reco_02_'+familyID+'.fcl'
        job.fRecoVersion             = '02';

        job.fNInputFiles             = -1                                        # placeholder, 
        job.fMaxInputFilesPerSegment =  1                                        # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        odsid                        = self.fFamilyID+'s51'+'r'+job.fRecoVersion;

        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ odsid                           ]
        job.fOutputFnPattern         = [ 'mcs.mu2e.'+job.fOutputDsID[0]+'.'+project ]
        job.fOutputFormat            = [ 'art'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:cele0b2s41r00:reco_03 : reco with DeltaFinder+TZFinder+PhiClusterFinder
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        job                          = s.new_job('reco_03','cele0b2s41r00');

        job.fRunNumber               = 1210;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_reco_03_'+familyID+'.fcl'
        job.fRecoVersion             = '03';

        job.fNInputFiles             = -1                                        # placeholder, 
        job.fMaxInputFilesPerSegment =  1                                        # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        odsid                        = self.fFamilyID+'s51'+'r'+job.fRecoVersion;

        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ odsid                           ]
        job.fOutputFnPattern         = [ 'mcs.mu2e.'+job.fOutputDsID[0]+'.'+project ]
        job.fOutputFormat            = [ 'art'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:reco_s51r04 : default reco, no E<3.5keV cut
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        job                          = s.new_job('reco_r04','cele0b2s41r00');

        job.fRunNumber               = 1210;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_reco_04_'+familyID+'.fcl'

        job.fNInputFiles             = -1                                        # placeholder, 
        job.fMaxInputFilesPerSegment =  1                                        # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        job.fOutputStream            = [ 'defaultOutput'                            ]
        job.fOutputDsID              = [ familyID+'s51r04'                          ]
        job.fOutputFnPattern         = [ 'mcs.mu2e.'+job.fOutputDsID[0]+'.'+project ]
        job.fOutputFormat            = [ 'art'                                      ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:reco_s51r05 : reco with FlagBkgHits+TZFinder+PhiClusterFinder, no Ehit<3.5keV cut in makePH
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        job                          = s.new_job('reco_s51r05','cele0b2s41r00');

        job.fRunNumber               = 1210;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_reco_05_'+familyID+'.fcl'

        job.fNInputFiles             = -1                                        # placeholder, 
        job.fMaxInputFilesPerSegment =  1                                        # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ familyID+'s51r05'               ]
        job.fOutputFnPattern         = [ 'mcs.mu2e.'+job.fOutputDsID[0]+'.'+project ]
        job.fOutputFormat            = [ 'art'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:cele0b2s41r00:reco_06 : reco with DeltaFinder+TZFinder+PhiClusterFinder, no Ehit<3.5keV cut
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        job                          = s.new_job('reco_06','cele0b2s41r00');
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_reco_06_'+familyID+'.fcl'

        job.fRunNumber               = 1210;                                     # not needed, defined by the input dataset
        job.fNInputFiles             = -1                                        # placeholder, 
        job.fMaxInputFilesPerSegment =  1                                        # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        odsid                        = familyID+'s51r06';                        # one output dataset
        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ odsid                           ]
        job.fOutputFnPattern         = [ 'mcs.mu2e.'+job.fOutputDsID[0]+'.'+project ]
        job.fOutputFormat            = [ 'art'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:cele0b2s41r00:reco_07 : reco with DeltaFinder+TZFinder+PhiClusterFinder, 
#                            - no Ehit<3.5keV cut
#                            - up to 4 SH/CH
#------------------------------------------------------------------------------        
        job                          = s.new_job('reco_07','cele0b2s41r00');
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_reco_07_'+familyID+'.fcl'
        job.fRecoVersion             = '07'

        job.fRunNumber               = 1210;                                     # not needed, defined by the input dataset
        job.fNInputFiles             = -1                                        # defined by the input dataset
        job.fMaxInputFilesPerSegment =  1                                        # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        odsid                        = self.fFamilyID+'s51'+job.reco_version();  # one output dataset
        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ odsid                           ]
        job.fOutputFnPattern         = [ 'mcs.mu2e.'+odsid+'.'+project   ]
        job.fOutputFormat            = [ 'art'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:cele0b2s41r00:reco_08 : reco with DeltaFinder+TZFinder+PhiClusterFinder, 
#                            - no Ehit<3.5keV cut
#                            - up to 4 SH/CH
#                            - scale CH errors along the wire
#------------------------------------------------------------------------------        
        job                          = s.new_job('reco_08', 'cele0b2s41r00');
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_reco_08_'+familyID+'.fcl'
        job.fRecoVersion             = '08'

        job.fRunNumber               = 1210;                                     # not needed, defined by the input dataset
        job.fNInputFiles             = -1                                        # defined by the input dataset
        job.fMaxInputFilesPerSegment =  1                                        # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        odsid                        = self.fFamilyID+s.name()+'1'+job.reco_version();  # one output dataset
        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ odsid                           ]
        job.fOutputFnPattern         = [ 'mcs.mu2e.'+odsid+'.'+project   ]
        job.fOutputFormat            = [ 'art'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:cele0b2s41r00:reco_09 : reco with DeltaFinder+TZFinder+PhiClusterFinder, 
#                            - no Ehit<3.5keV cut
#                            - up to 5 SH/CH
#                            - scale CH errors along the wire (PDG prescription)
#------------------------------------------------------------------------------        
        job                          = s.new_job('reco_09', 'cele0b2s41r00');
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_reco_09_'+familyID+'.fcl'
        job.fRecoVersion             = '09'

        job.fRunNumber               = 1210;                                     # not needed, defined by the input dataset
        job.fNInputFiles             = -1                                        # defined by the input dataset
        job.fMaxInputFilesPerSegment =  1                                        # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        odsid                        = self.fFamilyID+s.name()+'1'+job.reco_version();  # one output dataset
        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ odsid                           ]
        job.fOutputFnPattern         = [ 'mcs.mu2e.'+odsid+'.'+project   ]
        job.fOutputFormat            = [ 'art'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:cele0b2s41r00:reco_0a : reco with DeltaFinder+HelixFinderDe
#                            - no Ehit<3.5keV cut
#                            - up to 5 SH/CH
#                            - scale CH errors along the wire (PDG prescription)
#------------------------------------------------------------------------------        
        job                          = s.new_job('reco_0a', 'cele0b2s41r00');
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_reco_0a_'+familyID+'.fcl'
        job.fRecoVersion             = '0a'

        job.fRunNumber               = 1210;                                     # not needed, defined by the input dataset
        job.fNInputFiles             = -1                                        # defined by the input dataset
        job.fMaxInputFilesPerSegment =  1                                        # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        odsid                        = self.fFamilyID+s.name()+'1'+job.reco_version();  # one output dataset
        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ odsid                           ]
        job.fOutputFnPattern         = [ 'mcs.mu2e.'+odsid+'.'+project   ]
        job.fOutputFormat            = [ 'art'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:cele0b2s51r01:stn : default reco
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        idsid                        = 'cele0b2s51r01'
        job                          = s.new_job('stn',idsid);

        job.fRunNumber               = 1210;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_stn_'+familyID+'.fcl'

        job.fNInputFiles             = -1                                        # placeholder, 
        job.fMaxInputFilesPerSegment =  1                                        # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ idsid                           ]
        job.fOutputFnPattern         = [ 'nts.mu2e.'+job.fOutputDsID[0]+'.'+project ]
        job.fOutputFormat            = [ 'stn'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:cele0b2s51r02:stn : (TZClusterFinder+PhiClusterFinder)
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        idsid                        = 'cele0b2s51r02'
        job                          = s.new_job('stn',idsid);

        job.fRunNumber               = 1210;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_stn_'+familyID+'.fcl'

        job.fNInputFiles             = -1                                        # placeholder, 
        job.fMaxInputFilesPerSegment =  1                                        # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ idsid                           ]       # ntupling: odsid=idsid
        job.fOutputFnPattern         = [ 'nts.mu2e.'+job.fOutputDsID[0]+'.'+project ]
        job.fOutputFormat            = [ 'stn'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:cele0b2s51r03:stn : DeltaFinder+TZFinder+PhiClusterFinder
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        idsid                        = 'cele0b2s51r03'
        job                          = s.new_job('stn',idsid);

        job.fRunNumber               = 1210;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_stn_'+familyID+'.fcl'

        job.fNInputFiles             = -1                                        # placeholder, 
        job.fMaxInputFilesPerSegment =  1                                        # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ idsid                           ]       # ntupling: odsid=idsid
        job.fOutputFnPattern         = [ 'nts.mu2e.'+job.fOutputDsID[0]+'.'+project ]
        job.fOutputFormat            = [ 'stn'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:stn_s51r04 : default reco
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        idsid                        = 'cele0b2s51r04'
        job                          = s.new_job('stn_s51r04',idsid);

        job.fRunNumber               = 1210;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_stn_'+familyID+'.fcl'

        job.fNInputFiles             = -1                                        # placeholder, 
        job.fMaxInputFilesPerSegment =  1                                        # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ idsid                           ]
        job.fOutputFnPattern         = [ 'nts.mu2e.'+job.fOutputDsID[0]+'.'+project ]
        job.fOutputFormat            = [ 'stn'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:cele0b2s51r05:stn : (TZClusterFinder+PhiClusterFinder)
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        idsid                        = 'cele0b2s51r05'
        job                          = s.new_job('stn',idsid);

        job.fRunNumber               = 1210;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_stn_'+familyID+'.fcl'

        job.fNInputFiles             = -1                                        # placeholder, 
        job.fMaxInputFilesPerSegment =  1                                        # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ idsid                           ]       # ntupling: odsid=idsid
        job.fOutputFnPattern         = [ 'nts.mu2e.'+job.fOutputDsID[0]+'.'+project ]
        job.fOutputFormat            = [ 'stn'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:cele0b2s51r06:stn : DeltaFinder+TZFinder+PhiClusterFinder
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        idsid                        = 'cele0b2s51r06'
        job                          = s.new_job('stn',idsid);

        job.fRunNumber               = 1210;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_stn_'+familyID+'.fcl'

        job.fNInputFiles             = -1                                        # placeholder, 
        job.fMaxInputFilesPerSegment =  1                                        # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ idsid                           ]       # ntupling: odsid=idsid
        job.fOutputFnPattern         = [ 'nts.mu2e.'+job.fOutputDsID[0]+'.'+project ]
        job.fOutputFormat            = [ 'stn'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:cele0b2s51r07:stn : DeltaFinder+TZFinder+PhiClusterFinder
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        idsid                        = 'cele0b2s51r07';
        job                          = s.new_job('stn',idsid);

        job.fRunNumber               = 1210;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_stn_'+familyID+'.fcl'
        job.fRecoVersion             = '07'

        job.fNInputFiles             = -1                                        # placeholder, 
        job.fMaxInputFilesPerSegment =  1                                        # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ idsid                           ]       # ntupling: odsid=idsid
        job.fOutputFnPattern         = [ 'nts.mu2e.'+job.fOutputDsID[0]+'.'+project ]
        job.fOutputFormat            = [ 'stn'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:cele0b2s51r08:stn : DeltaFinder+TZFinder+PhiClusterFinder
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        idsid                        = 'cele0b2s51r08';
        job                          = s.new_job('stn',idsid);

        job.fRunNumber               = 1210;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_stn_'+familyID+'.fcl'
        job.fRecoVersion             = '08'

        job.fNInputFiles             = -1                                        # placeholder, 
        job.fMaxInputFilesPerSegment =  1                                        # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ idsid                           ]       # ntupling: odsid=idsid
        job.fOutputFnPattern         = [ 'nts.mu2e.'+job.fOutputDsID[0]+'.'+project ]
        job.fOutputFormat            = [ 'stn'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:cele0b2s51r0905:stn : DeltaFinder+TZFinder+PhiClusterFinder
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        idsid                        = 'cele0b2s51r0905';
        job                          = s.new_job('stn',idsid);

        job.fRunNumber               = 1210;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_stn_'+familyID+'.fcl'
        job.fRecoVersion             = '09'

        job.fNInputFiles             = -1                                        # placeholder, 
        job.fMaxInputFilesPerSegment =  1                                        # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ idsid                           ]       # ntupling: odsid=idsid
        job.fOutputFnPattern         = [ 'nts.mu2e.'+job.fOutputDsID[0]+'.'+project ]
        job.fOutputFormat            = [ 'stn'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:cele0b2s51r0a05:stn : DeltaFinder+TZFinder+PhiClusterFinder
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        idsid                        = 'cele0b2s51r0a05';
        job                          = s.new_job('stn',idsid);

        job.fRunNumber               = 1210;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_stn_'+familyID+'.fcl'
        job.fRecoVersion             = '0a'

        job.fNInputFiles             = -1                                        # placeholder, 
        job.fMaxInputFilesPerSegment =  1                                        # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ idsid                           ]       # ntupling: odsid=idsid
        job.fOutputFnPattern         = [ 'nts.mu2e.'+job.fOutputDsID[0]+'.'+project ]
        job.fOutputFormat            = [ 'stn'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:cele0b2s45r00:reco_01 : default reco
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        idsid                        = 'cele0b2s45r00';
        job                          = s.new_job('reco_01',idsid);

        job.fRunNumber               = 1210;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_reco_01_'+familyID+'.fcl'

        job.fNInputFiles             = -1                                        # placeholder, 
        job.fMaxInputFilesPerSegment =  1                                        # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        job.fOutputStream            = [ 'defaultOutput'                            ]
        job.fOutputDsID              = [ familyID+'s55r01'                          ]
        job.fOutputFnPattern         = [ 'mcs.mu2e.'+job.fOutputDsID[0]+'.'+project ]
        job.fOutputFormat            = [ 'art'                                      ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:cele0b2s45r00:reco_02 : reco with FlagBkgHits+TZFinder+PhiClusterFinder
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        idsid                        = 'cele0b2s45r00';
        job                          = s.new_job('reco_02',idsid);

        job.fRunNumber               = 1210;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_reco_02_'+familyID+'.fcl'

        job.fNInputFiles             = -1                                        # placeholder, 
        job.fMaxInputFilesPerSegment =  1                                        # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ familyID+'s55r02'               ]
        job.fOutputFnPattern         = [ 'mcs.mu2e.'+job.fOutputDsID[0]+'.'+project ]
        job.fOutputFormat            = [ 'art'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:cele0b2s45r00:reco_03 : reco with DeltaFinder+TZFinder+PhiClusterFinder
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        idsid                        = 'cele0b2s45r00';
        job                          = s.new_job('reco_03',idsid);

        job.fRunNumber               = 1210;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_reco_03_'+familyID+'.fcl'

        job.fNInputFiles             = -1                                        # placeholder, 
        job.fMaxInputFilesPerSegment =  1                                        # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ familyID+'s55r03'               ]
        job.fOutputFnPattern         = [ 'mcs.mu2e.'+job.fOutputDsID[0]+'.'+project ]
        job.fOutputFormat            = [ 'art'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:cele0b2s45r00:reco_04 : reco without E>3.5keV cut
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        idsid                        = 'cele0b2s45r00';
        job                          = s.new_job('reco_04',idsid);

        job.fRunNumber               = 1210;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_reco_04_'+familyID+'.fcl'

        job.fNInputFiles             = -1                                        # placeholder, 
        job.fMaxInputFilesPerSegment =  100                                      # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        job.fOutputStream            = [ 'defaultOutput'                            ]
        job.fOutputDsID              = [ familyID+'s55r04'                          ]
        job.fOutputFnPattern         = [ 'mcs.mu2e.'+job.fOutputDsID[0]+'.'+project ]
        job.fOutputFormat            = [ 'art'                                      ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:cele0b2s45r00:reco_05 : reco with FlagBkgHits+TZFinder+PhiClusterFinder w/o E>3.5keV cut
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        idsid                        = 'cele0b2s45r00';
        job                          = s.new_job('reco_05',idsid);

        job.fRunNumber               = 1210;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_reco_05_'+familyID+'.fcl'

        job.fNInputFiles             = -1                                        # placeholder, 
        job.fMaxInputFilesPerSegment =  100                                      # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ familyID+'s55r05'               ]
        job.fOutputFnPattern         = [ 'mcs.mu2e.'+job.fOutputDsID[0]+'.'+project ]
        job.fOutputFormat            = [ 'art'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:cele0b2s45r00:reco_06 : reco with DeltaFinder+TZFinder+PhiClusterFinder
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        idsid                        = 'cele0b2s45r00';
        job                          = s.new_job('reco_06',idsid);

        job.fRunNumber               = 1210;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_reco_06_'+familyID+'.fcl'

        job.fNInputFiles             = -1                                        # placeholder, 
        job.fMaxInputFilesPerSegment =  100                                      # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ familyID+'s55r06'               ]
        job.fOutputFnPattern         = [ 'mcs.mu2e.'+job.fOutputDsID[0]+'.'+project ]
        job.fOutputFormat            = [ 'art'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:cele0b2s45r00:reco_07 : reco with DeltaFinder+TZFinder+PhiClusterFinder, 
#                            - no Ehit<3.5keV cut
#                            - up to 4 SH/CH
# fileset:100
#------------------------------------------------------------------------------        
        idsid                        = 'cele0b2s45r00';
        job                          = s.new_job('reco_07',idsid);
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_reco_07_'+familyID+'.fcl'
        job.fRecoVersion             = '07'

        job.fRunNumber               = 1210;                                     # not needed, defined by the input dataset
        job.fNInputFiles             = -1                                        # defined by the input dataset
        job.fMaxInputFilesPerSegment =  100                                        # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        odsid                        = self.fFamilyID+'s51'+job.reco_version();  # one output dataset
        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ odsid                           ]
        job.fOutputFnPattern         = [ 'mcs.mu2e.'+odsid+'.'+project   ]
        job.fOutputFormat            = [ 'art'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:cele0b2s45r00:reco_08 : reco with DeltaFinder+TZFinder+PhiClusterFinder, 
#                            - no Ehit<3.5keV cut
#                            - up to 4 SH/CH
#                            - scale CH errors along the wire
# fileset:100
#------------------------------------------------------------------------------        
        idsid                        = 'cele0b2s45r00';
        job                          = s.new_job('reco_08',idsid);
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_reco_08_'+familyID+'.fcl'
        job.fRecoVersion             = '08'

        job.fRunNumber               = 1210;                                     # not needed, defined by the input dataset
        job.fNInputFiles             = -1                                        # defined by the input dataset
        job.fMaxInputFilesPerSegment =  100                                        # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        odsid                        = self.fFamilyID+'s55'+job.reco_version();  # one output dataset
        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ odsid                           ]
        job.fOutputFnPattern         = [ 'mcs.mu2e.'+odsid+'.'+project   ]
        job.fOutputFormat            = [ 'art'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:cele0b2s45r00:reco_09 : reco with DeltaFinder+TZFinder+PhiClusterFinder, 
#                            - no Ehit<3.5keV cut
#                            - up to 5 SH/CH
#                            - scale CH errors along the wire
# fileset:100
#------------------------------------------------------------------------------        
        idsid                        = 'cele0b2s45r00';
        job                          = s.new_job('reco_09',idsid);
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_reco_09_'+familyID+'.fcl'
        job.fRecoVersion             = '09'

        job.fRunNumber               = 1210;                                     # not needed, defined by the input dataset
        job.fNInputFiles             = -1                                        # defined by the input dataset
        job.fMaxInputFilesPerSegment =  100                                        # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        odsid                        = self.fFamilyID+'s55'+job.reco_version();  # one output dataset
        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ odsid                           ]
        job.fOutputFnPattern         = [ 'mcs.mu2e.'+odsid+'.'+project   ]
        job.fOutputFormat            = [ 'art'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:cele0b2s45r00:reco_09a : reco with DeltaFinder+TimeClusterFinder
#                            - no Ehit<3.5keV cut
#                            - up to 5 SH/CH
#                            - scale CH errors along the wire
# fileset:100
#------------------------------------------------------------------------------        
        idsid                        = 'cele0b2s45r00';
        job                          = s.new_job('reco_0a',idsid);
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_reco_0a_'+familyID+'.fcl'
        job.fRecoVersion             = '0a'

        job.fRunNumber               = 1210;                                     # not needed, defined by the input dataset
        job.fNInputFiles             = -1                                        # defined by the input dataset
        job.fMaxInputFilesPerSegment =  100                                        # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        odsid                        = self.fFamilyID+'s55'+job.reco_version();  # one output dataset
        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ odsid                           ]
        job.fOutputFnPattern         = [ 'mcs.mu2e.'+odsid+'.'+project   ]
        job.fOutputFormat            = [ 'art'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:cele0b2s55r01:stn : default reco
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        idsid                        = 'cele0b2s55r01'
        job                          = s.new_job('stn',idsid);

        job.fRunNumber               = 1210;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_stn_'+familyID+'.fcl'

        job.fNInputFiles             = -1                                        # placeholder, 
        job.fMaxInputFilesPerSegment =  100                                      # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ idsid                           ]
        job.fOutputFnPattern         = [ 'nts.mu2e.'+job.fOutputDsID[0]+'.'+project ]
        job.fOutputFormat            = [ 'stn'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:cele0b2s55r02:stn : (TZClusterFinder+PhiClusterFinder)
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        idsid                        = 'cele0b2s55r02'
        job                          = s.new_job('stn',idsid);

        job.fRunNumber               = 1210;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_stn_'+familyID+'.fcl'

        job.fNInputFiles             = -1                                        # placeholder, 
        job.fMaxInputFilesPerSegment =  1                                        # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ idsid                           ]       # ntupling: odsid=idsid
        job.fOutputFnPattern         = [ 'nts.mu2e.'+job.fOutputDsID[0]+'.'+project ]
        job.fOutputFormat            = [ 'stn'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:cele0b2s55r03:stn : DeltaFinder+TZFinder+PhiClusterFinder
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        idsid                        = 'cele0b2s55r03'
        job                          = s.new_job('stn',idsid);

        job.fRunNumber               = 1210;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_stn_'+familyID+'.fcl'

        job.fNInputFiles             = -1                                        # placeholder, 
        job.fMaxInputFilesPerSegment =  1                                        # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ idsid                           ]       # ntupling: odsid=idsid
        job.fOutputFnPattern         = [ 'nts.mu2e.'+job.fOutputDsID[0]+'.'+project ]
        job.fOutputFormat            = [ 'stn'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:cele0b2s55r04:stn : default reco
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        idsid                        = 'cele0b2s55r04'
        job                          = s.new_job('stn',idsid);

        job.fRunNumber               = 1210;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_stn_'+familyID+'.fcl'

        job.fNInputFiles             = -1                                        # placeholder, 
        job.fMaxInputFilesPerSegment =  1                                        # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ idsid                           ]
        job.fOutputFnPattern         = [ 'nts.mu2e.'+job.fOutputDsID[0]+'.'+project ]
        job.fOutputFormat            = [ 'stn'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:cele0b2s55r05:stn : (TZClusterFinder+PhiClusterFinder)
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        idsid                        = 'cele0b2s55r05'
        job                          = s.new_job('stn',idsid);

        job.fRunNumber               = 1210;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_stn_'+familyID+'.fcl'

        job.fNInputFiles             = -1                                        # placeholder, 
        job.fMaxInputFilesPerSegment =  1                                        # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ idsid                           ]       # ntupling: odsid=idsid
        job.fOutputFnPattern         = [ 'nts.mu2e.'+job.fOutputDsID[0]+'.'+project ]
        job.fOutputFormat            = [ 'stn'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:cele0b2s55r06:stn : DeltaFinder+TZFinder+PhiClusterFinder
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        idsid                        = 'cele0b2s55r06'
        job                          = s.new_job('stn',idsid);

        job.fRunNumber               = 1210;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_stn_'+familyID+'.fcl'

        job.fNInputFiles             = -1                                        # placeholder, 
        job.fMaxInputFilesPerSegment =  1                                        # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ idsid                           ]       # ntupling: odsid=idsid
        job.fOutputFnPattern         = [ 'nts.mu2e.'+job.fOutputDsID[0]+'.'+project ]
        job.fOutputFormat            = [ 'stn'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:cele0b2s55r08:stn : DeltaFinder+TZFinder+PhiClusterFinder
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        idsid                        = 'cele0b2s55r08'
        job                          = s.new_job('stn',idsid);

        job.fRunNumber               = 1210;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_stn_'+familyID+'.fcl'

        job.fNInputFiles             = -1                                        # placeholder, 
        job.fMaxInputFilesPerSegment =  1                                        # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ idsid                           ]       # ntupling: odsid=idsid
        job.fOutputFnPattern         = [ 'nts.mu2e.'+job.fOutputDsID[0]+'.'+project ]
        job.fOutputFormat            = [ 'stn'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:cele0b2s55r0904:stn : DeltaFinder+TZFinder+PhiClusterFinder
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        idsid                        = 'cele0b2s55r0904'
        job                          = s.new_job('stn',idsid);

        job.fRunNumber               = 1210;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_stn_'+familyID+'.fcl'

        job.fNInputFiles             = -1                                        # placeholder, 
        job.fMaxInputFilesPerSegment =  1                                        # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ idsid                           ]       # ntupling: odsid=idsid
        job.fOutputFnPattern         = [ 'nts.mu2e.'+job.fOutputDsID[0]+'.'+project ]
        job.fOutputFormat            = [ 'stn'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:cele0b2s55r0905:stn : DeltaFinder+TZFinder+PhiClusterFinder
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        idsid                        = 'cele0b2s55r0905'
        job                          = s.new_job('stn',idsid);

        job.fRunNumber               = 1210;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_stn_'+familyID+'.fcl'

        job.fNInputFiles             = -1                                        # placeholder, 
        job.fMaxInputFilesPerSegment =  1                                        # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ idsid                           ]       # ntupling: odsid=idsid
        job.fOutputFnPattern         = [ 'nts.mu2e.'+job.fOutputDsID[0]+'.'+project ]
        job.fOutputFormat            = [ 'stn'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:cele0b2s55r0a04:stn : DeltaFinder+TZFinder+PhiClusterFinder
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        idsid                        = 'cele0b2s55r0a04'
        job                          = s.new_job('stn',idsid);

        job.fRunNumber               = 1210;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_stn_'+familyID+'.fcl'

        job.fNInputFiles             = -1                                        # placeholder, 
        job.fMaxInputFilesPerSegment =  1                                        # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ idsid                           ]       # ntupling: odsid=idsid
        job.fOutputFnPattern         = [ 'nts.mu2e.'+job.fOutputDsID[0]+'.'+project ]
        job.fOutputFormat            = [ 'stn'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:cele0b2s55r0a05:stn : DeltaFinder+TZFinder+PhiClusterFinder
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        idsid                        = 'cele0b2s55r0a05'
        job                          = s.new_job('stn',idsid);

        job.fRunNumber               = 1210;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_stn_'+familyID+'.fcl'

        job.fNInputFiles             = -1                                        # placeholder, 
        job.fMaxInputFilesPerSegment =  1                                        # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ idsid                           ]       # ntupling: odsid=idsid
        job.fOutputFnPattern         = [ 'nts.mu2e.'+job.fOutputDsID[0]+'.'+project ]
        job.fOutputFormat            = [ 'stn'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# end
#------------------------------------------------------------------------------
