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
        familyID                     = 'cele02'

        self.fProjectName            = project;
        self.fFamilyID               = familyID;
        self.fStage                  = {}
#------------------------------------------------------------------------------
# init first stage. a Stage can have one or several jobs associated with it
#------------------------------------------------------------------------------        
        s                            = self.new_stage('s5');
#------------------------------------------------------------------------------
# s5:reco_01 : default reco
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        job                          = s.new_job('reco_01');

        job.fRunNumber               = 1000;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_reco_01_'+familyID+'.fcl'
        
        idsid                        = familyID+'s41b2';
        defname                      = 'dig.mu2e.CeEndpointMix2BBUntriggered.MDC2020r_perfect_v1_0.art' # dataset definition name
        job.fInputDataset            = Dataset(defname,idsid,'local')            # 
        job.fNInputFiles             = -1                                        # placeholder, 
        job.fMaxInputFilesPerSegment =  100                                      # 12 events/input file
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ familyID+'s51b2'                ]
        job.fOutputFnPattern         = [ 'nts.mu2e.'+project+'.'+job.fOutputDsID[0] ]
        job.fOutputFormat            = [ 'art'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:reco_02 : reco with FlagBkgHits+TZFinder+PhiClusterFinder
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        job                          = s.new_job('reco_02');

        job.fRunNumber               = 1000;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_reco_02_'+familyID+'.fcl'

        idsid                        = familyID+'s41b2';
        defname                      = 'dig.mu2e.CeEndpointMix2BBUntriggered.MDC2020r_perfect_v1_0.art' # dataset definition name
        job.fInputDataset            = Dataset(defname,idsid,'local')            # 
        job.fNInputFiles             = -1                                        # placeholder, 
        job.fMaxInputFilesPerSegment =  100                                      # 12 events/input file
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ familyID+'s52b2'                ]
        job.fOutputFnPattern         = [ 'nts.mu2e.'+project+'.'+job.fOutputDsID[0] ]
        job.fOutputFormat            = [ 'art'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:reco_03 : reco with DeltaFinder+TZFinder+PhiClusterFinder
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        job                          = s.new_job('reco_03');

        job.fRunNumber               = 1000;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_reco_03_'+familyID+'.fcl'

        idsid                        = familyID+'s41b2';
        defname                      = 'dig.mu2e.CeEndpointMix2BBUntriggered.MDC2020r_perfect_v1_0.art' # dataset definition name
        job.fInputDataset            = Dataset(defname,idsid,'local')            # 
        job.fNInputFiles             = -1                                        # placeholder, 
        job.fMaxInputFilesPerSegment =  100                                      # 12 events/input file
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ familyID+'s53b2'                ]
        job.fOutputFnPattern         = [ 'nts.mu2e.'+project+'.'+job.fOutputDsID[0] ]
        job.fOutputFormat            = [ 'art'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:stn_01 : default reco
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        job                          = s.new_job('stn_01');

        job.fRunNumber               = 1000;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_stn_'+familyID+'.fcl'

        idsid                        = familyID+'s51b2';                         # input dsid
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
        job.fOutputDsID              = [ idsid                           ]       # ntupling doesn't change the dsid
        job.fOutputFnPattern         = [ 'nts.mu2e.'+project+'.'+job.fOutputDsID[0] ]
        job.fOutputFormat            = [ 'stn'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:stn_01 : default reco
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        job                          = s.new_job('stn_02');

        job.fRunNumber               = 1000;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_stn_'+familyID+'.fcl'

        idsid                        = familyID+'s52b2';                         # input dsid
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
        job.fOutputFnPattern         = [ 'nts.mu2e.'+project+'.'+job.fOutputDsID[0] ]
        job.fOutputFormat            = [ 'stn'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# s5:stn_01 : ntuple output of modified reco
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        job                          = s.new_job('stn_03');

        job.fRunNumber               = 1000;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_stn_'+familyID+'.fcl'
        
        idsid                        = familyID+'s53b2';                         # input dsid
        defname                      = 'mcs.mu2e.'+idsid+'.mdc2020.art  '        # dataset definition name
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
        job.fOutputFnPattern         = [ 'nts.mu2e.'+project+'.'+job.fOutputDsID[0] ]
        job.fOutputFormat            = [ 'stn'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# end
#------------------------------------------------------------------------------
