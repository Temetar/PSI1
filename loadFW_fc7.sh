
CMSIT_XML=${PH2ACF_ANALYSIS_DIR}/configs/init/CMSIT.xml

if [ ! -f ${CMSIT_XML} ]; then
  printf "%s\n" "target xml configuration file not found: ${CMSIT_XML}"
  exit 1
fi

echo "Loading firmware"

#fpgaconfig -c ${CMSIT_XML} -i ph2ITuDTC_v4p1_SC_KS-KS_x1G28
fpgaconfig -c ${CMSIT_XML} -i IT-uDTC_v4p2-KSU-4x_elec_x1G28
