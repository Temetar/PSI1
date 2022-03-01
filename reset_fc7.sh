#!/bin/bash -e

CMSIT_XML=${PH2ACF_ANALYSIS_DIR}/configs/init/CMSIT.xml

if [ ! -f ${CMSIT_XML} ]; then
  printf "%s\n" "target xml configuration file not found: ${CMSIT_XML}"
  exit 1
fi

echo "Resetting FC7"
CMSITminiDAQ -f ${CMSIT_XML} -r

unset CMSIT_XML
