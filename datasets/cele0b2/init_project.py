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

    def __init__(self):

        project                      = 'mdc2020'
        familyID                     = 'cele0b2'

        self.fProjectName            = project;
        self.fFamilyID               = familyID;
        self.fStage                  = {}
#------------------------------------------------------------------------------
# init first stage. a Stage can have one or several jobs associated with it
#------------------------------------------------------------------------------        
        s                            = self.new_stage('s5');
#------------------------------------------------------------------------------
# s5:reco_s51r01 : default reco
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        job                          = s.new_job('reco_s5101');

        job.fRunNumber               = 1000;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_reco_01_'+familyID+'.fcl'

        defname                      = 'dig.mu2e.CeEndpointMix2BBSignal.MDC2020r_perfect_v1_0.art' # dataset definition name
        job.fInputDataset            = Dataset(defname,'cele0b2s41r00','local')    # 
        job.fNInputFiles             = -1                                        # placeholder, 
        job.fMaxInputFilesPerSegment =  1                                        # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        job.fOutputStream            = [ 'defaultOutput'                            ]
        job.fOutputDsID              = [ familyID+'s51r01'                          ]
        job.fOutputFnPattern         = [ 'mcs.mu2e.'+job.fOutputDsID[0]+'.'+project ]
        job.fOutputFormat            = [ 'art'                                      ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:reco_s51r02 : reco with FlagBkgHits+TZFinder+PhiClusterFinder
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        job                          = s.new_job('reco_s51r02');

        job.fRunNumber               = 1000;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_reco_02_'+familyID+'.fcl'

        defname                      = 'dig.mu2e.CeEndpointMix2BBSignal.MDC2020r_perfect_v1_0.art' # dataset definition name
        job.fInputDataset            = Dataset(defname,'cele0b2s41r00','local')    # 
        job.fNInputFiles             = -1                                        # placeholder, 
        job.fMaxInputFilesPerSegment =  1                                        # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ familyID+'s51r02'               ]
        job.fOutputFnPattern         = [ 'mcs.mu2e.'+job.fOutputDsID[0]+'.'+project ]
        job.fOutputFormat            = [ 'art'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:reco_s51r03 : reco with DeltaFinder+TZFinder+PhiClusterFinder
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        job                          = s.new_job('reco_s51r03');

        job.fRunNumber               = 1000;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_reco_03_'+familyID+'.fcl'

        defname                      = 'dig.mu2e.CeEndpointMix2BBSignal.MDC2020r_perfect_v1_0.art' # dataset definition name
        job.fInputDataset            = Dataset(defname,'cele0b2s41r00','local')    # 
        job.fNInputFiles             = -1                                        # placeholder, 
        job.fMaxInputFilesPerSegment =  1                                        # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ familyID+'s53r03'               ]
        job.fOutputFnPattern         = [ 'mcs.mu2e.'+job.fOutputDsID[0]+'.'+project ]
        job.fOutputFormat            = [ 'art'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:stn_s51r01 : default reco
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        job                          = s.new_job('stn_s51r01');

        job.fRunNumber               = 1000;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_stn_'+familyID+'.fcl'

        idsid                        = 'cele0b2s51r01'
        defname                      = 'mcs.mu2e.'+idsid+'.mdc2020.art'          # dataset definition name
        job.fInputDataset            = Dataset(defname,idsid,'local')            # 
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
# s5:stn_s51r02 : (TZClusterFinder+PhiClusterFinder)
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        job                          = s.new_job('stn_s51r02');

        job.fRunNumber               = 1000;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_stn_'+familyID+'.fcl'

        idsid                        = 'cele0b2s51r02'
        defname                      = 'mcs.mu2e.'+idsid+'.mdc2020.art'          # dataset definition name
        job.fInputDataset            = Dataset(defname,idsid,'local')            # 
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
# s5:stn_s51r03 : DeltaFinder+TZFinder+PhiClusterFinder
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        job                          = s.new_job('stn_s51r03');

        job.fRunNumber               = 1000;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_stn_'+familyID+'.fcl'

        idsid                        = 'cele0b2s51r03'
        defname                      = 'mcs.mu2e.'+idsid+'.mdc2020.art'          # dataset definition name
        job.fInputDataset            = Dataset(defname,idsid,'local')            # 
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
# s5:reco_s55r01 : default reco
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        job                          = s.new_job('reco_s5501');

        job.fRunNumber               = 1000;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_reco_01_'+familyID+'.fcl'

        defname                      = 'dig.mu2e.CeEndpointMix2BBUntriggered.MDC2020r_perfect_v1_0.art' # dataset definition name
        job.fInputDataset            = Dataset(defname,'cele0b2s45r00','local')    # 
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
# s5:reco_s55r02 : reco with FlagBkgHits+TZFinder+PhiClusterFinder
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        job                          = s.new_job('reco_s55r02');

        job.fRunNumber               = 1000;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_reco_02_'+familyID+'.fcl'

        defname                      = 'dig.mu2e.CeEndpointMix2BBUntriggered.MDC2020r_perfect_v1_0.art' # dataset definition name
        job.fInputDataset            = Dataset(defname,'cele0b2s45r00','local')    # 
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
# s5:reco_s55r03 : reco with DeltaFinder+TZFinder+PhiClusterFinder
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        job                          = s.new_job('reco_s55r03');

        job.fRunNumber               = 1000;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_reco_03_'+familyID+'.fcl'

        defname                      = 'dig.mu2e.CeEndpointMix2BBSignal.MDC2020r_perfect_v1_0.art' # dataset definition name
        job.fInputDataset            = Dataset(defname,'cele0b2s45r00','local')    # 
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
# s5:stn_s55r01 : default reco
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        job                          = s.new_job('stn_s55r01');

        job.fRunNumber               = 1000;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_stn_'+familyID+'.fcl'

        idsid                        = 'cele0b2s55r01'
        defname                      = 'mcs.mu2e.'+idsid+'.mdc2020.art'          # dataset definition name
        job.fInputDataset            = Dataset(defname,idsid,'local')            # 
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
# s5:stn_s55r02 : (TZClusterFinder+PhiClusterFinder)
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        job                          = s.new_job('stn_s55r02');

        job.fRunNumber               = 1000;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_stn_'+familyID+'.fcl'

        idsid                        = 'cele0b2s55r02'
        defname                      = 'mcs.mu2e.'+idsid+'.mdc2020.art'          # dataset definition name
        job.fInputDataset            = Dataset(defname,idsid,'local')            # 
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
# s5:stn_s55r03 : DeltaFinder+TZFinder+PhiClusterFinder
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        job                          = s.new_job('stn_s55r03');

        job.fRunNumber               = 1000;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_stn_'+familyID+'.fcl'

        idsid                        = 'cele0b2s55r03'
        defname                      = 'mcs.mu2e.'+idsid+'.mdc2020.art'          # dataset definition name
        job.fInputDataset            = Dataset(defname,idsid,'local')            # 
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
# s5:stn_s55r01 : default reco
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        job                          = s.new_job('stn_s55r01');

        job.fRunNumber               = 1000;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_stn_'+familyID+'.fcl'

        idsid                        = 'cele0b2s55r01'
        defname                      = 'mcs.mu2e.'+idsid+'.mdc2020.art'          # dataset definition name
        job.fInputDataset            = Dataset(defname,idsid,'local')            # 
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
# s5:stn_s55r02 : (TZClusterFinder+PhiClusterFinder)
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        job                          = s.new_job('stn_s55r02');

        job.fRunNumber               = 1000;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_stn_'+familyID+'.fcl'

        idsid                        = 'cele0b2s55r02'
        defname                      = 'mcs.mu2e.'+idsid+'.mdc2020.art'          # dataset definition name
        job.fInputDataset            = Dataset(defname,idsid,'local')            # 
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
# s5:stn_s55r03 : DeltaFinder+TZFinder+PhiClusterFinder
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        job                          = s.new_job('stn_s55r03');

        job.fRunNumber               = 1000;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_stn_'+familyID+'.fcl'

        idsid                        = 'cele0b2s55r03'
        defname                      = 'mcs.mu2e.'+idsid+'.mdc2020.art'          # dataset definition name
        job.fInputDataset            = Dataset(defname,idsid,'local')            # 
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
