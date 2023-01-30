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
        familyID                     = 'mnbs0b1'

        self.fProjectName            = project;
        self.fFamilyID               = familyID;
        self.fStage                  = {}
        self.fDataset                = {};
#------------------------------------------------------------------------------
# init datasets
#------------------------------------------------------------------------------        
        self.fDataset['mnbs0b1s41r00'] = Dataset('dig.mu2e.NoPrimaryMix1BBUntriggered.MDC2020r_best_v1_0.art','mnbs0b1s41r00','local')    # 

        self.fDataset['mnbs0b1s51r01'] = Dataset('mcs.mu2e.mnbs0b1s51r01.mdc2020.art'                        ,'mnbs0b1s51r01','local')    # 
        self.fDataset['mnbs0b1s51r08'] = Dataset('mcs.mu2e.mnbs0b1s51r08.mdc2020.art'                        ,'mnbs0b1s51r08','local')    # 
#------------------------------------------------------------------------------
# init first stage. a Stage can have one or several jobs associated with it
#------------------------------------------------------------------------------        
        s                            = self.new_stage('s5');
#------------------------------------------------------------------------------
# s5:mnbs0b1s41r00:reco_01 : default reco
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        idsid                        = 'mnbs0b1s41r00';
        job                          = s.new_job('reco_01',idsid);

        job.fRunNumber               = 1201;
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
# s5:mnbs0b1s41r00:reco_08 : reco with DeltaFinder+TZFinder+PhiClusterFinder, 
#                            - no Ehit<3.5keV cut
#                            - up to 4 SH/CH
#                            - scale CH errors along the wire
#------------------------------------------------------------------------------        
        idsid                        = 'mnbs0b1s41r00';
        job                          = s.new_job('reco_08', idsid);
        job.fBaseFcl                 = project+'/datasets/'+familyID+'/'+s.name()+'_reco_08_'+familyID+'.fcl'
        job.fRecoVersion             = '08'

        job.fRunNumber               = 1201;                                     # not needed, defined by the input dataset
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
# s5:mnbs0b1s51r01:stn : default reco
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        idsid                        = 'mnbs0b1s51r01'
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
# s5:mnbs0b1s51r08:stn : DeltaFinder+TZFinder+PhiClusterFinder
# for a job with an input dataset, 'job.fNInputFiles' is defined by the input dataset
#------------------------------------------------------------------------------        
        idsid                        = 'mnbs0b1s51r08';
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
# end
#------------------------------------------------------------------------------
