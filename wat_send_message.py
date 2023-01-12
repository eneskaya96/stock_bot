from time import sleep

import pywhatkit

tel_aslı = ""
tel_enes = "-"
pywhatkit.sendwhatmsg_instantly(
    phone_no=tel_enes,
    message="Artık otomatik message atabiliyorum",
    wait_time=17,
    tab_close=True
)

