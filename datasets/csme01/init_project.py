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
        familyID                     = 'cosme01'

        self.fProjectName            = project;
        self.fFamilyID               = familyID;
        self.fStage                  = {}
#------------------------------------------------------------------------------
# init first stage. a Stage can have one or several jobs associated with it
#------------------------------------------------------------------------------        
        s                            = self.new_stage('s1');
#------------------------------------------------------------------------------
# s1:vst_stn
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        job                          = s.new_job('stn');

        job.fRunNumber               = 1000;
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_stn_'+familyID+'.fcl'

        defname                      = 'dig.mu2e.CosmicCORSICAExtractedNoFieldTrk.MDC2020r_perfect_v1_0.art' # dattaset definition name
        job.fInputDataset            = Dataset(defname,'csme01','local')         # 
        job.fNInputFiles             = -1                                        # placeholder, 
        job.fMaxInputFilesPerSegment =  500                                      # process each run separately
        job.fNEventsPerSegment       =  1000000                                  # placeholder
        job.fResample                = 'no'                                      # yes/no
        job.fMaxMemory               = '2000MB'
        job.fRequestedTime           = '12h'
        job.fIfdh                    = 'xrootd'                                  # ifdh/xrootd

        job.fOutputStream            = [ 'defaultOutput'                 ]
        job.fOutputDsID              = [ job.input_dataset().id()        ]
        job.fOutputFnPattern         = [ 'nts.mu2e.'+project+'.'+job.fOutputDsID[0] ]
        job.fOutputFormat            = [ 'stn'                           ]

        desc                         = project+'.'+job.input_dataset().id()+'.'+s.name()+'_'+job.name()
        job.fDescription             = desc;
#------------------------------------------------------------------------------
# end
#------------------------------------------------------------------------------
