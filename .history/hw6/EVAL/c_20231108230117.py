
import re
import matplotlib.pyplot as plt
import numpy as np

run0 = """[#CLIENT#] R[0]: Sent: 86390.208108543 Recv: 86390.226206209 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 0    Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[1]: Sent: 86390.409510835 Recv: 86390.497656001 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[2]: Sent: 86390.562467668 Recv: 86390.654781043 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[3]: Sent: 86390.584509876 Recv: 86390.746840543 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[4]: Sent: 86390.617087001 Recv: 86390.764828251 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No HASH: 2326e8a964742d53375a7edba55f44a4
[#CLIENT#] R[5]: Sent: 86390.716290835 Recv: 86390.734461210 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 1    Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[6]: Sent: 86391.038448418 Recv: 86391.095015502 Opcode: IMG_BLUR        OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[7]: Sent: 86391.164961752 Recv: 86391.198162668 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[8]: Sent: 86391.199810085 Recv: 86391.306552002 Opcode: IMG_BLUR        OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[9]: Sent: 86391.362900585 Recv: 86391.380808877 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[10]: Sent: 86391.380844002 Recv: 86391.467758877 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[11]: Sent: 86391.405500752 Recv: 86391.632224002 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[12]: Sent: 86391.500361668 Recv: 86391.674062085 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[13]: Sent: 86391.574705835 Recv: 86391.695124293 Opcode: IMG_BLUR        OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[14]: Sent: 86391.609357585 Recv: 86391.858641544 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[15]: Sent: 86391.756338585 Recv: 86392.030286419 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[16]: Sent: 86391.789691502 Recv: 86392.086523044 Opcode: IMG_BLUR        OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[17]: Sent: 86392.041076377 Recv: 86392.170364127 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[18]: Sent: 86392.115762835 Recv: 86392.212536252 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[19]: Sent: 86392.224637085 Recv: 86392.309097502 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[20]: Sent: 86392.231304960 Recv: 86392.365389085 Opcode: IMG_BLUR        OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[21]: Sent: 86392.237851877 Recv: 86392.528642294 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[22]: Sent: 86392.470385461 Recv: 86392.648210961 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[23]: Sent: 86392.548036044 Recv: 86392.648191669 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 3    Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[24]: Sent: 86392.720061877 Recv: 86392.774271544 Opcode: IMG_BLUR        OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[25]: Sent: 86392.724140419 Recv: 86392.880164002 Opcode: IMG_BLUR        OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[26]: Sent: 86392.991288919 Recv: 86393.097092586 Opcode: IMG_BLUR        OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[27]: Sent: 86393.125474586 Recv: 86393.217027669 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[28]: Sent: 86393.241956294 Recv: 86393.329019378 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[29]: Sent: 86393.454106544 Recv: 86393.559890586 Opcode: IMG_BLUR        OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[30]: Sent: 86393.480150419 Recv: 86393.698579794 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[31]: Sent: 86393.596240878 Recv: 86393.698575378 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[32]: Sent: 86393.805675920 Recv: 86393.889989336 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[33]: Sent: 86394.063424295 Recv: 86394.080974170 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 5    Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[34]: Sent: 86394.196240503 Recv: 86394.686284920 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[35]: Sent: 86394.220585503 Recv: 86394.770185503 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[36]: Sent: 86394.236581128 Recv: 86394.861740962 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[37]: Sent: 86394.293166795 Recv: 86394.870107087 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[38]: Sent: 86394.447388753 Recv: 86394.887828503 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No HASH: c9e9acb37a12747a13739fb3fe21a308
[#CLIENT#] R[39]: Sent: 86394.473080586 Recv: 86394.983296128 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No HASH: 55f606719c1033a44269b8e4136e8211
[#CLIENT#] R[40]: Sent: 86394.554411878 Recv: 86395.354090045 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[41]: Sent: 86394.791758045 Recv: 86395.818896879 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[42]: Sent: 86394.860215212 Recv: 86395.907121046 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[43]: Sent: 86395.133647087 Recv: 86396.371236921 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[44]: Sent: 86395.272283129 Recv: 86396.834261921 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[45]: Sent: 86395.298769629 Recv: 86395.317390004 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 6    Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[46]: Sent: 86395.333667879 Recv: 86396.918325963 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[47]: Sent: 86395.491475629 Recv: 86397.407123421 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[48]: Sent: 86395.499265462 Recv: 86397.898143546 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[49]: Sent: 86395.573034295 Recv: 86398.384964172 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[50]: Sent: 86395.732930129 Recv: 86398.556907172 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[51]: Sent: 86396.075375879 Recv: 86399.022045339 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[52]: Sent: 86396.085280171 Recv: 86399.040378505 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No HASH: 88580d74c84ac71f83f497a49312521b
[#CLIENT#] R[53]: Sent: 86396.093466837 Recv: 86396.196641796 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 7    Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[54]: Sent: 86396.258538337 Recv: 86399.321799505 Opcode: IMG_BLUR        OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[55]: Sent: 86396.399489629 Recv: 86399.410128381 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[56]: Sent: 86397.595051796 Recv: 86399.913954256 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[57]: Sent: 86397.608537713 Recv: 86400.361195089 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[58]: Sent: 86397.813021338 Recv: 86397.831563880 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 8    Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[59]: Sent: 86398.088103088 Recv: 86400.398905422 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[60]: Sent: 86398.106034880 Recv: 86400.474312547 Opcode: IMG_BLUR        OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[61]: Sent: 86398.277397672 Recv: 86400.492488881 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No HASH: 88580d74c84ac71f83f497a49312521b
[#CLIENT#] R[62]: Sent: 86398.364076380 Recv: 86400.940730339 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[63]: Sent: 86398.374608422 Recv: 86400.996920173 Opcode: IMG_BLUR        OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[64]: Sent: 86398.410924088 Recv: 86401.037148964 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[65]: Sent: 86398.621056713 Recv: 86401.500825715 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[66]: Sent: 86398.624742713 Recv: 86401.588139715 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[67]: Sent: 86398.884365672 Recv: 86401.690231756 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No HASH: 3b45556ca43a453c23cddf80da7af879
[#CLIENT#] R[68]: Sent: 86399.272867589 Recv: 86401.725351131 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No HASH: 732a5bde390f582e4cfff5c80094733c
[#CLIENT#] R[69]: Sent: 86399.684012756 Recv: 86401.894872715 Opcode: IMG_BLUR        OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[70]: Sent: 86399.702019464 Recv: 86399.754452631 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 9    Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[71]: Sent: 86399.762464881 Recv: 86402.359773798 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[72]: Sent: 86399.861814256 Recv: 86399.913919006 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 10   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[73]: Sent: 86399.951954631 Recv: 86402.401045215 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[74]: Sent: 86399.959710297 Recv: 86402.629491007 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[75]: Sent: 86400.065048131 Recv: 86402.664508715 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No HASH: 732a5bde390f582e4cfff5c80094733c
[#CLIENT#] R[76]: Sent: 86400.097941464 Recv: 86402.664524215 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[77]: Sent: 86400.110007672 Recv: 86402.885897549 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[78]: Sent: 86400.398863131 Recv: 86403.348604424 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[79]: Sent: 86400.587120172 Recv: 86403.366817299 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No HASH: 5270006985a5f40de12fea9382d69f27
[#CLIENT#] R[80]: Sent: 86400.629495422 Recv: 86403.366826340 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[81]: Sent: 86400.656174089 Recv: 86403.440383632 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[82]: Sent: 86400.721971006 Recv: 86403.903650716 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[83]: Sent: 86400.742230423 Recv: 86404.368322799 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[84]: Sent: 86400.795714464 Recv: 86404.413298258 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[85]: Sent: 86400.897261256 Recv: 86400.914830589 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 11   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[86]: Sent: 86401.008779423 Recv: 86404.469642716 Opcode: IMG_BLUR        OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[87]: Sent: 86401.048640964 Recv: 86404.556429341 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[88]: Sent: 86401.302449631 Recv: 86404.662209966 Opcode: IMG_BLUR        OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[89]: Sent: 86401.332243006 Recv: 86404.718412799 Opcode: IMG_BLUR        OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[90]: Sent: 86401.362459714 Recv: 86404.774503341 Opcode: IMG_BLUR        OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[91]: Sent: 86401.372337673 Recv: 86404.821339424 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[92]: Sent: 86401.458340465 Recv: 86404.909792758 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[93]: Sent: 86401.492460715 Recv: 86405.071547300 Opcode: IMG_BLUR        OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[94]: Sent: 86401.532500548 Recv: 86405.235238633 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[95]: Sent: 86401.532891590 Recv: 86405.536494258 Opcode: IMG_BLUR        OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[96]: Sent: 86401.553763881 Recv: 86406.001120508 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[97]: Sent: 86401.805053923 Recv: 86406.018937050 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No HASH: 70cf2014ae70367eb9f0b3a744d9fc82
[#CLIENT#] R[98]: Sent: 86401.818018965 Recv: 86406.465804884 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[99]: Sent: 86401.966903548 Recv: 86406.567746675 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[100]: Sent: 86402.165023548 Recv: 86406.643674092 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[101]: Sent: 86402.244496423 Recv: 86406.699866217 Opcode: IMG_BLUR        OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[102]: Sent: 86402.484965215 Recv: 86406.786918009 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[103]: Sent: 86402.570889090 Recv: 86402.605597340 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 12   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[104]: Sent: 86402.805528007 Recv: 86406.793692467 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[105]: Sent: 86402.994617424 Recv: 86406.877562884 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[106]: Sent: 86403.014574424 Recv: 86406.919748675 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[107]: Sent: 86403.029585757 Recv: 86407.005997509 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[108]: Sent: 86403.211731799 Recv: 86407.256067717 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[109]: Sent: 86403.236878424 Recv: 86407.357401509 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No HASH: 57886e6e07fbc6d6f889d8409e86a1dd
[#CLIENT#] R[110]: Sent: 86403.251789215 Recv: 86407.357424301 Opcode: IMG_BLUR        OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[111]: Sent: 86403.520520840 Recv: 86407.805167426 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[112]: Sent: 86403.701891216 Recv: 86407.845116218 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[113]: Sent: 86403.742724382 Recv: 86403.760391091 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 13   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[114]: Sent: 86403.854289257 Recv: 86408.144300426 Opcode: IMG_BLUR        OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[115]: Sent: 86403.861897466 Recv: 86408.305941426 Opcode: IMG_BLUR        OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[116]: Sent: 86403.907109507 Recv: 86408.770518885 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[117]: Sent: 86403.916696757 Recv: 86408.859147135 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[118]: Sent: 86404.004331257 Recv: 86409.020786176 Opcode: IMG_BLUR        OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[119]: Sent: 86404.147844799 Recv: 86409.115575468 Opcode: IMG_BLUR        OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[120]: Sent: 86404.362502216 Recv: 86409.183612968 Opcode: IMG_BLUR        OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[121]: Sent: 86404.385857174 Recv: 86409.646811218 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[122]: Sent: 86404.563075841 Recv: 86410.110607844 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[123]: Sent: 86404.602593258 Recv: 86410.211422260 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No HASH: abaacf2afea051f6c7f8d2df54564402
[#CLIENT#] R[124]: Sent: 86405.021582050 Recv: 86410.211458969 Opcode: IMG_BLUR        OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[125]: Sent: 86405.036275300 Recv: 86410.211468135 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[126]: Sent: 86405.189247508 Recv: 86410.283018802 Opcode: IMG_BLUR        OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[127]: Sent: 86405.201472300 Recv: 86410.545036552 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[128]: Sent: 86405.206534300 Recv: 86410.809385261 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[129]: Sent: 86405.329644550 Recv: 86411.059452469 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[130]: Sent: 86405.530150383 Recv: 86411.143374636 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[131]: Sent: 86405.578496675 Recv: 86411.162144094 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No HASH: 60a1e239cb4ca19a0edb461e80133d15
[#CLIENT#] R[132]: Sent: 86405.744154842 Recv: 86411.227633636 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[133]: Sent: 86405.749696758 Recv: 86405.802603383 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 14   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[134]: Sent: 86405.920370258 Recv: 86411.269407761 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[135]: Sent: 86406.018945675 Recv: 86411.276484678 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[136]: Sent: 86406.109379383 Recv: 86411.367572886 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[137]: Sent: 86406.329025967 Recv: 86411.374343136 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[138]: Sent: 86406.423175759 Recv: 86411.637936011 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[139]: Sent: 86406.513904134 Recv: 86406.567720300 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 15   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[140]: Sent: 86406.574996592 Recv: 86411.887499094 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[141]: Sent: 86406.593631675 Recv: 86412.137830928 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[142]: Sent: 86406.768985342 Recv: 86412.191093678 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No HASH: 07713d772d0b67e8304db40f99efce2f
[#CLIENT#] R[143]: Sent: 86406.979648634 Recv: 86412.310757470 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[144]: Sent: 86407.087335801 Recv: 86412.311997636 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[145]: Sent: 86407.238034592 Recv: 86412.800542637 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[146]: Sent: 86407.357433426 Recv: 86412.855267095 Opcode: IMG_BLUR        OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[147]: Sent: 86407.452265967 Recv: 86412.874044303 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No HASH: ac3c20fe392ffe1675d760e0acc0325d
[#CLIENT#] R[148]: Sent: 86407.604746092 Recv: 86412.874054803 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[149]: Sent: 86407.656075342 Recv: 86413.026186012 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[150]: Sent: 86407.682380884 Recv: 86413.112895970 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[151]: Sent: 86407.699218176 Recv: 86413.136428012 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[152]: Sent: 86407.747093676 Recv: 86413.292781845 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[153]: Sent: 86407.880868134 Recv: 86413.817485012 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[154]: Sent: 86407.961299884 Recv: 86413.946151220 Opcode: IMG_BLUR        OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[155]: Sent: 86408.127309968 Recv: 86414.432727387 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[156]: Sent: 86408.231178218 Recv: 86414.588815762 Opcode: IMG_BLUR        OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[157]: Sent: 86408.416970759 Recv: 86414.594625637 Opcode: IMG_BLUR        OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[158]: Sent: 86408.490144218 Recv: 86415.086106013 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[159]: Sent: 86408.617079385 Recv: 86415.348702054 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[160]: Sent: 86408.633702635 Recv: 86415.815220263 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[161]: Sent: 86408.749483926 Recv: 86415.899061096 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[162]: Sent: 86408.870024301 Recv: 86416.198475430 Opcode: IMG_BLUR        OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[163]: Sent: 86408.870668885 Recv: 86408.923333385 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 16   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[164]: Sent: 86409.029876801 Recv: 86416.448519430 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[165]: Sent: 86409.071679635 Recv: 86409.090016051 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 17   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[166]: Sent: 86409.195951968 Recv: 86416.620830180 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[167]: Sent: 86409.216612260 Recv: 86416.784576972 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[168]: Sent: 86409.393228677 Recv: 86416.868533597 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[169]: Sent: 86409.414475593 Recv: 86416.887191055 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No HASH: 2b87ba29a04361673e6c89b35bde43d4
[#CLIENT#] R[170]: Sent: 86409.617724218 Recv: 86417.357061555 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[171]: Sent: 86409.887326302 Recv: 86417.443894097 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[172]: Sent: 86409.967542760 Recv: 86417.528061014 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[173]: Sent: 86410.048033010 Recv: 86417.548513556 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[174]: Sent: 86410.216358344 Recv: 86417.650010222 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No HASH: a70bdc3cdf2b54142b30883214c9c99c
[#CLIENT#] R[175]: Sent: 86410.752427927 Recv: 86410.770531011 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 18   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[176]: Sent: 86410.977894302 Recv: 86417.650018972 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[177]: Sent: 86411.120400969 Recv: 86417.694864889 Opcode: IMG_BLUR        OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[178]: Sent: 86411.162156386 Recv: 86417.800754181 Opcode: IMG_BLUR        OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[179]: Sent: 86411.180460261 Recv: 86417.840819056 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[180]: Sent: 86411.386873136 Recv: 86417.859012264 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No HASH: 18743a90a1c8b73697150fda5f9497ce
[#CLIENT#] R[181]: Sent: 86411.481603761 Recv: 86417.959008681 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No HASH: 13498c3ae65af1245b92c44175fe9e20
[#CLIENT#] R[182]: Sent: 86411.558985469 Recv: 86417.959017097 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[183]: Sent: 86411.562383928 Recv: 86411.580082386 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 19   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[184]: Sent: 86411.758840803 Recv: 86418.205475806 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[185]: Sent: 86411.826182469 Recv: 86418.224497973 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No HASH: fe98aaa171a54ea15946e81aba274db1
[#CLIENT#] R[186]: Sent: 86411.994621886 Recv: 86418.243121973 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No HASH: 18743a90a1c8b73697150fda5f9497ce
[#CLIENT#] R[187]: Sent: 86412.054856720 Recv: 86418.456185764 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[188]: Sent: 86412.083268428 Recv: 86418.512529848 Opcode: IMG_BLUR        OW: 1 ClientImgID: 17   ServerImgID: 17   Rejected: No
[#CLIENT#] R[189]: Sent: 86412.209765136 Recv: 86412.310752886 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 20   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[190]: Sent: 86412.398165803 Recv: 86412.500759386 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 21   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[191]: Sent: 86413.033967428 Recv: 86418.975832890 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[192]: Sent: 86413.136403303 Recv: 86419.139434431 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[193]: Sent: 86413.161266303 Recv: 86419.223160848 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[194]: Sent: 86413.295241512 Recv: 86419.242041390 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[195]: Sent: 86413.485416387 Recv: 86419.260530348 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 17   ServerImgID: 17   Rejected: No HASH: 1d58d784c91555c8541eca0755b4bb5a
[#CLIENT#] R[196]: Sent: 86413.714830512 Recv: 86413.817476220 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 22   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[197]: Sent: 86413.894380012 Recv: 86419.278520223 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No HASH: d0786a5de39ca03211ddc5c71ef9d5da
[#CLIENT#] R[198]: Sent: 86414.193708596 Recv: 86419.315687848 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[199]: Sent: 86414.535765721 Recv: 86414.588822429 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 23   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[200]: Sent: 86414.740365721 Recv: 86419.399377848 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[201]: Sent: 86414.770228388 Recv: 86419.418006598 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 17   ServerImgID: 17   Rejected: No HASH: 1d58d784c91555c8541eca0755b4bb5a
[#CLIENT#] R[202]: Sent: 86414.810577763 Recv: 86419.649789057 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[203]: Sent: 86414.891475763 Recv: 86419.704566515 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No HASH: dbc5cfa2ed2144a04653f8fe75f6fb2e
[#CLIENT#] R[204]: Sent: 86414.956543763 Recv: 86419.758285640 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No HASH: 83af9aa159e73eca99768998d53faa35
[#CLIENT#] R[205]: Sent: 86415.204948138 Recv: 86419.758293348 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 17   ServerImgID: 17   Rejected: No
[#CLIENT#] R[206]: Sent: 86415.405650513 Recv: 86419.776180473 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No HASH: d0786a5de39ca03211ddc5c71ef9d5da
[#CLIENT#] R[207]: Sent: 86415.427908180 Recv: 86419.794051682 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No HASH: 9501a7ff4534a1193b3fc6fa69efaad3
[#CLIENT#] R[208]: Sent: 86415.540817138 Recv: 86419.794063348 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[209]: Sent: 86415.623158971 Recv: 86415.726203680 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 24   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[210]: Sent: 86415.728120388 Recv: 86419.835639890 Opcode: IMG_BLUR        OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[211]: Sent: 86415.985521096 Recv: 86419.996712473 Opcode: IMG_BLUR        OW: 1 ClientImgID: 16   ServerImgID: 16   Rejected: No
[#CLIENT#] R[212]: Sent: 86416.203812930 Recv: 86420.260124807 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[213]: Sent: 86416.263288597 Recv: 86420.344296932 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[214]: Sent: 86416.365226180 Recv: 86420.808409724 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 21   ServerImgID: 21   Rejected: No
[#CLIENT#] R[215]: Sent: 86416.399927055 Recv: 86420.979577932 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[216]: Sent: 86416.629656930 Recv: 86420.999662057 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[217]: Sent: 86416.661580722 Recv: 86421.083936557 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[218]: Sent: 86416.862364305 Recv: 86421.104554849 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[219]: Sent: 86417.120846180 Recv: 86421.591705557 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[220]: Sent: 86417.139197139 Recv: 86421.598828016 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[221]: Sent: 86417.158605972 Recv: 86421.605745266 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No
[#CLIENT#] R[222]: Sent: 86417.452230305 Recv: 86421.905340474 Opcode: IMG_BLUR        OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[223]: Sent: 86417.465058555 Recv: 86421.994666933 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[224]: Sent: 86417.711879847 Recv: 86422.013428808 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No HASH: 56dce5d5ef77a4d1b70bb5f0ede39c26
[#CLIENT#] R[225]: Sent: 86417.719247306 Recv: 86422.067341433 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No HASH: 9559d5665fccb0cf0ca4a5cb2425a4e9
[#CLIENT#] R[226]: Sent: 86417.776657681 Recv: 86422.067350183 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No
[#CLIENT#] R[227]: Sent: 86418.020186639 Recv: 86422.466022058 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 22   ServerImgID: 22   Rejected: No
[#CLIENT#] R[228]: Sent: 86418.023763847 Recv: 86422.474150891 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[229]: Sent: 86418.163787431 Recv: 86422.482229016 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[230]: Sent: 86418.167453597 Recv: 86422.972138766 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[231]: Sent: 86418.275897056 Recv: 86422.992479225 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[232]: Sent: 86418.496080098 Recv: 86423.164533225 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[233]: Sent: 86418.501282181 Recv: 86423.342439100 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[234]: Sent: 86418.621319806 Recv: 86423.714649017 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[235]: Sent: 86418.658907681 Recv: 86423.814712392 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 21   ServerImgID: 21   Rejected: No HASH: 22286fe7eb8d021fb7fb11f7614799bf
[#CLIENT#] R[236]: Sent: 86418.824681848 Recv: 86423.814720559 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 16   ServerImgID: 16   Rejected: No
[#CLIENT#] R[237]: Sent: 86418.830218889 Recv: 86418.882734223 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 25   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[238]: Sent: 86418.910732764 Recv: 86423.814766184 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[239]: Sent: 86418.916760723 Recv: 86423.862044559 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[240]: Sent: 86418.922552556 Recv: 86423.921851684 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[241]: Sent: 86418.952281931 Recv: 86418.969884556 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 26   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[242]: Sent: 86419.057666431 Recv: 86424.083580309 Opcode: IMG_BLUR        OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[243]: Sent: 86419.318171265 Recv: 86424.172650434 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[244]: Sent: 86419.448922723 Recv: 86424.215347600 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 22   ServerImgID: 22   Rejected: No
[#CLIENT#] R[245]: Sent: 86419.549364765 Recv: 86424.703715601 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[246]: Sent: 86419.817539223 Recv: 86424.790887559 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[247]: Sent: 86419.891545140 Recv: 86419.994113265 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 27   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[248]: Sent: 86420.108044640 Recv: 86424.882476559 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No
[#CLIENT#] R[249]: Sent: 86420.139420182 Recv: 86425.182368017 Opcode: IMG_BLUR        OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[250]: Sent: 86420.163590432 Recv: 86425.645553143 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[251]: Sent: 86420.278693598 Recv: 86426.109352810 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 22   ServerImgID: 22   Rejected: No
[#CLIENT#] R[252]: Sent: 86420.470094349 Recv: 86426.201619435 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No
[#CLIENT#] R[253]: Sent: 86420.580391015 Recv: 86426.285736476 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[254]: Sent: 86420.609228349 Recv: 86426.304442685 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No HASH: 56dce5d5ef77a4d1b70bb5f0ede39c26
[#CLIENT#] R[255]: Sent: 86420.681506932 Recv: 86426.548713810 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[256]: Sent: 86420.757273057 Recv: 86426.640231143 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[257]: Sent: 86420.890782557 Recv: 86426.659085893 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No HASH: 98b9ed3ea6eae02e2969162cccbd71f7
[#CLIENT#] R[258]: Sent: 86420.895315765 Recv: 86427.132255185 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 22   ServerImgID: 22   Rejected: No
[#CLIENT#] R[259]: Sent: 86420.962147015 Recv: 86427.294069435 Opcode: IMG_BLUR        OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[260]: Sent: 86421.133784641 Recv: 86427.333866185 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[261]: Sent: 86421.142056474 Recv: 86427.595807269 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 16   ServerImgID: 16   Rejected: No
[#CLIENT#] R[262]: Sent: 86421.398994682 Recv: 86427.679959894 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[263]: Sent: 86421.427121099 Recv: 86427.979237644 Opcode: IMG_BLUR        OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[264]: Sent: 86421.436896099 Recv: 86421.471237557 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 28   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[265]: Sent: 86421.489418682 Recv: 86428.033660102 Opcode: IMG_BLUR        OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[266]: Sent: 86421.639760641 Recv: 86428.139674269 Opcode: IMG_BLUR        OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[267]: Sent: 86421.773177516 Recv: 86428.158367477 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No HASH: 6eea4bd5c0b7ead532c334eea7ccd250
[#CLIENT#] R[268]: Sent: 86421.783356766 Recv: 86428.226759644 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[269]: Sent: 86421.794089308 Recv: 86428.282923227 Opcode: IMG_BLUR        OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[270]: Sent: 86421.960074183 Recv: 86428.369932644 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No
[#CLIENT#] R[271]: Sent: 86421.992577224 Recv: 86428.476146061 Opcode: IMG_BLUR        OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[272]: Sent: 86422.135690849 Recv: 86422.239695599 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 29   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[273]: Sent: 86422.426328475 Recv: 86428.515608269 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[274]: Sent: 86422.487436725 Recv: 86422.540361600 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 30   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[275]: Sent: 86422.579474891 Recv: 86428.765942686 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[276]: Sent: 86422.588014683 Recv: 86429.119092519 Opcode: IMG_BLUR        OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[277]: Sent: 86422.695888183 Recv: 86429.119096394 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 29   ServerImgID: 29   Rejected: No
[#CLIENT#] R[278]: Sent: 86422.783252516 Recv: 86429.568050103 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 29   ServerImgID: 29   Rejected: No
[#CLIENT#] R[279]: Sent: 86422.858561308 Recv: 86422.961015975 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 31   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[280]: Sent: 86423.107224266 Recv: 86429.743075353 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[281]: Sent: 86423.179659350 Recv: 86429.992929436 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[282]: Sent: 86423.239968475 Recv: 86423.342433725 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 32   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[283]: Sent: 86423.399320308 Recv: 86430.048016811 Opcode: IMG_BLUR        OW: 1 ClientImgID: 26   ServerImgID: 26   Rejected: No
[#CLIENT#] R[284]: Sent: 86423.412859642 Recv: 86430.132149353 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[285]: Sent: 86423.564415350 Recv: 86430.597313519 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 22   ServerImgID: 22   Rejected: No
[#CLIENT#] R[286]: Sent: 86423.814730017 Recv: 86431.060896436 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[287]: Sent: 86423.819602309 Recv: 86423.836874225 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 33   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[288]: Sent: 86424.099829684 Recv: 86431.114219561 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 25   ServerImgID: 25   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[289]: Sent: 86424.190576892 Recv: 86431.114227603 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 33   ServerImgID: 33   Rejected: No
[#CLIENT#] R[290]: Sent: 86424.268182350 Recv: 86431.158523436 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[291]: Sent: 86424.354453850 Recv: 86431.213376603 Opcode: IMG_BLUR        OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[292]: Sent: 86424.510209309 Recv: 86431.231451103 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 33   ServerImgID: 33   Rejected: No HASH: a46fa185b469892706544a2d486bf142
[#CLIENT#] R[293]: Sent: 86424.520526934 Recv: 86424.554966601 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 34   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[294]: Sent: 86424.692492726 Recv: 86431.676833645 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No
[#CLIENT#] R[295]: Sent: 86424.870715434 Recv: 86431.716550603 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 21   ServerImgID: 21   Rejected: No
[#CLIENT#] R[296]: Sent: 86424.943381101 Recv: 86432.181224520 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[297]: Sent: 86425.029901517 Recv: 86432.199516812 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 17   ServerImgID: 17   Rejected: No HASH: 87504e6eb7330f31ab17020c33a18aa9
[#CLIENT#] R[298]: Sent: 86425.170984142 Recv: 86432.301414437 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[299]: Sent: 86425.186575101 Recv: 86432.466338937 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[300]: Sent: 86425.372611476 Recv: 86432.766710604 Opcode: IMG_BLUR        OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No
[#CLIENT#] R[301]: Sent: 86425.482536476 Recv: 86432.850931562 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[302]: Sent: 86425.701899976 Recv: 86433.314103771 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No
[#CLIENT#] R[303]: Sent: 86425.733455351 Recv: 86433.334680354 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[304]: Sent: 86425.840692476 Recv: 86433.348038229 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 28   ServerImgID: 28   Rejected: No
[#CLIENT#] R[305]: Sent: 86425.911444893 Recv: 86433.432978146 Opcode: IMG_BLUR        OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[306]: Sent: 86425.926814810 Recv: 86433.654250688 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[307]: Sent: 86426.030283185 Recv: 86426.048071351 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 35   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[308]: Sent: 86426.160164393 Recv: 86433.742174229 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[309]: Sent: 86426.327921393 Recv: 86426.362423685 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 36   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[310]: Sent: 86426.451686476 Recv: 86426.469868851 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 37   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[311]: Sent: 86426.618770893 Recv: 86433.904108979 Opcode: IMG_BLUR        OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[312]: Sent: 86426.830875852 Recv: 86434.168641604 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[313]: Sent: 86426.875542685 Recv: 86434.275083896 Opcode: IMG_BLUR        OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[314]: Sent: 86426.979858018 Recv: 86434.576944230 Opcode: IMG_BLUR        OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[315]: Sent: 86427.183498143 Recv: 86435.040292897 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[316]: Sent: 86427.347446519 Recv: 86435.503312688 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 29   ServerImgID: 29   Rejected: No
[#CLIENT#] R[317]: Sent: 86427.393196685 Recv: 86427.411129185 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 38   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[318]: Sent: 86427.502587894 Recv: 86435.543552730 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[319]: Sent: 86427.559249935 Recv: 86435.649491564 Opcode: IMG_BLUR        OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[320]: Sent: 86427.621028519 Recv: 86435.767398022 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[321]: Sent: 86427.646473102 Recv: 86436.200183689 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No
[#CLIENT#] R[322]: Sent: 86427.682329685 Recv: 86436.283862022 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 35   ServerImgID: 35   Rejected: No
[#CLIENT#] R[323]: Sent: 86427.747808769 Recv: 86436.368043106 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[324]: Sent: 86427.943672810 Recv: 86436.406046939 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 28   ServerImgID: 28   Rejected: No
[#CLIENT#] R[325]: Sent: 86427.964120935 Recv: 86436.470015106 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 38   ServerImgID: 38   Rejected: No
[#CLIENT#] R[326]: Sent: 86427.998228560 Recv: 86436.490856481 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[327]: Sent: 86428.114601394 Recv: 86436.753126897 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 23   ServerImgID: 23   Rejected: No
[#CLIENT#] R[328]: Sent: 86428.435844644 Recv: 86436.760097731 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[329]: Sent: 86428.633458061 Recv: 86428.651275852 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 39   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[330]: Sent: 86428.728065394 Recv: 86436.844199981 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[331]: Sent: 86428.904478561 Recv: 86436.851333022 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No
[#CLIENT#] R[332]: Sent: 86428.956514144 Recv: 86436.951144981 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No HASH: 443973423be9f977eba85b1a8c0f41a9
[#CLIENT#] R[333]: Sent: 86428.973359603 Recv: 86436.951156022 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[334]: Sent: 86429.016046978 Recv: 86429.119088144 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 40   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[335]: Sent: 86429.221370519 Recv: 86436.981044731 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 17   ServerImgID: 17   Rejected: No
[#CLIENT#] R[336]: Sent: 86429.299359061 Recv: 86436.988332481 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 27   ServerImgID: 27   Rejected: No
[#CLIENT#] R[337]: Sent: 86429.320662103 Recv: 86437.089147606 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No HASH: 15cbf08ec384eb4822b847c3b349f691
[#CLIENT#] R[338]: Sent: 86429.347661311 Recv: 86437.155301189 Opcode: IMG_BLUR        OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[339]: Sent: 86429.390672061 Recv: 86437.239381231 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 26   ServerImgID: 26   Rejected: No
[#CLIENT#] R[340]: Sent: 86429.432799478 Recv: 86437.489306689 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 16   ServerImgID: 16   Rejected: No
[#CLIENT#] R[341]: Sent: 86429.598568853 Recv: 86429.616930561 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 41   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[342]: Sent: 86429.690593228 Recv: 86429.743046770 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 42   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[343]: Sent: 86429.787482645 Recv: 86437.573589898 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[344]: Sent: 86429.902440853 Recv: 86429.954539061 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 43   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[345]: Sent: 86429.969666270 Recv: 86438.039989523 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[346]: Sent: 86430.061467436 Recv: 86438.094300565 Opcode: IMG_BLUR        OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[347]: Sent: 86430.264845644 Recv: 86430.282640519 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 44   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[348]: Sent: 86430.320175519 Recv: 86438.558210773 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 22   ServerImgID: 22   Rejected: No
[#CLIENT#] R[349]: Sent: 86430.396217061 Recv: 86438.658954940 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No HASH: 09265369a030e219fcd2d80a99ded564
[#CLIENT#] R[350]: Sent: 86430.715089811 Recv: 86438.658977565 Opcode: IMG_BLUR        OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[351]: Sent: 86430.720616686 Recv: 86430.823480770 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 45   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[352]: Sent: 86430.827552270 Recv: 86438.917049148 Opcode: IMG_BLUR        OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[353]: Sent: 86430.852434978 Recv: 86430.954537811 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 46   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[354]: Sent: 86430.962207436 Recv: 86439.403349024 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No
[#CLIENT#] R[355]: Sent: 86431.023875061 Recv: 86439.575412690 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[356]: Sent: 86431.114239228 Recv: 86439.682048649 Opcode: IMG_BLUR        OW: 1 ClientImgID: 34   ServerImgID: 34   Rejected: No
[#CLIENT#] R[357]: Sent: 86431.231463395 Recv: 86439.771101565 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[358]: Sent: 86431.296010895 Recv: 86431.314226853 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 47   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[359]: Sent: 86431.581411187 Recv: 86440.020742107 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 25   ServerImgID: 25   Rejected: No
[#CLIENT#] R[360]: Sent: 86431.812674812 Recv: 86440.038821482 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No HASH: 17f53b44873a51687c7b7eb59caa78d4
[#CLIENT#] R[361]: Sent: 86432.067095895 Recv: 86440.107872816 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No
[#CLIENT#] R[362]: Sent: 86432.301432062 Recv: 86440.125990982 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No HASH: e86ac01aa209232d9ecce0271f9ce47b
[#CLIENT#] R[363]: Sent: 86432.301977395 Recv: 86440.226879982 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No HASH: 2dd00aef69f7247958b4025a2a00fe32
[#CLIENT#] R[364]: Sent: 86432.400766229 Recv: 86440.226890691 Opcode: IMG_BLUR        OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No
[#CLIENT#] R[365]: Sent: 86432.404522520 Recv: 86440.484938941 Opcode: IMG_BLUR        OW: 1 ClientImgID: 21   ServerImgID: 21   Rejected: No
[#CLIENT#] R[366]: Sent: 86432.610169312 Recv: 86440.503304607 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No HASH: e86ac01aa209232d9ecce0271f9ce47b
[#CLIENT#] R[367]: Sent: 86432.722710104 Recv: 86432.741634229 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 48   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[368]: Sent: 86432.843207104 Recv: 86440.528265108 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[369]: Sent: 86433.396490854 Recv: 86433.432971854 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 49   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[370]: Sent: 86433.443423312 Recv: 86440.991199316 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No
[#CLIENT#] R[371]: Sent: 86433.477858646 Recv: 86441.011402858 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 23   ServerImgID: 23   Rejected: No
[#CLIENT#] R[372]: Sent: 86433.525800437 Recv: 86441.115478983 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No HASH: 8aedd77e65db0bdf11484030beb7f7d2
[#CLIENT#] R[373]: Sent: 86433.746123688 Recv: 86441.266913150 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 42   ServerImgID: 42   Rejected: No
[#CLIENT#] R[374]: Sent: 86433.765611271 Recv: 86441.388917983 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[375]: Sent: 86434.025202104 Recv: 86441.445796691 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[376]: Sent: 86434.057549896 Recv: 86441.464134066 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 26   ServerImgID: 26   Rejected: No HASH: 9d73e97ac536ed43ec67b869dac562a7
[#CLIENT#] R[377]: Sent: 86434.233992354 Recv: 86441.534769191 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 33   ServerImgID: 33   Rejected: No
[#CLIENT#] R[378]: Sent: 86434.294338521 Recv: 86441.621672608 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[379]: Sent: 86434.356234730 Recv: 86434.374664230 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 50   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[380]: Sent: 86434.423555855 Recv: 86441.678008233 Opcode: IMG_BLUR        OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No
[#CLIENT#] R[381]: Sent: 86434.444399355 Recv: 86441.718252108 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[382]: Sent: 86434.693825230 Recv: 86441.737296650 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No HASH: 2ec8a864904a738fd306d50b3cd3cf7e
[#CLIENT#] R[383]: Sent: 86434.789477855 Recv: 86434.841749896 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 51   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[384]: Sent: 86434.911451271 Recv: 86441.737311358 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 17   ServerImgID: 17   Rejected: No
[#CLIENT#] R[385]: Sent: 86435.016520897 Recv: 86441.755231941 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 33   ServerImgID: 33   Rejected: No HASH: 0ca2b17283ae8bada714cf75628b9380
[#CLIENT#] R[386]: Sent: 86435.089985813 Recv: 86441.781076775 Opcode: IMG_BLUR        OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[387]: Sent: 86435.202541397 Recv: 86442.243633192 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[388]: Sent: 86435.357831813 Recv: 86442.252706858 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 33   ServerImgID: 33   Rejected: No
[#CLIENT#] R[389]: Sent: 86435.398523397 Recv: 86442.743363317 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[390]: Sent: 86435.426468397 Recv: 86442.781172275 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No HASH: 94cf2cdf5b2100fc3b24dff8d66c2ed5
[#CLIENT#] R[391]: Sent: 86435.480576855 Recv: 86442.828170609 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[392]: Sent: 86435.631056938 Recv: 86443.314744275 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[393]: Sent: 86435.646780897 Recv: 86443.477753026 Opcode: IMG_BLUR        OW: 1 ClientImgID: 43   ServerImgID: 43   Rejected: No
[#CLIENT#] R[394]: Sent: 86435.720989522 Recv: 86435.755429939 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 52   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[395]: Sent: 86435.833477189 Recv: 86443.561677192 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[396]: Sent: 86435.860359105 Recv: 86443.667346692 Opcode: IMG_BLUR        OW: 1 ClientImgID: 34   ServerImgID: 34   Rejected: No
[#CLIENT#] R[397]: Sent: 86435.925173022 Recv: 86444.233424901 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 40   ServerImgID: 40   Rejected: No
[#CLIENT#] R[398]: Sent: 86436.208646147 Recv: 86444.629445484 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 40   ServerImgID: 40   Rejected: No
[#CLIENT#] R[399]: Sent: 86436.239678189 Recv: 86444.924247610 Opcode: IMG_BLUR        OW: 1 ClientImgID: 22   ServerImgID: 22   Rejected: No
[#CLIENT#] R[400]: Sent: 86436.299217314 Recv: 86444.954545068 Opcode: IMG_BLUR        OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[401]: Sent: 86436.387587356 Recv: 86436.406059522 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 53   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[402]: Sent: 86436.762963397 Recv: 86444.973204901 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No HASH: 63462aae85d7bb2238584f421e5321b0
[#CLIENT#] R[403]: Sent: 86437.182851148 Recv: 86445.204299610 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 51   ServerImgID: 51   Rejected: No
[#CLIENT#] R[404]: Sent: 86437.255380814 Recv: 86437.307796273 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 54   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[405]: Sent: 86437.442510231 Recv: 86445.367775568 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 49   ServerImgID: 49   Rejected: No
[#CLIENT#] R[406]: Sent: 86437.530356106 Recv: 86445.529157318 Opcode: IMG_BLUR        OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[407]: Sent: 86437.569512523 Recv: 86445.614988860 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 38   ServerImgID: 38   Rejected: No
[#CLIENT#] R[408]: Sent: 86437.724316773 Recv: 86445.635533027 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[409]: Sent: 86437.780140190 Recv: 86445.799568610 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 49   ServerImgID: 49   Rejected: No
[#CLIENT#] R[410]: Sent: 86437.902374856 Recv: 86445.883681652 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 39   ServerImgID: 39   Rejected: No
[#CLIENT#] R[411]: Sent: 86437.903209648 Recv: 86445.928452735 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No
[#CLIENT#] R[412]: Sent: 86437.977209231 Recv: 86446.030862902 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 40   ServerImgID: 40   Rejected: No HASH: c805a881624da3f0e7f8f6fc6f74044a
[#CLIENT#] R[413]: Sent: 86437.995541940 Recv: 86446.030877110 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 26   ServerImgID: 26   Rejected: No
[#CLIENT#] R[414]: Sent: 86438.076978981 Recv: 86446.104342527 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No
[#CLIENT#] R[415]: Sent: 86438.098534231 Recv: 86446.206844485 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No HASH: d2c3d5995b9441fdf8a21ca59f5bfb21
[#CLIENT#] R[416]: Sent: 86438.228506565 Recv: 86446.371503319 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 42   ServerImgID: 42   Rejected: No
[#CLIENT#] R[417]: Sent: 86438.341910356 Recv: 86446.835345361 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 29   ServerImgID: 29   Rejected: No
[#CLIENT#] R[418]: Sent: 86438.469805315 Recv: 86438.522357065 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 55   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[419]: Sent: 86438.658986190 Recv: 86446.876012819 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[420]: Sent: 86438.812524982 Recv: 86438.915235773 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 56   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[421]: Sent: 86438.963304898 Recv: 86447.038134569 Opcode: IMG_BLUR        OW: 1 ClientImgID: 23   ServerImgID: 23   Rejected: No
[#CLIENT#] R[422]: Sent: 86439.156220732 Recv: 86447.092554361 Opcode: IMG_BLUR        OW: 1 ClientImgID: 35   ServerImgID: 35   Rejected: No
[#CLIENT#] R[423]: Sent: 86439.555030940 Recv: 86447.556965069 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[424]: Sent: 86439.792571482 Recv: 86439.827037107 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 57   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[425]: Sent: 86439.843879816 Recv: 86439.946098899 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 58   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[426]: Sent: 86439.977175149 Recv: 86447.729029403 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 52   ServerImgID: 52   Rejected: No
[#CLIENT#] R[427]: Sent: 86440.042415941 Recv: 86447.783517528 Opcode: IMG_BLUR        OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[428]: Sent: 86440.073529149 Recv: 86447.796884403 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 52   ServerImgID: 52   Rejected: No
[#CLIENT#] R[429]: Sent: 86440.226901066 Recv: 86448.259822653 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[430]: Sent: 86440.335800482 Recv: 86448.509270986 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 43   ServerImgID: 43   Rejected: No
[#CLIENT#] R[431]: Sent: 86440.762381191 Recv: 86449.006710570 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[432]: Sent: 86440.776134649 Recv: 86449.041882820 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 36   ServerImgID: 36   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[433]: Sent: 86440.782403274 Recv: 86449.257023653 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[434]: Sent: 86440.929010733 Recv: 86449.291239945 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 36   ServerImgID: 36   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[435]: Sent: 86441.115497066 Recv: 86449.397748945 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No HASH: 265c37ce11140c300e85e1d7606634c6
[#CLIENT#] R[436]: Sent: 86441.276880358 Recv: 86441.295163358 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 59   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[437]: Sent: 86441.354654441 Recv: 86441.388926900 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 60   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[438]: Sent: 86441.392524400 Recv: 86449.397756695 Opcode: IMG_BLUR        OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No
[#CLIENT#] R[439]: Sent: 86441.435563025 Recv: 86449.397770737 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[440]: Sent: 86441.605859400 Recv: 86449.442974528 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[441]: Sent: 86441.621623566 Recv: 86449.545982487 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[442]: Sent: 86441.663245316 Recv: 86449.563619320 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 33   ServerImgID: 33   Rejected: No HASH: 8424c5f06ec75b6d7be01c9662dba8cc
[#CLIENT#] R[443]: Sent: 86441.922750650 Recv: 86449.621466029 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[444]: Sent: 86441.929808400 Recv: 86449.710178404 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[445]: Sent: 86441.969043067 Recv: 86450.173058112 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 22   ServerImgID: 22   Rejected: No
[#CLIENT#] R[446]: Sent: 86442.188363567 Recv: 86450.193530695 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 25   ServerImgID: 25   Rejected: No
[#CLIENT#] R[447]: Sent: 86442.255298692 Recv: 86450.280148904 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No
[#CLIENT#] R[448]: Sent: 86442.416373567 Recv: 86450.743671654 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No
[#CLIENT#] R[449]: Sent: 86442.495696900 Recv: 86450.762423654 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No HASH: 99904a9a04062db3ec5b5af7eda23f71
[#CLIENT#] R[450]: Sent: 86442.542726817 Recv: 86451.207508029 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 56   ServerImgID: 56   Rejected: No
[#CLIENT#] R[451]: Sent: 86442.549747192 Recv: 86442.567605608 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 61   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[452]: Sent: 86442.568252525 Recv: 86451.508217154 Opcode: IMG_BLUR        OW: 1 ClientImgID: 21   ServerImgID: 21   Rejected: No
[#CLIENT#] R[453]: Sent: 86442.573073650 Recv: 86451.595125404 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No
[#CLIENT#] R[454]: Sent: 86442.591623317 Recv: 86451.634610696 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[455]: Sent: 86442.624679942 Recv: 86452.097674280 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No
[#CLIENT#] R[456]: Sent: 86442.701950525 Recv: 86452.348114655 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 23   ServerImgID: 23   Rejected: No
[#CLIENT#] R[457]: Sent: 86442.725092359 Recv: 86452.437351738 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[458]: Sent: 86442.869936192 Recv: 86452.540698322 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 29   ServerImgID: 29   Rejected: No HASH: 93c6c71a0c9f784606e4a999406c05c6
[#CLIENT#] R[459]: Sent: 86442.935606650 Recv: 86452.540720322 Opcode: IMG_BLUR        OW: 1 ClientImgID: 50   ServerImgID: 50   Rejected: No
[#CLIENT#] R[460]: Sent: 86443.198783192 Recv: 86452.748846030 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 55   ServerImgID: 55   Rejected: No
[#CLIENT#] R[461]: Sent: 86443.345290776 Recv: 86452.762637697 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 57   ServerImgID: 57   Rejected: No
[#CLIENT#] R[462]: Sent: 86443.800824651 Recv: 86452.865742322 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No HASH: 769e766e455d7911c84b1647970036eb
[#CLIENT#] R[463]: Sent: 86443.927386776 Recv: 86453.017965530 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 42   ServerImgID: 42   Rejected: No
[#CLIENT#] R[464]: Sent: 86443.928861609 Recv: 86443.963242651 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 62   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[465]: Sent: 86444.067588859 Recv: 86453.038730905 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 54   ServerImgID: 54   Rejected: No
[#CLIENT#] R[466]: Sent: 86444.116670151 Recv: 86453.093053280 Opcode: IMG_BLUR        OW: 1 ClientImgID: 44   ServerImgID: 44   Rejected: No
[#CLIENT#] R[467]: Sent: 86444.120191359 Recv: 86453.100266738 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 59   ServerImgID: 59   Rejected: No
[#CLIENT#] R[468]: Sent: 86444.123973901 Recv: 86444.233419443 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 63   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[469]: Sent: 86444.289574276 Recv: 86453.440634947 Opcode: IMG_BLUR        OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[470]: Sent: 86444.372465651 Recv: 86453.705207780 Opcode: IMG_BLUR        OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No
[#CLIENT#] R[471]: Sent: 86444.401920526 Recv: 86453.723372572 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 39   ServerImgID: 39   Rejected: No HASH: d4f94469bfe2b5ed7246046002f99653
[#CLIENT#] R[472]: Sent: 86444.507008151 Recv: 86453.794115822 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 44   ServerImgID: 44   Rejected: No
[#CLIENT#] R[473]: Sent: 86444.516413693 Recv: 86454.258113156 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[474]: Sent: 86444.585334151 Recv: 86444.603093401 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 64   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[475]: Sent: 86444.889765193 Recv: 86444.924234901 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 65   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[476]: Sent: 86445.062579860 Recv: 86454.341808489 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 38   ServerImgID: 38   Rejected: No
[#CLIENT#] R[477]: Sent: 86445.225935401 Recv: 86454.827786614 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[478]: Sent: 86445.316849026 Recv: 86454.883270489 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 30   ServerImgID: 30   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[479]: Sent: 86445.577681943 Recv: 86445.596284027 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 66   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[480]: Sent: 86445.637749068 Recv: 86454.883278489 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[481]: Sent: 86445.661753027 Recv: 86455.134566448 Opcode: IMG_BLUR        OW: 1 ClientImgID: 40   ServerImgID: 40   Rejected: No
[#CLIENT#] R[482]: Sent: 86445.756724568 Recv: 86455.221301781 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[483]: Sent: 86445.835766360 Recv: 86455.309763781 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 39   ServerImgID: 39   Rejected: No
[#CLIENT#] R[484]: Sent: 86445.841894402 Recv: 86455.504197906 Opcode: IMG_BLUR        OW: 1 ClientImgID: 65   ServerImgID: 65   Rejected: No
[#CLIENT#] R[485]: Sent: 86445.880646152 Recv: 86455.606555156 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No HASH: 5fbf731145da02fb096ea1d97a956e1e
[#CLIENT#] R[486]: Sent: 86446.975727611 Recv: 86455.606568156 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 49   ServerImgID: 49   Rejected: No
[#CLIENT#] R[487]: Sent: 86447.040017319 Recv: 86455.666288031 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 52   ServerImgID: 52   Rejected: No
[#CLIENT#] R[488]: Sent: 86447.051610361 Recv: 86455.831038198 Opcode: IMG_BLUR        OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[489]: Sent: 86447.085040361 Recv: 86456.002429615 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No
[#CLIENT#] R[490]: Sent: 86447.150379486 Recv: 86456.027624240 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 42   ServerImgID: 42   Rejected: No
[#CLIENT#] R[491]: Sent: 86447.248176527 Recv: 86456.190605240 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 60   ServerImgID: 60   Rejected: No
[#CLIENT#] R[492]: Sent: 86447.314664569 Recv: 86456.659600782 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 21   ServerImgID: 21   Rejected: No
[#CLIENT#] R[493]: Sent: 86447.320275694 Recv: 86456.699545657 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 21   ServerImgID: 21   Rejected: No
[#CLIENT#] R[494]: Sent: 86447.325199986 Recv: 86456.753485282 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No HASH: 8ee92d5fe2cf8dcafc52abe575e551a9
[#CLIENT#] R[495]: Sent: 86447.390658861 Recv: 86456.965546365 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[496]: Sent: 86448.109108944 Recv: 86448.161677444 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 67   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[497]: Sent: 86448.649046445 Recv: 86456.978950657 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 65   ServerImgID: 65   Rejected: No
[#CLIENT#] R[498]: Sent: 86448.717245820 Recv: 86448.735464486 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 68   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[499]: Sent: 86448.813167486 Recv: 86448.847386236 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 69   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[500]: Sent: 86448.929732528 Recv: 86448.948025903 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 70   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[501]: Sent: 86448.960705778 Recv: 86457.140896949 Opcode: IMG_BLUR        OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[502]: Sent: 86449.041897320 Recv: 86457.181699032 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[503]: Sent: 86449.072669278 Recv: 86457.268456907 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 50   ServerImgID: 50   Rejected: No
[#CLIENT#] R[504]: Sent: 86449.162032528 Recv: 86457.731518282 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[505]: Sent: 86449.455471153 Recv: 86457.836176782 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No HASH: d7748f1a206eb62d36a79102083cf548
[#CLIENT#] R[506]: Sent: 86449.487823945 Recv: 86457.836188324 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 57   ServerImgID: 57   Rejected: No
[#CLIENT#] R[507]: Sent: 86449.527589153 Recv: 86449.545978528 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 71   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[508]: Sent: 86449.782981279 Recv: 86458.258047199 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 27   ServerImgID: 27   Rejected: No
[#CLIENT#] R[509]: Sent: 86449.876995320 Recv: 86458.258050908 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 36   ServerImgID: 36   Rejected: No
[#CLIENT#] R[510]: Sent: 86449.921999029 Recv: 86458.415285658 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 65   ServerImgID: 65   Rejected: No
[#CLIENT#] R[511]: Sent: 86449.992440612 Recv: 86458.878358491 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 45   ServerImgID: 45   Rejected: No
[#CLIENT#] R[512]: Sent: 86450.021513779 Recv: 86458.919063408 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[513]: Sent: 86450.045761070 Recv: 86458.919526075 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 16   ServerImgID: 16   Rejected: No
[#CLIENT#] R[514]: Sent: 86450.328574154 Recv: 86459.006549700 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 17   ServerImgID: 17   Rejected: No
[#CLIENT#] R[515]: Sent: 86450.395692529 Recv: 86459.170437283 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 28   ServerImgID: 28   Rejected: No
[#CLIENT#] R[516]: Sent: 86450.415481779 Recv: 86459.420080700 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[517]: Sent: 86450.513755446 Recv: 86459.455262783 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No HASH: 434ea3af0e2fce0af8833464e6fda832
[#CLIENT#] R[518]: Sent: 86450.549777112 Recv: 86459.475455908 Opcode: IMG_BLUR        OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[519]: Sent: 86450.588072946 Recv: 86459.559393033 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[520]: Sent: 86450.901883737 Recv: 86459.566201450 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[521]: Sent: 86451.021617571 Recv: 86459.668649450 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No HASH: 2f188c6767b30436ddf1bb7dddb39792
[#CLIENT#] R[522]: Sent: 86451.039693154 Recv: 86459.668658367 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 69   ServerImgID: 69   Rejected: No
[#CLIENT#] R[523]: Sent: 86451.225451738 Recv: 86459.668661575 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 30   ServerImgID: 30   Rejected: No
[#CLIENT#] R[524]: Sent: 86451.380895904 Recv: 86459.723981283 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 51   ServerImgID: 51   Rejected: No HASH: be2f2892be0a6d85742dab3365fb5d6a
[#CLIENT#] R[525]: Sent: 86451.385741988 Recv: 86459.723988117 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 21   ServerImgID: 21   Rejected: No
[#CLIENT#] R[526]: Sent: 86451.396176196 Recv: 86459.723991825 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No
[#CLIENT#] R[527]: Sent: 86451.684244488 Recv: 86451.702019863 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 72   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[528]: Sent: 86451.787402905 Recv: 86459.755560575 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[529]: Sent: 86451.853589988 Recv: 86460.005815408 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 51   ServerImgID: 51   Rejected: No
[#CLIENT#] R[530]: Sent: 86451.877544238 Recv: 86460.024584950 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 47   ServerImgID: 47   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[531]: Sent: 86451.916437655 Recv: 86460.097685408 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 66   ServerImgID: 66   Rejected: No
[#CLIENT#] R[532]: Sent: 86452.184341363 Recv: 86460.560432158 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 29   ServerImgID: 29   Rejected: No
[#CLIENT#] R[533]: Sent: 86452.256029238 Recv: 86460.647211075 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 53   ServerImgID: 53   Rejected: No
[#CLIENT#] R[534]: Sent: 86452.295621946 Recv: 86460.694566408 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[535]: Sent: 86452.639460155 Recv: 86460.945164159 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 51   ServerImgID: 51   Rejected: No
[#CLIENT#] R[536]: Sent: 86452.687603863 Recv: 86461.028732242 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 72   ServerImgID: 72   Rejected: No
[#CLIENT#] R[537]: Sent: 86452.873739322 Recv: 86461.047761700 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No HASH: 0d3d7d856df5680b1b6a63fd5b3314b5
[#CLIENT#] R[538]: Sent: 86452.988938405 Recv: 86461.101039742 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 51   ServerImgID: 51   Rejected: No HASH: 8e0e76c9075fd45334543ee2a3edaf7f
[#CLIENT#] R[539]: Sent: 86453.153144614 Recv: 86461.517866367 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 58   ServerImgID: 58   Rejected: No
[#CLIENT#] R[540]: Sent: 86453.325342530 Recv: 86461.780688951 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 43   ServerImgID: 43   Rejected: No
[#CLIENT#] R[541]: Sent: 86453.334862322 Recv: 86453.440629364 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 73   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[542]: Sent: 86453.453343072 Recv: 86461.867589826 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[543]: Sent: 86453.470842197 Recv: 86453.488329364 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 74   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[544]: Sent: 86453.544121030 Recv: 86461.909051367 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 66   ServerImgID: 66   Rejected: No
[#CLIENT#] R[545]: Sent: 86453.742881030 Recv: 86462.361739743 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 40   ServerImgID: 40   Rejected: No
[#CLIENT#] R[546]: Sent: 86454.051370364 Recv: 86462.824347784 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No
[#CLIENT#] R[547]: Sent: 86454.263989239 Recv: 86463.073809285 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 43   ServerImgID: 43   Rejected: No
[#CLIENT#] R[548]: Sent: 86454.295224656 Recv: 86463.335921118 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 55   ServerImgID: 55   Rejected: No
[#CLIENT#] R[549]: Sent: 86454.349321739 Recv: 86463.420143618 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[550]: Sent: 86454.453835739 Recv: 86463.438303535 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No HASH: 2534f3b4744ebd76878f4b516855f50e
[#CLIENT#] R[551]: Sent: 86454.701893864 Recv: 86454.754530739 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 75   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[552]: Sent: 86455.006476948 Recv: 86463.468089410 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 73   ServerImgID: 73   Rejected: No
[#CLIENT#] R[553]: Sent: 86455.179634573 Recv: 86463.474878326 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 72   ServerImgID: 72   Rejected: No
[#CLIENT#] R[554]: Sent: 86455.243218698 Recv: 86463.566303243 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 47   ServerImgID: 47   Rejected: No
[#CLIENT#] R[555]: Sent: 86455.348365448 Recv: 86464.031063202 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 63   ServerImgID: 63   Rejected: No
[#CLIENT#] R[556]: Sent: 86455.401180531 Recv: 86455.504184156 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 76   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[557]: Sent: 86455.692501365 Recv: 86464.138529410 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No HASH: bac05c6033777c730e76ff3b22f12369
[#CLIENT#] R[558]: Sent: 86455.931266615 Recv: 86464.504083744 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[559]: Sent: 86455.949318573 Recv: 86464.560492244 Opcode: IMG_BLUR        OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No
[#CLIENT#] R[560]: Sent: 86455.960050323 Recv: 86464.810905369 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 43   ServerImgID: 43   Rejected: No
[#CLIENT#] R[561]: Sent: 86456.227474907 Recv: 86464.974542577 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 34   ServerImgID: 34   Rejected: No
[#CLIENT#] R[562]: Sent: 86456.597967907 Recv: 86465.138101494 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 34   ServerImgID: 34   Rejected: No
[#CLIENT#] R[563]: Sent: 86456.616188032 Recv: 86465.388695286 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[564]: Sent: 86456.617626865 Recv: 86465.688280953 Opcode: IMG_BLUR        OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No
[#CLIENT#] R[565]: Sent: 86456.804835782 Recv: 86465.730064953 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 44   ServerImgID: 44   Rejected: No
[#CLIENT#] R[566]: Sent: 86456.904438574 Recv: 86456.921975782 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 77   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[567]: Sent: 86457.060059990 Recv: 86465.859027161 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 57   ServerImgID: 57   Rejected: No
[#CLIENT#] R[568]: Sent: 86457.064722532 Recv: 86465.961490744 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No HASH: bb2bb45c3407997b8d9e65123dc1b341
[#CLIENT#] R[569]: Sent: 86457.087506740 Recv: 86466.163747369 Opcode: IMG_BLUR        OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[570]: Sent: 86457.090634240 Recv: 86466.182719328 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No HASH: 09455cf5848b5aa244104a6b118f9bfb
[#CLIENT#] R[571]: Sent: 86457.133315824 Recv: 86466.326789703 Opcode: IMG_BLUR        OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[572]: Sent: 86457.161340865 Recv: 86466.490525078 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 60   ServerImgID: 60   Rejected: No
[#CLIENT#] R[573]: Sent: 86457.344597157 Recv: 86466.510728078 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 43   ServerImgID: 43   Rejected: No
[#CLIENT#] R[574]: Sent: 86457.379666741 Recv: 86466.598010328 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[575]: Sent: 86457.383555491 Recv: 86457.418071157 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 78   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[576]: Sent: 86457.684944157 Recv: 86466.605995495 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[577]: Sent: 86457.947720991 Recv: 86457.965328782 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 79   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[578]: Sent: 86458.205764033 Recv: 86458.258043324 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 80   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[579]: Sent: 86458.273625324 Recv: 86466.624887953 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 71   ServerImgID: 71   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[580]: Sent: 86458.278673699 Recv: 86466.624899328 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 52   ServerImgID: 52   Rejected: No
[#CLIENT#] R[581]: Sent: 86458.310362699 Recv: 86466.628155661 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[582]: Sent: 86458.440816991 Recv: 86466.646228370 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 26   ServerImgID: 26   Rejected: No HASH: 55348f8ec458faee8aef206c3daa6f14
[#CLIENT#] R[583]: Sent: 86458.482378491 Recv: 86466.717740953 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[584]: Sent: 86458.745059075 Recv: 86466.735964120 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No HASH: b52bf2575572cfd08cd9725b1ec1a230
[#CLIENT#] R[585]: Sent: 86459.073872158 Recv: 86467.210784370 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[586]: Sent: 86459.083936533 Recv: 86467.252037037 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No
[#CLIENT#] R[587]: Sent: 86459.216916075 Recv: 86467.333783412 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 64   ServerImgID: 64   Rejected: No
[#CLIENT#] R[588]: Sent: 86459.348253741 Recv: 86467.583877787 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 55   ServerImgID: 55   Rejected: No
[#CLIENT#] R[589]: Sent: 86459.810516950 Recv: 86467.833884787 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 54   ServerImgID: 54   Rejected: No
[#CLIENT#] R[590]: Sent: 86459.923809700 Recv: 86467.920447954 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 66   ServerImgID: 66   Rejected: No
[#CLIENT#] R[591]: Sent: 86460.149262367 Recv: 86467.933846579 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[592]: Sent: 86460.234429158 Recv: 86467.952317370 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 79   ServerImgID: 79   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[593]: Sent: 86460.350728700 Recv: 86460.461542200 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 81   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[594]: Sent: 86460.513237617 Recv: 86468.021515579 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No
[#CLIENT#] R[595]: Sent: 86460.646398617 Recv: 86468.273922495 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 51   ServerImgID: 51   Rejected: No
[#CLIENT#] R[596]: Sent: 86460.721950575 Recv: 86468.358215704 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 77   ServerImgID: 77   Rejected: No
[#CLIENT#] R[597]: Sent: 86460.775933325 Recv: 86468.446824662 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 61   ServerImgID: 61   Rejected: No
[#CLIENT#] R[598]: Sent: 86460.791579200 Recv: 86460.809129367 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 82   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[599]: Sent: 86460.951131617 Recv: 86468.504019204 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 75   ServerImgID: 75   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[600]: Sent: 86461.013115534 Recv: 86468.778474121 Opcode: IMG_BLUR        OW: 1 ClientImgID: 76   ServerImgID: 76   Rejected: No
[#CLIENT#] R[601]: Sent: 86461.101050700 Recv: 86468.925066204 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No
[#CLIENT#] R[602]: Sent: 86461.187038284 Recv: 86468.943258871 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 74   ServerImgID: 74   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[603]: Sent: 86461.273634867 Recv: 86469.089565537 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 28   ServerImgID: 28   Rejected: No
[#CLIENT#] R[604]: Sent: 86461.287963575 Recv: 86469.130062829 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 51   ServerImgID: 51   Rejected: No
[#CLIENT#] R[605]: Sent: 86461.364272784 Recv: 86469.130074163 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[606]: Sent: 86461.535073867 Recv: 86469.164515454 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 63   ServerImgID: 63   Rejected: No
[#CLIENT#] R[607]: Sent: 86461.786445534 Recv: 86469.655567371 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[608]: Sent: 86461.930128826 Recv: 86461.948170034 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 83   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[609]: Sent: 86461.978016784 Recv: 86469.673407996 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No HASH: b52bf2575572cfd08cd9725b1ec1a230
[#CLIENT#] R[610]: Sent: 86462.058045992 Recv: 86469.820142996 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 34   ServerImgID: 34   Rejected: No
[#CLIENT#] R[611]: Sent: 86462.174741201 Recv: 86469.839052621 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 70   ServerImgID: 70   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[612]: Sent: 86462.462429243 Recv: 86469.873893288 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No HASH: cc8b12cd931a024df74ed947b274d736
[#CLIENT#] R[613]: Sent: 86462.467038201 Recv: 86462.573504493 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 84   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[614]: Sent: 86462.613620784 Recv: 86469.873899955 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 66   ServerImgID: 66   Rejected: No
[#CLIENT#] R[615]: Sent: 86462.744436368 Recv: 86470.090917746 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[616]: Sent: 86462.767323118 Recv: 86470.341625205 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 75   ServerImgID: 75   Rejected: No
[#CLIENT#] R[617]: Sent: 86462.956886701 Recv: 86470.819090122 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 45   ServerImgID: 45   Rejected: No
[#CLIENT#] R[618]: Sent: 86463.008237660 Recv: 86463.060680701 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 85   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[619]: Sent: 86463.149853618 Recv: 86470.845777663 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[620]: Sent: 86463.201965160 Recv: 86471.110543872 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[621]: Sent: 86463.276805826 Recv: 86471.131230288 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 43   ServerImgID: 43   Rejected: No
[#CLIENT#] R[622]: Sent: 86463.464924826 Recv: 86471.434382580 Opcode: IMG_BLUR        OW: 1 ClientImgID: 81   ServerImgID: 81   Rejected: No
[#CLIENT#] R[623]: Sent: 86463.748571160 Recv: 86471.897724289 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 84   ServerImgID: 84   Rejected: No
[#CLIENT#] R[624]: Sent: 86463.817062243 Recv: 86471.984874372 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 68   ServerImgID: 68   Rejected: No
[#CLIENT#] R[625]: Sent: 86464.138546077 Recv: 86472.159052664 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No
[#CLIENT#] R[626]: Sent: 86464.405815202 Recv: 86472.167072206 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[627]: Sent: 86464.414011285 Recv: 86472.330804164 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 52   ServerImgID: 52   Rejected: No
[#CLIENT#] R[628]: Sent: 86464.561566369 Recv: 86464.579439077 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 86   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[629]: Sent: 86464.596313160 Recv: 86472.491987539 Opcode: IMG_BLUR        OW: 1 ClientImgID: 55   ServerImgID: 55   Rejected: No
[#CLIENT#] R[630]: Sent: 86465.041644577 Recv: 86472.510514581 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 68   ServerImgID: 68   Rejected: No HASH: 78a7633528e7dc2fc020b73ae9ed6596
[#CLIENT#] R[631]: Sent: 86465.173428869 Recv: 86472.622531456 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No
[#CLIENT#] R[632]: Sent: 86465.284951661 Recv: 86472.632600623 Opcode: IMG_BLUR        OW: 1 ClientImgID: 64   ServerImgID: 64   Rejected: No
[#CLIENT#] R[633]: Sent: 86465.333539869 Recv: 86472.741717248 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 83   ServerImgID: 83   Rejected: No
[#CLIENT#] R[634]: Sent: 86465.393167327 Recv: 86472.844452789 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No HASH: 416c13671c31bb9bb45ea4b2c6e57530
[#CLIENT#] R[635]: Sent: 86466.022044203 Recv: 86473.231401873 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No
[#CLIENT#] R[636]: Sent: 86466.105559869 Recv: 86473.244787539 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No
[#CLIENT#] R[637]: Sent: 86466.459839828 Recv: 86473.286987164 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[638]: Sent: 86466.474090286 Recv: 86473.450540790 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 49   ServerImgID: 49   Rejected: No
[#CLIENT#] R[639]: Sent: 86466.646243995 Recv: 86473.541671290 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[640]: Sent: 86466.677564911 Recv: 86473.643743415 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No HASH: 4c67d9a86c38a6a55fed1e0ec9f7d27e
[#CLIENT#] R[641]: Sent: 86466.682861536 Recv: 86473.643760706 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 70   ServerImgID: 70   Rejected: No
[#CLIENT#] R[642]: Sent: 86466.872521953 Recv: 86474.120270373 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 21   ServerImgID: 21   Rejected: No
[#CLIENT#] R[643]: Sent: 86466.966119620 Recv: 86474.606189123 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 84   ServerImgID: 84   Rejected: No
[#CLIENT#] R[644]: Sent: 86467.012120078 Recv: 86474.856309665 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[645]: Sent: 86467.074453120 Recv: 86474.877057582 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 23   ServerImgID: 23   Rejected: No
[#CLIENT#] R[646]: Sent: 86467.171719287 Recv: 86467.205869328 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 87   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[647]: Sent: 86467.210753495 Recv: 86475.346974124 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 40   ServerImgID: 40   Rejected: No
[#CLIENT#] R[648]: Sent: 86467.300159662 Recv: 86467.317872787 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 88   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[649]: Sent: 86467.423578912 Recv: 86467.441079995 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 89   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[650]: Sent: 86467.614152745 Recv: 86475.510690291 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[651]: Sent: 86467.685082745 Recv: 86475.974368957 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 76   ServerImgID: 76   Rejected: No
[#CLIENT#] R[652]: Sent: 86467.711771870 Recv: 86476.058570124 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 74   ServerImgID: 74   Rejected: No
[#CLIENT#] R[653]: Sent: 86467.900800204 Recv: 86476.358285416 Opcode: IMG_BLUR        OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[654]: Sent: 86467.952331329 Recv: 86476.376436833 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 26   ServerImgID: 26   Rejected: No HASH: 55348f8ec458faee8aef206c3daa6f14
[#CLIENT#] R[655]: Sent: 86467.959050745 Recv: 86476.522677916 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No
[#CLIENT#] R[656]: Sent: 86467.966794162 Recv: 86468.019060620 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 90   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[657]: Sent: 86468.048274620 Recv: 86476.614565124 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 47   ServerImgID: 47   Rejected: No
[#CLIENT#] R[658]: Sent: 86468.162313370 Recv: 86468.179985287 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 91   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[659]: Sent: 86468.193456120 Recv: 86476.776872749 Opcode: IMG_BLUR        OW: 1 ClientImgID: 43   ServerImgID: 43   Rejected: No
[#CLIENT#] R[660]: Sent: 86468.330608912 Recv: 86476.868097541 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No
[#CLIENT#] R[661]: Sent: 86468.405876787 Recv: 86476.875664166 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No
[#CLIENT#] R[662]: Sent: 86468.428983995 Recv: 86476.893815458 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 79   ServerImgID: 79   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[663]: Sent: 86468.504031996 Recv: 86476.962939208 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[664]: Sent: 86468.607778121 Recv: 86468.642010496 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 92   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[665]: Sent: 86468.669569121 Recv: 86468.778448537 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 93   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[666]: Sent: 86468.805205746 Recv: 86477.046661333 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[667]: Sent: 86468.826647287 Recv: 86477.153081041 Opcode: IMG_BLUR        OW: 1 ClientImgID: 92   ServerImgID: 92   Rejected: No
[#CLIENT#] R[668]: Sent: 86468.835664996 Recv: 86477.166406041 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 92   ServerImgID: 92   Rejected: No
[#CLIENT#] R[669]: Sent: 86468.840500162 Recv: 86477.417204833 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[670]: Sent: 86469.059430954 Recv: 86477.667766875 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 42   ServerImgID: 42   Rejected: No
[#CLIENT#] R[671]: Sent: 86469.269179579 Recv: 86477.757244083 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[672]: Sent: 86469.276070663 Recv: 86478.057566500 Opcode: IMG_BLUR        OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[673]: Sent: 86469.312347496 Recv: 86478.093100917 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 78   ServerImgID: 78   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[674]: Sent: 86469.334595288 Recv: 86478.111482167 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 50   ServerImgID: 50   Rejected: No HASH: 718d34266062049362b6c40493e775e1
[#CLIENT#] R[675]: Sent: 86469.347370663 Recv: 86478.550203709 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[676]: Sent: 86469.422671371 Recv: 86469.528855954 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 94   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[677]: Sent: 86469.533784704 Recv: 86478.641560875 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No
[#CLIENT#] R[678]: Sent: 86469.673417871 Recv: 86478.706753875 Opcode: IMG_BLUR        OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[679]: Sent: 86469.690025163 Recv: 86478.789974917 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 70   ServerImgID: 70   Rejected: No
[#CLIENT#] R[680]: Sent: 86470.082878996 Recv: 86478.846696167 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 51   ServerImgID: 51   Rejected: No HASH: 546b5df34b55d9683741c2a2fb3984e8
[#CLIENT#] R[681]: Sent: 86470.086261996 Recv: 86478.846713917 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 75   ServerImgID: 75   Rejected: No
[#CLIENT#] R[682]: Sent: 86470.255615913 Recv: 86470.274023038 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 95   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[683]: Sent: 86470.357393496 Recv: 86478.897543542 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 72   ServerImgID: 72   Rejected: No
[#CLIENT#] R[684]: Sent: 86470.371378830 Recv: 86478.952983876 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 16   ServerImgID: 16   Rejected: No HASH: 4b2c35b86d903c301597d0ec3e9cb745
[#CLIENT#] R[685]: Sent: 86470.534094913 Recv: 86479.197435584 Opcode: IMG_BLUR        OW: 1 ClientImgID: 94   ServerImgID: 94   Rejected: No
[#CLIENT#] R[686]: Sent: 86470.639148038 Recv: 86479.285322001 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 77   ServerImgID: 77   Rejected: No
[#CLIENT#] R[687]: Sent: 86470.775519288 Recv: 86470.809798580 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 96   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[688]: Sent: 86470.851198413 Recv: 86479.748247209 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[689]: Sent: 86470.863444788 Recv: 86479.790057668 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[690]: Sent: 86470.885425580 Recv: 86479.854309001 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 89   ServerImgID: 89   Rejected: No
[#CLIENT#] R[691]: Sent: 86470.925901330 Recv: 86479.908583793 Opcode: IMG_BLUR        OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[692]: Sent: 86470.931067038 Recv: 86480.394887793 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 84   ServerImgID: 84   Rejected: No
[#CLIENT#] R[693]: Sent: 86471.012050288 Recv: 86480.502853085 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 84   ServerImgID: 84   Rejected: No HASH: 724f8c7da6816ec84a846429e542b3af
[#CLIENT#] R[694]: Sent: 86471.047421538 Recv: 86471.099922955 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 97   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[695]: Sent: 86471.357415955 Recv: 86480.567200710 Opcode: IMG_BLUR        OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[696]: Sent: 86471.469668330 Recv: 86481.029380877 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 76   ServerImgID: 76   Rejected: No
[#CLIENT#] R[697]: Sent: 86471.622709664 Recv: 86481.083966043 Opcode: IMG_BLUR        OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[698]: Sent: 86471.681529705 Recv: 86471.792822789 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 98   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[699]: Sent: 86471.928723289 Recv: 86471.980739997 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 99   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[700]: Sent: 86472.110430206 Recv: 86481.168055252 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 39   ServerImgID: 39   Rejected: No
[#CLIENT#] R[701]: Sent: 86472.143716331 Recv: 86481.417955210 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 75   ServerImgID: 75   Rejected: No
[#CLIENT#] R[702]: Sent: 86472.177849289 Recv: 86481.425094377 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 26   ServerImgID: 26   Rejected: No
[#CLIENT#] R[703]: Sent: 86472.344367831 Recv: 86472.396787747 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 100  Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[704]: Sent: 86472.413332664 Recv: 86481.687342627 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 75   ServerImgID: 75   Rejected: No
[#CLIENT#] R[705]: Sent: 86472.485334414 Recv: 86481.730768669 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 40   ServerImgID: 40   Rejected: No
[#CLIENT#] R[706]: Sent: 86472.486596747 Recv: 86482.032177710 Opcode: IMG_BLUR        OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No
[#CLIENT#] R[707]: Sent: 86472.510520914 Recv: 86482.283163294 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 75   ServerImgID: 75   Rejected: No
[#CLIENT#] R[708]: Sent: 86472.516962164 Recv: 86472.622526747 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 101  Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[709]: Sent: 86472.671522956 Recv: 86482.301425544 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 35   ServerImgID: 35   Rejected: No HASH: e91603ff2577620f87e773d162cbb1b8
[#CLIENT#] R[710]: Sent: 86472.708282706 Recv: 86472.741710873 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 102  Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[711]: Sent: 86472.903969956 Recv: 86482.533389461 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 54   ServerImgID: 54   Rejected: No
[#CLIENT#] R[712]: Sent: 86473.139816789 Recv: 86473.158137664 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 103  Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[713]: Sent: 86473.214606623 Recv: 86482.617591044 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[714]: Sent: 86473.507561248 Recv: 86473.541642373 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 104  Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[715]: Sent: 86473.643769748 Recv: 86482.701633544 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[716]: Sent: 86473.658643915 Recv: 86482.865108419 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 104  ServerImgID: 104  Rejected: No
[#CLIENT#] R[717]: Sent: 86473.689810415 Recv: 86483.165413753 Opcode: IMG_BLUR        OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[718]: Sent: 86473.815112706 Recv: 86483.651775919 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No
[#CLIENT#] R[719]: Sent: 86473.984823081 Recv: 86474.037325373 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 105  Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[720]: Sent: 86474.154298665 Recv: 86483.902922545 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 25   ServerImgID: 25   Rejected: No
[#CLIENT#] R[721]: Sent: 86474.229856665 Recv: 86484.005504253 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 73   ServerImgID: 73   Rejected: No HASH: a475f010c4c086a083fedd66f3725234
[#CLIENT#] R[722]: Sent: 86474.340948998 Recv: 86474.393530790 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 106  Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[723]: Sent: 86474.411150540 Recv: 86484.005514086 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 74   ServerImgID: 74   Rejected: No
[#CLIENT#] R[724]: Sent: 86474.492733082 Recv: 86484.040387086 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 60   ServerImgID: 60   Rejected: No HASH: b1b45b2076c3827d711962b82aa208f4
[#CLIENT#] R[725]: Sent: 86474.509752665 Recv: 86484.040392795 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No
[#CLIENT#] R[726]: Sent: 86474.723177499 Recv: 86484.058316920 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 91   ServerImgID: 91   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[727]: Sent: 86474.775603790 Recv: 86484.178653920 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 69   ServerImgID: 69   Rejected: No
[#CLIENT#] R[728]: Sent: 86474.848597165 Recv: 86484.428482836 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 80   ServerImgID: 80   Rejected: No
[#CLIENT#] R[729]: Sent: 86474.955515165 Recv: 86484.593094920 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 36   ServerImgID: 36   Rejected: No
[#CLIENT#] R[730]: Sent: 86475.039212207 Recv: 86484.679635253 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 47   ServerImgID: 47   Rejected: No
[#CLIENT#] R[731]: Sent: 86475.409034249 Recv: 86484.929036920 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 25   ServerImgID: 25   Rejected: No
[#CLIENT#] R[732]: Sent: 86475.427101207 Recv: 86485.012708128 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 72   ServerImgID: 72   Rejected: No
[#CLIENT#] R[733]: Sent: 86475.482296082 Recv: 86485.103910128 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 103  ServerImgID: 103  Rejected: No
[#CLIENT#] R[734]: Sent: 86475.565387249 Recv: 86485.367584420 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[735]: Sent: 86475.699122416 Recv: 86475.717016916 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 107  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[736]: Sent: 86475.777982499 Recv: 86485.381056920 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[737]: Sent: 86475.910663999 Recv: 86485.472894837 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[738]: Sent: 86476.049346791 Recv: 86485.508053920 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 34   ServerImgID: 34   Rejected: No HASH: 6af9501a868a53fa1aad440e6858e798
[#CLIENT#] R[739]: Sent: 86476.132699374 Recv: 86485.544448754 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 92   ServerImgID: 92   Rejected: No HASH: 2ed48485c391a80bfb05fe3b8525c2eb
[#CLIENT#] R[740]: Sent: 86476.216538708 Recv: 86485.999520796 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 27   ServerImgID: 27   Rejected: No
[#CLIENT#] R[741]: Sent: 86476.223157416 Recv: 86476.240941374 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 108  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[742]: Sent: 86476.435531708 Recv: 86485.999524796 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No
[#CLIENT#] R[743]: Sent: 86476.627237916 Recv: 86486.111148171 Opcode: IMG_BLUR        OW: 1 ClientImgID: 25   ServerImgID: 25   Rejected: No
[#CLIENT#] R[744]: Sent: 86476.693126749 Recv: 86486.195175546 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 89   ServerImgID: 89   Rejected: No
[#CLIENT#] R[745]: Sent: 86476.810958416 Recv: 86486.234303421 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No
[#CLIENT#] R[746]: Sent: 86476.817506958 Recv: 86486.282108004 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 84   ServerImgID: 84   Rejected: No
[#CLIENT#] R[747]: Sent: 86476.949539750 Recv: 86486.388498046 Opcode: IMG_BLUR        OW: 1 ClientImgID: 102  ServerImgID: 102  Rejected: No
[#CLIENT#] R[748]: Sent: 86477.297981875 Recv: 86486.429176754 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 93   ServerImgID: 93   Rejected: No
[#CLIENT#] R[749]: Sent: 86477.364738166 Recv: 86486.535480587 Opcode: IMG_BLUR        OW: 1 ClientImgID: 69   ServerImgID: 69   Rejected: No
[#CLIENT#] R[750]: Sent: 86477.375481791 Recv: 86486.591556337 Opcode: IMG_BLUR        OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No
[#CLIENT#] R[751]: Sent: 86477.445539666 Recv: 86486.676018921 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[752]: Sent: 86477.470740416 Recv: 86486.759777504 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 107  ServerImgID: 107  Rejected: No
[#CLIENT#] R[753]: Sent: 86477.734758542 Recv: 86486.843586879 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 82   ServerImgID: 82   Rejected: No
[#CLIENT#] R[754]: Sent: 86477.888088000 Recv: 86486.883351796 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 93   ServerImgID: 93   Rejected: No
[#CLIENT#] R[755]: Sent: 86477.930613875 Recv: 86486.967110296 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 72   ServerImgID: 72   Rejected: No
[#CLIENT#] R[756]: Sent: 86478.111496208 Recv: 86487.053930546 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No
[#CLIENT#] R[757]: Sent: 86478.392566000 Recv: 86487.089567713 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 69   ServerImgID: 69   Rejected: No HASH: 08d5145482ee2b793c663934d28ba736
[#CLIENT#] R[758]: Sent: 86478.422882042 Recv: 86487.139489671 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 89   ServerImgID: 89   Rejected: No
[#CLIENT#] R[759]: Sent: 86478.451959084 Recv: 86487.194743171 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 75   ServerImgID: 75   Rejected: No HASH: adc23dc6dc33b962db7266b6c30d2722
[#CLIENT#] R[760]: Sent: 86478.536294417 Recv: 86487.194775379 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No
[#CLIENT#] R[761]: Sent: 86478.687935084 Recv: 86478.706747792 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 109  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[762]: Sent: 86478.952998376 Recv: 86487.300795421 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 29   ServerImgID: 29   Rejected: No HASH: 9d278f693acd1c3d933d5bcbd5e97aef
[#CLIENT#] R[763]: Sent: 86479.310846667 Recv: 86487.654475713 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 40   ServerImgID: 40   Rejected: No
[#CLIENT#] R[764]: Sent: 86479.388895792 Recv: 86487.746600213 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[765]: Sent: 86479.403088501 Recv: 86487.996636630 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 23   ServerImgID: 23   Rejected: No
[#CLIENT#] R[766]: Sent: 86479.468693001 Recv: 86488.459508505 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 56   ServerImgID: 56   Rejected: No
[#CLIENT#] R[767]: Sent: 86479.473316667 Recv: 86488.759982964 Opcode: IMG_BLUR        OW: 1 ClientImgID: 94   ServerImgID: 94   Rejected: No
[#CLIENT#] R[768]: Sent: 86479.555072709 Recv: 86488.862573755 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 22   ServerImgID: 22   Rejected: No HASH: 8ad3ff104f1f02bc48625a0d3278d7ca
[#CLIENT#] R[769]: Sent: 86479.702688418 Recv: 86488.862581464 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 78   ServerImgID: 78   Rejected: No
[#CLIENT#] R[770]: Sent: 86479.731398459 Recv: 86488.862627880 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[771]: Sent: 86479.813376918 Recv: 86488.902987214 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 107  ServerImgID: 107  Rejected: No
[#CLIENT#] R[772]: Sent: 86479.958279959 Recv: 86488.994620589 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[773]: Sent: 86480.087021626 Recv: 86489.048209547 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 67   ServerImgID: 67   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[774]: Sent: 86480.121096834 Recv: 86489.066751089 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 59   ServerImgID: 59   Rejected: No HASH: ca8dabad272577686d07ecf7bb519b7f
[#CLIENT#] R[775]: Sent: 86480.502870376 Recv: 86489.082171714 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[776]: Sent: 86480.549843376 Recv: 86489.100240422 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 74   ServerImgID: 74   Rejected: No HASH: 3b3e20aa776ada5ed79da1b1242d54fd
[#CLIENT#] R[777]: Sent: 86480.655101085 Recv: 86489.155179297 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 16   ServerImgID: 16   Rejected: No HASH: 4b2c35b86d903c301597d0ec3e9cb745
[#CLIENT#] R[778]: Sent: 86480.725104918 Recv: 86489.172374214 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[779]: Sent: 86480.956346918 Recv: 86489.635930881 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 93   ServerImgID: 93   Rejected: No
[#CLIENT#] R[780]: Sent: 86480.996560376 Recv: 86490.099611172 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[781]: Sent: 86481.220963502 Recv: 86490.563404172 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[782]: Sent: 86481.230901960 Recv: 86490.653017631 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[783]: Sent: 86481.247573752 Recv: 86490.671868297 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 50   ServerImgID: 50   Rejected: No HASH: 718d34266062049362b6c40493e775e1
[#CLIENT#] R[784]: Sent: 86481.247628002 Recv: 86481.266042793 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 110  Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[785]: Sent: 86481.320315543 Recv: 86490.953056131 Opcode: IMG_BLUR        OW: 1 ClientImgID: 45   ServerImgID: 45   Rejected: No
[#CLIENT#] R[786]: Sent: 86481.461302877 Recv: 86491.009604881 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 97   ServerImgID: 97   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[787]: Sent: 86481.613044335 Recv: 86491.440462756 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No
[#CLIENT#] R[788]: Sent: 86481.669947585 Recv: 86491.903258506 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 101  ServerImgID: 101  Rejected: No
[#CLIENT#] R[789]: Sent: 86482.042698210 Recv: 86491.990106923 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 53   ServerImgID: 53   Rejected: No
[#CLIENT#] R[790]: Sent: 86482.150468127 Recv: 86492.046307548 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 43   ServerImgID: 43   Rejected: No HASH: 1832c766ca31fff55366ca0b5ebfe998
[#CLIENT#] R[791]: Sent: 86482.156041335 Recv: 86492.046328965 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 23   ServerImgID: 23   Rejected: No
[#CLIENT#] R[792]: Sent: 86482.435987502 Recv: 86492.311701090 Opcode: IMG_BLUR        OW: 1 ClientImgID: 27   ServerImgID: 27   Rejected: No
[#CLIENT#] R[793]: Sent: 86482.455375877 Recv: 86492.347026923 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No HASH: e0d35013596353b35647792dfb1d70fb
[#CLIENT#] R[794]: Sent: 86482.588158169 Recv: 86492.775382215 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 81   ServerImgID: 81   Rejected: No
[#CLIENT#] R[795]: Sent: 86482.605474544 Recv: 86492.829816673 Opcode: IMG_BLUR        OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[796]: Sent: 86482.691983169 Recv: 86492.914548507 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 39   ServerImgID: 39   Rejected: No
[#CLIENT#] R[797]: Sent: 86482.756729752 Recv: 86492.969054840 Opcode: IMG_BLUR        OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[798]: Sent: 86482.983151044 Recv: 86483.001178169 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 111  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[799]: Sent: 86483.051586211 Recv: 86493.052955132 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 35   ServerImgID: 35   Rejected: No
[#CLIENT#] R[800]: Sent: 86483.189438253 Recv: 86493.523246882 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[801]: Sent: 86483.211919544 Recv: 86493.988740424 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 98   ServerImgID: 98   Rejected: No
[#CLIENT#] R[802]: Sent: 86483.249665044 Recv: 86494.238836133 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 16   ServerImgID: 16   Rejected: No
[#CLIENT#] R[803]: Sent: 86483.441189128 Recv: 86494.331312008 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[804]: Sent: 86483.518974378 Recv: 86494.383271258 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 81   ServerImgID: 81   Rejected: No
[#CLIENT#] R[805]: Sent: 86483.628626378 Recv: 86494.467341008 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 74   ServerImgID: 74   Rejected: No
[#CLIENT#] R[806]: Sent: 86483.647327086 Recv: 86494.631481674 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[807]: Sent: 86483.703242836 Recv: 86494.650326633 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 72   ServerImgID: 72   Rejected: No HASH: 60ea7ced6c2564b47808ed9c0f294ac5
[#CLIENT#] R[808]: Sent: 86483.712706753 Recv: 86494.705541841 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 23   ServerImgID: 23   Rejected: No HASH: 5e5931dcd1b1bc70190585de0496669f
[#CLIENT#] R[809]: Sent: 86483.820358961 Recv: 86494.720686174 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 68   ServerImgID: 68   Rejected: No
[#CLIENT#] R[810]: Sent: 86483.824116628 Recv: 86494.893618841 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[811]: Sent: 86484.904643253 Recv: 86494.932748674 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 63   ServerImgID: 63   Rejected: No
[#CLIENT#] R[812]: Sent: 86484.915482878 Recv: 86495.420113008 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 93   ServerImgID: 93   Rejected: No
[#CLIENT#] R[813]: Sent: 86485.065754837 Recv: 86495.504276841 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 33   ServerImgID: 33   Rejected: No
[#CLIENT#] R[814]: Sent: 86485.198011837 Recv: 86495.558729591 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 42   ServerImgID: 42   Rejected: No HASH: be9bcb384b494d77de72bf72c984488a
[#CLIENT#] R[815]: Sent: 86485.548262337 Recv: 86485.657167379 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 112  Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[816]: Sent: 86485.893819629 Recv: 86485.999516296 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 113  Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[817]: Sent: 86486.034898671 Recv: 86495.968824925 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 81   ServerImgID: 81   Rejected: No
[#CLIENT#] R[818]: Sent: 86486.295082254 Recv: 86496.001154342 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 106  ServerImgID: 106  Rejected: No
[#CLIENT#] R[819]: Sent: 86486.320415337 Recv: 86496.018958050 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 79   ServerImgID: 79   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[820]: Sent: 86486.338697004 Recv: 86496.077346092 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No
[#CLIENT#] R[821]: Sent: 86486.392374587 Recv: 86496.541872550 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[822]: Sent: 86486.394661337 Recv: 86496.581750925 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[823]: Sent: 86486.656786171 Recv: 86496.621598425 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 22   ServerImgID: 22   Rejected: No
[#CLIENT#] R[824]: Sent: 86486.693303463 Recv: 86496.667629967 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 27   ServerImgID: 27   Rejected: No
[#CLIENT#] R[825]: Sent: 86486.915962338 Recv: 86497.157862967 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No
[#CLIENT#] R[826]: Sent: 86487.102671754 Recv: 86497.420576842 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 55   ServerImgID: 55   Rejected: No
[#CLIENT#] R[827]: Sent: 86487.300811754 Recv: 86497.725742134 Opcode: IMG_BLUR        OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[828]: Sent: 86487.307604005 Recv: 86497.975424801 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 97   ServerImgID: 97   Rejected: No
[#CLIENT#] R[829]: Sent: 86487.429356255 Recv: 86498.067096884 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No
[#CLIENT#] R[830]: Sent: 86487.435258046 Recv: 86498.552744843 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 76   ServerImgID: 76   Rejected: No
[#CLIENT#] R[831]: Sent: 86487.640765880 Recv: 86498.641088385 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[832]: Sent: 86487.683861921 Recv: 86498.648802718 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[833]: Sent: 86487.847142796 Recv: 86498.948645135 Opcode: IMG_BLUR        OW: 1 ClientImgID: 58   ServerImgID: 58   Rejected: No
[#CLIENT#] R[834]: Sent: 86487.856495963 Recv: 86487.874332088 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 114  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[835]: Sent: 86488.010235797 Recv: 86499.110142468 Opcode: IMG_BLUR        OW: 1 ClientImgID: 16   ServerImgID: 16   Rejected: No
[#CLIENT#] R[836]: Sent: 86488.067070297 Recv: 86499.197045677 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No
[#CLIENT#] R[837]: Sent: 86488.107046338 Recv: 86499.281274385 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 35   ServerImgID: 35   Rejected: No
[#CLIENT#] R[838]: Sent: 86488.303220838 Recv: 86499.453471885 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 49   ServerImgID: 49   Rejected: No
[#CLIENT#] R[839]: Sent: 86488.315290922 Recv: 86499.537369427 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 108  ServerImgID: 108  Rejected: No
[#CLIENT#] R[840]: Sent: 86488.454049588 Recv: 86499.839158052 Opcode: IMG_BLUR        OW: 1 ClientImgID: 93   ServerImgID: 93   Rejected: No
[#CLIENT#] R[841]: Sent: 86488.618471713 Recv: 86499.929133510 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[842]: Sent: 86488.862593630 Recv: 86500.092170969 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 36   ServerImgID: 36   Rejected: No
[#CLIENT#] R[843]: Sent: 86489.155193422 Recv: 86500.115319385 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[844]: Sent: 86489.377367839 Recv: 86500.577577177 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 84   ServerImgID: 84   Rejected: No
[#CLIENT#] R[845]: Sent: 86489.433577964 Recv: 86500.741427969 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 65   ServerImgID: 65   Rejected: No
[#CLIENT#] R[846]: Sent: 86489.507489631 Recv: 86500.905318094 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 36   ServerImgID: 36   Rejected: No
[#CLIENT#] R[847]: Sent: 86489.515363631 Recv: 86500.918695261 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 28   ServerImgID: 28   Rejected: No
[#CLIENT#] R[848]: Sent: 86489.564349631 Recv: 86501.021614427 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No HASH: 9cc30f3f41b6c1664957f515b67bb06b
[#CLIENT#] R[849]: Sent: 86489.612665339 Recv: 86501.021629552 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 50   ServerImgID: 50   Rejected: No
[#CLIENT#] R[850]: Sent: 86489.646477297 Recv: 86501.099720427 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 77   ServerImgID: 77   Rejected: No
[#CLIENT#] R[851]: Sent: 86489.677273547 Recv: 86501.183776094 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[852]: Sent: 86489.809193131 Recv: 86501.273077636 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 39   ServerImgID: 39   Rejected: No
[#CLIENT#] R[853]: Sent: 86489.933827172 Recv: 86501.375454011 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No HASH: 44c02a40a3054f600a746dd4283071ab
[#CLIENT#] R[854]: Sent: 86489.947938631 Recv: 86501.375469428 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 72   ServerImgID: 72   Rejected: No
[#CLIENT#] R[855]: Sent: 86489.982912756 Recv: 86501.538666344 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 28   ServerImgID: 28   Rejected: No
[#CLIENT#] R[856]: Sent: 86489.992964631 Recv: 86501.556444594 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 39   ServerImgID: 39   Rejected: No HASH: 7fba26df9b8d47e422afff7b6044e9c1
[#CLIENT#] R[857]: Sent: 86490.040458422 Recv: 86501.658836344 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 56   ServerImgID: 56   Rejected: No HASH: 09265369a030e219fcd2d80a99ded564
[#CLIENT#] R[858]: Sent: 86490.258335506 Recv: 86490.276093297 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 115  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[859]: Sent: 86490.392233297 Recv: 86502.042823636 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 63   ServerImgID: 63   Rejected: No
[#CLIENT#] R[860]: Sent: 86490.458161214 Recv: 86502.205292553 Opcode: IMG_BLUR        OW: 1 ClientImgID: 85   ServerImgID: 85   Rejected: No
[#CLIENT#] R[861]: Sent: 86490.498283631 Recv: 86502.369265136 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[862]: Sent: 86490.509080256 Recv: 86502.425890720 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 75   ServerImgID: 75   Rejected: No HASH: adc23dc6dc33b962db7266b6c30d2722
[#CLIENT#] R[863]: Sent: 86490.525061922 Recv: 86502.454560428 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 88   ServerImgID: 88   Rejected: No
[#CLIENT#] R[864]: Sent: 86490.556722464 Recv: 86502.617865553 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 60   ServerImgID: 60   Rejected: No
[#CLIENT#] R[865]: Sent: 86490.639292839 Recv: 86503.117270762 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[866]: Sent: 86490.783312798 Recv: 86503.198377303 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 108  ServerImgID: 108  Rejected: No
[#CLIENT#] R[867]: Sent: 86490.820107048 Recv: 86490.872033464 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 116  Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[868]: Sent: 86490.946467339 Recv: 86503.304267303 Opcode: IMG_BLUR        OW: 1 ClientImgID: 102  ServerImgID: 102  Rejected: No
[#CLIENT#] R[869]: Sent: 86491.978625423 Recv: 86503.767593887 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 45   ServerImgID: 45   Rejected: No
[#CLIENT#] R[870]: Sent: 86492.089291590 Recv: 86492.197387757 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 117  Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[871]: Sent: 86492.258951340 Recv: 86503.854897720 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[872]: Sent: 86492.347037548 Recv: 86504.333437262 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No
[#CLIENT#] R[873]: Sent: 86492.413028632 Recv: 86504.401992137 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 109  ServerImgID: 109  Rejected: No
[#CLIENT#] R[874]: Sent: 86492.480150548 Recv: 86492.514360382 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 118  Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[875]: Sent: 86492.559211840 Recv: 86504.416043054 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 49   ServerImgID: 49   Rejected: No
[#CLIENT#] R[876]: Sent: 86492.635022632 Recv: 86504.451308429 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 52   ServerImgID: 52   Rejected: No HASH: a8668745537ff91a7572d7046ad701bb
[#CLIENT#] R[877]: Sent: 86492.708434007 Recv: 86504.471036512 Opcode: IMG_BLUR        OW: 1 ClientImgID: 74   ServerImgID: 74   Rejected: No
[#CLIENT#] R[878]: Sent: 86492.760036090 Recv: 86504.520885596 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 27   ServerImgID: 27   Rejected: No
[#CLIENT#] R[879]: Sent: 86492.843834299 Recv: 86492.862181090 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 119  Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[880]: Sent: 86492.912618049 Recv: 86504.604801762 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 111  ServerImgID: 111  Rejected: No
[#CLIENT#] R[881]: Sent: 86492.932021632 Recv: 86492.950155799 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 120  Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[882]: Sent: 86492.968903090 Recv: 86504.659158304 Opcode: IMG_BLUR        OW: 1 ClientImgID: 74   ServerImgID: 74   Rejected: No
[#CLIENT#] R[883]: Sent: 86492.981103924 Recv: 86504.748091846 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 79   ServerImgID: 79   Rejected: No
[#CLIENT#] R[884]: Sent: 86493.107852507 Recv: 86505.210582013 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 94   ServerImgID: 94   Rejected: No
[#CLIENT#] R[885]: Sent: 86493.120016507 Recv: 86505.229785888 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 50   ServerImgID: 50   Rejected: No HASH: 9db28b1eaa63f07ad95591ec3ed72587
[#CLIENT#] R[886]: Sent: 86493.210800299 Recv: 86505.298836554 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No
[#CLIENT#] R[887]: Sent: 86493.241070090 Recv: 86493.294262674 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 121  Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[888]: Sent: 86493.360685215 Recv: 86505.385797554 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 50   ServerImgID: 50   Rejected: No
[#CLIENT#] R[889]: Sent: 86493.377745590 Recv: 86505.514228471 Opcode: IMG_BLUR        OW: 1 ClientImgID: 61   ServerImgID: 61   Rejected: No
[#CLIENT#] R[890]: Sent: 86493.701888966 Recv: 86505.514231721 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 26   ServerImgID: 26   Rejected: No
[#CLIENT#] R[891]: Sent: 86493.750034632 Recv: 86505.514239346 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 40   ServerImgID: 40   Rejected: No
[#CLIENT#] R[892]: Sent: 86493.888253674 Recv: 86505.955519805 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[893]: Sent: 86493.906274216 Recv: 86506.061542013 Opcode: IMG_BLUR        OW: 1 ClientImgID: 96   ServerImgID: 96   Rejected: No
[#CLIENT#] R[894]: Sent: 86494.055768216 Recv: 86506.080032096 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 35   ServerImgID: 35   Rejected: No HASH: f02548bdc1d694bf2aa0e1d35726601f
[#CLIENT#] R[895]: Sent: 86494.248087508 Recv: 86506.149032680 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[896]: Sent: 86494.571718799 Recv: 86506.313432513 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 34   ServerImgID: 34   Rejected: No
[#CLIENT#] R[897]: Sent: 86494.767884508 Recv: 86494.786015049 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 122  Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[898]: Sent: 86494.980631675 Recv: 86506.803976722 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[899]: Sent: 86495.045944716 Recv: 86495.155150425 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 123  Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[900]: Sent: 86495.951446300 Recv: 86506.896032055 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[901]: Sent: 86495.960759883 Recv: 86506.914762764 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 59   ServerImgID: 59   Rejected: No HASH: ca8dabad272577686d07ecf7bb519b7f
[#CLIENT#] R[902]: Sent: 86495.983510592 Recv: 86496.001146300 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 124  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[903]: Sent: 86496.161253883 Recv: 86507.195863555 Opcode: IMG_BLUR        OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No
[#CLIENT#] R[904]: Sent: 86496.205303592 Recv: 86507.445632639 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 55   ServerImgID: 55   Rejected: No
[#CLIENT#] R[905]: Sent: 86496.250722342 Recv: 86507.499947430 Opcode: IMG_BLUR        OW: 1 ClientImgID: 33   ServerImgID: 33   Rejected: No
[#CLIENT#] R[906]: Sent: 86496.271399175 Recv: 86507.602788597 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 58   ServerImgID: 58   Rejected: No HASH: 0e2dd886b2225341ca50f8f37103dbce
[#CLIENT#] R[907]: Sent: 86496.314890633 Recv: 86507.620789722 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 91   ServerImgID: 91   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[908]: Sent: 86496.363126550 Recv: 86507.670353139 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No
[#CLIENT#] R[909]: Sent: 86496.476887884 Recv: 86507.689120347 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 53   ServerImgID: 53   Rejected: No HASH: cb8a2ae1d35da5dc317ed9a391166950
[#CLIENT#] R[910]: Sent: 86496.643154550 Recv: 86507.920739181 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 42   ServerImgID: 42   Rejected: No
[#CLIENT#] R[911]: Sent: 86496.661998592 Recv: 86508.026934722 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 27   ServerImgID: 27   Rejected: No HASH: 113ea43c7c52e20533fd5c0a6c5bc11e
[#CLIENT#] R[912]: Sent: 86496.940558384 Recv: 86508.026941431 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[913]: Sent: 86496.973725800 Recv: 86508.079481889 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No
[#CLIENT#] R[914]: Sent: 86497.011749550 Recv: 86497.064499717 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 125  Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[915]: Sent: 86497.207095134 Recv: 86508.079512431 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[916]: Sent: 86497.336844592 Recv: 86508.336847431 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[917]: Sent: 86497.504674967 Recv: 86497.522919134 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 126  Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[918]: Sent: 86497.555827217 Recv: 86508.423775223 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No
[#CLIENT#] R[919]: Sent: 86497.650978717 Recv: 86508.527069598 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No HASH: a669a8b1c741bbd02a88795289a0e8ac
[#CLIENT#] R[920]: Sent: 86497.998634426 Recv: 86508.527078931 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 51   ServerImgID: 51   Rejected: No
[#CLIENT#] R[921]: Sent: 86498.035435134 Recv: 86508.543481223 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 71   ServerImgID: 71   Rejected: No
[#CLIENT#] R[922]: Sent: 86498.036539926 Recv: 86509.010791223 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 81   ServerImgID: 81   Rejected: No
[#CLIENT#] R[923]: Sent: 86498.212180051 Recv: 86509.097191515 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 126  ServerImgID: 126  Rejected: No
[#CLIENT#] R[924]: Sent: 86498.467109385 Recv: 86509.397902140 Opcode: IMG_BLUR        OW: 1 ClientImgID: 58   ServerImgID: 58   Rejected: No
[#CLIENT#] R[925]: Sent: 86498.474398635 Recv: 86509.452058973 Opcode: IMG_BLUR        OW: 1 ClientImgID: 77   ServerImgID: 77   Rejected: No
[#CLIENT#] R[926]: Sent: 86498.487824093 Recv: 86509.701451598 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 23   ServerImgID: 23   Rejected: No
[#CLIENT#] R[927]: Sent: 86498.492843135 Recv: 86510.163701265 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 101  ServerImgID: 101  Rejected: No
[#CLIENT#] R[928]: Sent: 86498.613029426 Recv: 86510.269104307 Opcode: IMG_BLUR        OW: 1 ClientImgID: 57   ServerImgID: 57   Rejected: No
[#CLIENT#] R[929]: Sent: 86498.885416635 Recv: 86510.372682057 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No HASH: 601af64569241055b07d9a99f0c670a1
[#CLIENT#] R[930]: Sent: 86498.912035968 Recv: 86510.540472724 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[931]: Sent: 86499.002418426 Recv: 86510.560894432 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[932]: Sent: 86499.013859218 Recv: 86511.024512349 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No
[#CLIENT#] R[933]: Sent: 86499.382247177 Recv: 86511.031577224 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[934]: Sent: 86499.902795844 Recv: 86511.084689307 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No HASH: 12c73cb1e8f64e1922959be2a9d982a0
[#CLIENT#] R[935]: Sent: 86499.976804469 Recv: 86511.084742266 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 51   ServerImgID: 51   Rejected: No
[#CLIENT#] R[936]: Sent: 86500.234437219 Recv: 86511.103430307 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No HASH: 9a2938e4f0d7513d21fe58144e3560d3
[#CLIENT#] R[937]: Sent: 86500.283118260 Recv: 86511.121338016 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 26   ServerImgID: 26   Rejected: No HASH: 2cc529524a171427ba242fcf8a09b6ff
[#CLIENT#] R[938]: Sent: 86500.313058844 Recv: 86511.156222057 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No HASH: 2767be6f95d5d7f6dee66214219c59a2
[#CLIENT#] R[939]: Sent: 86500.574274427 Recv: 86511.347388057 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 116  ServerImgID: 116  Rejected: No
[#CLIENT#] R[940]: Sent: 86500.581454136 Recv: 86511.431658641 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[941]: Sent: 86500.649884427 Recv: 86511.681249182 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 54   ServerImgID: 54   Rejected: No
[#CLIENT#] R[942]: Sent: 86500.697343344 Recv: 86500.732224219 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 127  Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[943]: Sent: 86500.838317552 Recv: 86511.772634266 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 53   ServerImgID: 53   Rejected: No
[#CLIENT#] R[944]: Sent: 86501.931447720 Recv: 86511.859654266 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 66   ServerImgID: 66   Rejected: No
[#CLIENT#] R[945]: Sent: 86502.011230136 Recv: 86512.109352224 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[946]: Sent: 86502.039284720 Recv: 86512.116343974 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 107  ServerImgID: 107  Rejected: No
[#CLIENT#] R[947]: Sent: 86502.093350428 Recv: 86512.279912558 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 118  ServerImgID: 118  Rejected: No
[#CLIENT#] R[948]: Sent: 86502.306705303 Recv: 86512.298148016 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 38   ServerImgID: 38   Rejected: No HASH: b8104132493de7040858ff7f6ba4b1e0
[#CLIENT#] R[949]: Sent: 86502.556096095 Recv: 86512.364305849 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 114  ServerImgID: 114  Rejected: No
[#CLIENT#] R[950]: Sent: 86502.571056386 Recv: 86512.450938725 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 122  ServerImgID: 122  Rejected: No
[#CLIENT#] R[951]: Sent: 86502.643280720 Recv: 86512.470293808 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 114  ServerImgID: 114  Rejected: No HASH: 392626c80f548779a200c8ec6e46c645
[#CLIENT#] R[952]: Sent: 86502.686641887 Recv: 86512.539387850 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 38   ServerImgID: 38   Rejected: No
[#CLIENT#] R[953]: Sent: 86502.795020553 Recv: 86512.546145266 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 88   ServerImgID: 88   Rejected: No
[#CLIENT#] R[954]: Sent: 86502.826706887 Recv: 86512.709685933 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 92   ServerImgID: 92   Rejected: No
[#CLIENT#] R[955]: Sent: 86502.837573262 Recv: 86512.793962183 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 82   ServerImgID: 82   Rejected: No
[#CLIENT#] R[956]: Sent: 86502.863153470 Recv: 86512.880934350 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[957]: Sent: 86503.007982178 Recv: 86503.117265887 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 128  Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[958]: Sent: 86503.264187262 Recv: 86513.143490808 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 67   ServerImgID: 67   Rejected: No
[#CLIENT#] R[959]: Sent: 86503.544715054 Recv: 86513.150302975 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 38   ServerImgID: 38   Rejected: No
[#CLIENT#] R[960]: Sent: 86503.568093470 Recv: 86513.312707017 Opcode: IMG_BLUR        OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[961]: Sent: 86503.733401970 Recv: 86513.399620308 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 47   ServerImgID: 47   Rejected: No
[#CLIENT#] R[962]: Sent: 86503.774371095 Recv: 86513.861989850 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[963]: Sent: 86504.002166054 Recv: 86513.946397309 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 91   ServerImgID: 91   Rejected: No
[#CLIENT#] R[964]: Sent: 86504.065418096 Recv: 86514.000789350 Opcode: IMG_BLUR        OW: 1 ClientImgID: 77   ServerImgID: 77   Rejected: No
[#CLIENT#] R[965]: Sent: 86504.069898429 Recv: 86514.014097142 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 49   ServerImgID: 49   Rejected: No
[#CLIENT#] R[966]: Sent: 86504.085575262 Recv: 86504.104015512 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 129  Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[967]: Sent: 86504.223267679 Recv: 86514.119832934 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 128  ServerImgID: 128  Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[968]: Sent: 86504.232085304 Recv: 86514.154721725 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 87   ServerImgID: 87   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[969]: Sent: 86504.315214679 Recv: 86504.333431929 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 130  Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[970]: Sent: 86504.340218054 Recv: 86514.187590309 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No
[#CLIENT#] R[971]: Sent: 86504.451320137 Recv: 86514.349198684 Opcode: IMG_BLUR        OW: 1 ClientImgID: 43   ServerImgID: 43   Rejected: No
[#CLIENT#] R[972]: Sent: 86504.629031346 Recv: 86514.611071934 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 85   ServerImgID: 85   Rejected: No
[#CLIENT#] R[973]: Sent: 86504.972477638 Recv: 86514.629382392 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 86   ServerImgID: 86   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[974]: Sent: 86505.100074221 Recv: 86514.695488309 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[975]: Sent: 86505.229795763 Recv: 86505.281695221 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 131  Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[976]: Sent: 86505.339717179 Recv: 86514.779597392 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 33   ServerImgID: 33   Rejected: No
[#CLIENT#] R[977]: Sent: 86505.362116679 Recv: 86514.835902392 Opcode: IMG_BLUR        OW: 1 ClientImgID: 120  ServerImgID: 120  Rejected: No
[#CLIENT#] R[978]: Sent: 86505.412054513 Recv: 86505.514224138 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 132  Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[979]: Sent: 86505.743946305 Recv: 86514.853930226 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 88   ServerImgID: 88   Rejected: No HASH: 3b3e20aa776ada5ed79da1b1242d54fd
[#CLIENT#] R[980]: Sent: 86505.845420013 Recv: 86514.923319184 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[981]: Sent: 86505.982017680 Recv: 86515.007348934 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 72   ServerImgID: 72   Rejected: No
[#CLIENT#] R[982]: Sent: 86506.115295430 Recv: 86515.307638559 Opcode: IMG_BLUR        OW: 1 ClientImgID: 101  ServerImgID: 101  Rejected: No
[#CLIENT#] R[983]: Sent: 86506.444947305 Recv: 86506.480213805 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 133  Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[984]: Sent: 86506.489295222 Recv: 86515.326033976 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 79   ServerImgID: 79   Rejected: No HASH: ef8229e5c754a6f351669a8d377268c2
[#CLIENT#] R[985]: Sent: 86506.536944680 Recv: 86515.557428434 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 80   ServerImgID: 80   Rejected: No
[#CLIENT#] R[986]: Sent: 86506.821239930 Recv: 86515.823830018 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[987]: Sent: 86506.821359264 Recv: 86515.843727726 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 53   ServerImgID: 53   Rejected: No HASH: 1f1c8796819b3be90020a1649fbceb45
[#CLIENT#] R[988]: Sent: 86506.860084972 Recv: 86506.878036680 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 134  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[989]: Sent: 86506.989533389 Recv: 86516.123575935 Opcode: IMG_BLUR        OW: 1 ClientImgID: 63   ServerImgID: 63   Rejected: No
[#CLIENT#] R[990]: Sent: 86507.493923930 Recv: 86516.207571643 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 89   ServerImgID: 89   Rejected: No
[#CLIENT#] R[991]: Sent: 86507.620801639 Recv: 86516.265400351 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 90   ServerImgID: 90   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[992]: Sent: 86508.026950764 Recv: 86508.079488889 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 135  Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[993]: Sent: 86508.235516098 Recv: 86516.508297560 Opcode: IMG_BLUR        OW: 1 ClientImgID: 84   ServerImgID: 84   Rejected: No
[#CLIENT#] R[994]: Sent: 86508.406766431 Recv: 86516.592073435 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 124  ServerImgID: 124  Rejected: No
[#CLIENT#] R[995]: Sent: 86508.527088306 Recv: 86516.610127102 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 72   ServerImgID: 72   Rejected: No HASH: 5ea1fa06c4cda67fa5c705c720733694
[#CLIENT#] R[996]: Sent: 86508.966108431 Recv: 86516.855095185 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 85   ServerImgID: 85   Rejected: No
[#CLIENT#] R[997]: Sent: 86509.003938806 Recv: 86517.157637852 Opcode: IMG_BLUR        OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[998]: Sent: 86509.028097640 Recv: 86517.193410268 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 102  ServerImgID: 102  Rejected: No HASH: 2789dd1ef70d8504357a520edd47d455
[#CLIENT#] R[999]: Sent: 86509.175722765 Recv: 86509.194271223 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 136  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31"""

run1 = """[#CLIENT#] R[0]: Sent: 111927.531148173 Recv: 111927.549471673 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 0    Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[1]: Sent: 111927.732842840 Recv: 111927.820761506 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[2]: Sent: 111927.885980298 Recv: 111927.978367590 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[3]: Sent: 111927.908084506 Recv: 111928.069635673 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[4]: Sent: 111927.940674465 Recv: 111928.087505215 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No HASH: 2326e8a964742d53375a7edba55f44a4
[#CLIENT#] R[5]: Sent: 111928.039885923 Recv: 111928.058876173 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 1    Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[6]: Sent: 111928.362926132 Recv: 111928.419853965 Opcode: IMG_BLUR        OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[7]: Sent: 111928.489559632 Recv: 111928.523989465 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[8]: Sent: 111928.525646882 Recv: 111928.632541048 Opcode: IMG_BLUR        OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[9]: Sent: 111928.688787507 Recv: 111928.707029757 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[10]: Sent: 111928.707093132 Recv: 111928.794695674 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[11]: Sent: 111928.731757465 Recv: 111928.958244674 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[12]: Sent: 111928.826634840 Recv: 111929.000102632 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[13]: Sent: 111928.901019757 Recv: 111929.021410257 Opcode: IMG_BLUR        OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[14]: Sent: 111928.935658924 Recv: 111929.184515882 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[15]: Sent: 111929.082648049 Recv: 111929.356641466 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[16]: Sent: 111929.116048174 Recv: 111929.413582841 Opcode: IMG_BLUR        OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[17]: Sent: 111929.367486216 Recv: 111929.498243216 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[18]: Sent: 111929.442238966 Recv: 111929.541539341 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[19]: Sent: 111929.551147757 Recv: 111929.634728174 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[20]: Sent: 111929.557815841 Recv: 111929.690901091 Opcode: IMG_BLUR        OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[21]: Sent: 111929.564360716 Recv: 111929.853631049 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[22]: Sent: 111929.796900882 Recv: 111929.979993132 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[23]: Sent: 111929.874562257 Recv: 111929.979978341 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 3    Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[24]: Sent: 111930.051849716 Recv: 111930.106368924 Opcode: IMG_BLUR        OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[25]: Sent: 111930.055914966 Recv: 111930.211372466 Opcode: IMG_BLUR        OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[26]: Sent: 111930.323040924 Recv: 111930.428459383 Opcode: IMG_BLUR        OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[27]: Sent: 111930.457229049 Recv: 111930.548449216 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[28]: Sent: 111930.573704258 Recv: 111930.660568966 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[29]: Sent: 111930.785839216 Recv: 111930.892041216 Opcode: IMG_BLUR        OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[30]: Sent: 111930.811875466 Recv: 111931.030953216 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[31]: Sent: 111930.927955425 Recv: 111931.030947133 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[32]: Sent: 111931.138057425 Recv: 111931.222189341 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[33]: Sent: 111931.395758758 Recv: 111931.412956258 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 5    Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[34]: Sent: 111931.528230758 Recv: 111932.021244758 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[35]: Sent: 111931.552571842 Recv: 111932.105099925 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[36]: Sent: 111931.568566592 Recv: 111932.196464550 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[37]: Sent: 111931.625144383 Recv: 111932.204467884 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[38]: Sent: 111931.779370008 Recv: 111932.222081384 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No HASH: c9e9acb37a12747a13739fb3fe21a308
[#CLIENT#] R[39]: Sent: 111931.805039008 Recv: 111932.320559467 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No HASH: 55f606719c1033a44269b8e4136e8211
[#CLIENT#] R[40]: Sent: 111931.886382258 Recv: 111932.687755175 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[41]: Sent: 111932.123742550 Recv: 111933.153602092 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[42]: Sent: 111932.192198759 Recv: 111933.242281676 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[43]: Sent: 111932.465611009 Recv: 111933.705012009 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[44]: Sent: 111932.604248134 Recv: 111934.168747676 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[45]: Sent: 111932.630737009 Recv: 111932.649132759 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 6    Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[46]: Sent: 111932.665436425 Recv: 111934.252756843 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[47]: Sent: 111932.823262050 Recv: 111934.740506843 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[48]: Sent: 111932.831060467 Recv: 111935.235148760 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[49]: Sent: 111932.904811884 Recv: 111935.721919385 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[50]: Sent: 111933.064707092 Recv: 111935.893356552 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[51]: Sent: 111933.407133717 Recv: 111936.362789386 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[52]: Sent: 111933.417008967 Recv: 111936.381114677 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No HASH: 88580d74c84ac71f83f497a49312521b
[#CLIENT#] R[53]: Sent: 111933.425197342 Recv: 111933.529799467 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 7    Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[54]: Sent: 111933.591695676 Recv: 111936.662928927 Opcode: IMG_BLUR        OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[55]: Sent: 111933.732640884 Recv: 111936.751203469 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[56]: Sent: 111934.928168510 Recv: 111937.247215094 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[57]: Sent: 111934.941640760 Recv: 111937.699628219 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[58]: Sent: 111935.146156385 Recv: 111935.164593343 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 8    Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[59]: Sent: 111935.421108468 Recv: 111937.732525886 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[60]: Sent: 111935.439028218 Recv: 111937.812165303 Opcode: IMG_BLUR        OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[61]: Sent: 111935.610412968 Recv: 111937.830299469 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No HASH: 88580d74c84ac71f83f497a49312521b
[#CLIENT#] R[62]: Sent: 111935.697144135 Recv: 111938.280681594 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[63]: Sent: 111935.707722844 Recv: 111938.336779678 Opcode: IMG_BLUR        OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[64]: Sent: 111935.744063177 Recv: 111938.377076761 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[65]: Sent: 111935.954199802 Recv: 111938.839810720 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[66]: Sent: 111935.957846927 Recv: 111938.926833928 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[67]: Sent: 111936.217469969 Recv: 111939.034034886 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No HASH: 3b45556ca43a453c23cddf80da7af879
[#CLIENT#] R[68]: Sent: 111936.606040261 Recv: 111939.069183053 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No HASH: 732a5bde390f582e4cfff5c80094733c
[#CLIENT#] R[69]: Sent: 111937.017239927 Recv: 111939.236039470 Opcode: IMG_BLUR        OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[70]: Sent: 111937.035246386 Recv: 111937.087656553 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 9    Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[71]: Sent: 111937.095668928 Recv: 111939.698353053 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[72]: Sent: 111937.195031719 Recv: 111937.247190553 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 10   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[73]: Sent: 111937.285243094 Recv: 111939.740086137 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[74]: Sent: 111937.292977928 Recv: 111939.969470887 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[75]: Sent: 111937.398304678 Recv: 111940.004433012 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No HASH: 732a5bde390f582e4cfff5c80094733c
[#CLIENT#] R[76]: Sent: 111937.431188178 Recv: 111940.004446512 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[77]: Sent: 111937.443245803 Recv: 111940.226287554 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[78]: Sent: 111937.732115553 Recv: 111940.687486762 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[79]: Sent: 111937.920701594 Recv: 111940.705540304 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No HASH: 5270006985a5f40de12fea9382d69f27
[#CLIENT#] R[80]: Sent: 111937.963041844 Recv: 111940.705549471 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[81]: Sent: 111937.989715011 Recv: 111940.778739512 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[82]: Sent: 111938.055513053 Recv: 111941.240766096 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[83]: Sent: 111938.075698386 Recv: 111941.703813679 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[84]: Sent: 111938.129183594 Recv: 111941.753342763 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[85]: Sent: 111938.230740928 Recv: 111938.248499428 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 11   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[86]: Sent: 111938.342439553 Recv: 111941.809553013 Opcode: IMG_BLUR        OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[87]: Sent: 111938.382334261 Recv: 111941.896230638 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[88]: Sent: 111938.636133595 Recv: 111942.001444138 Opcode: IMG_BLUR        OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[89]: Sent: 111938.665930511 Recv: 111942.057842555 Opcode: IMG_BLUR        OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[90]: Sent: 111938.696138886 Recv: 111942.114042721 Opcode: IMG_BLUR        OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[91]: Sent: 111938.706016845 Recv: 111942.153220971 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[92]: Sent: 111938.792044970 Recv: 111942.240998763 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[93]: Sent: 111938.826187678 Recv: 111942.402794971 Opcode: IMG_BLUR        OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[94]: Sent: 111938.866231220 Recv: 111942.566311263 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[95]: Sent: 111938.866632511 Recv: 111942.870442263 Opcode: IMG_BLUR        OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[96]: Sent: 111938.887501220 Recv: 111943.333919305 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[97]: Sent: 111939.138803220 Recv: 111943.351983055 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No HASH: 70cf2014ae70367eb9f0b3a744d9fc82
[#CLIENT#] R[98]: Sent: 111939.151824595 Recv: 111943.797163847 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[99]: Sent: 111939.300730053 Recv: 111943.901571889 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[100]: Sent: 111939.498929262 Recv: 111943.974949014 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[101]: Sent: 111939.578483137 Recv: 111944.031189847 Opcode: IMG_BLUR        OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[102]: Sent: 111939.818999804 Recv: 111944.117390972 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[103]: Sent: 111939.904979804 Recv: 111939.939375887 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 12   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[104]: Sent: 111940.139313595 Recv: 111944.124208181 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[105]: Sent: 111940.328437054 Recv: 111944.208488264 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[106]: Sent: 111940.348429929 Recv: 111944.253427431 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[107]: Sent: 111940.363468137 Recv: 111944.339989847 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[108]: Sent: 111940.545662637 Recv: 111944.589662889 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[109]: Sent: 111940.570831554 Recv: 111944.698747306 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No HASH: 57886e6e07fbc6d6f889d8409e86a1dd
[#CLIENT#] R[110]: Sent: 111940.585757762 Recv: 111944.698756139 Opcode: IMG_BLUR        OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[111]: Sent: 111940.854507512 Recv: 111945.142439098 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[112]: Sent: 111941.035897179 Recv: 111945.183054139 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[113]: Sent: 111941.076755429 Recv: 111941.094418679 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 13   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[114]: Sent: 111941.188328763 Recv: 111945.482028723 Opcode: IMG_BLUR        OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[115]: Sent: 111941.195938138 Recv: 111945.643652848 Opcode: IMG_BLUR        OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[116]: Sent: 111941.241153888 Recv: 111946.106704348 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[117]: Sent: 111941.250746513 Recv: 111946.194828182 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[118]: Sent: 111941.338376096 Recv: 111946.356521890 Opcode: IMG_BLUR        OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[119]: Sent: 111941.481868429 Recv: 111946.412943307 Opcode: IMG_BLUR        OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[120]: Sent: 111941.696533721 Recv: 111946.518899265 Opcode: IMG_BLUR        OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[121]: Sent: 111941.719917846 Recv: 111946.981593224 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[122]: Sent: 111941.897130596 Recv: 111947.445204807 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[123]: Sent: 111941.936655180 Recv: 111947.548049266 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No HASH: abaacf2afea051f6c7f8d2df54564402
[#CLIENT#] R[124]: Sent: 111942.355690471 Recv: 111947.548058724 Opcode: IMG_BLUR        OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[125]: Sent: 111942.370409138 Recv: 111947.548070974 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[126]: Sent: 111942.523404513 Recv: 111947.617490891 Opcode: IMG_BLUR        OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[127]: Sent: 111942.535642138 Recv: 111947.879101391 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[128]: Sent: 111942.540716846 Recv: 111948.142718474 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[129]: Sent: 111942.663820222 Recv: 111948.391890724 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[130]: Sent: 111942.864270097 Recv: 111948.475699016 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[131]: Sent: 111942.912602097 Recv: 111948.494597599 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No HASH: 60a1e239cb4ca19a0edb461e80133d15
[#CLIENT#] R[132]: Sent: 111943.078249763 Recv: 111948.560446433 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[133]: Sent: 111943.083809847 Recv: 111943.137359513 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 14   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[134]: Sent: 111943.255123013 Recv: 111948.602943974 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[135]: Sent: 111943.351996014 Recv: 111948.609948933 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[136]: Sent: 111943.442464055 Recv: 111948.701210474 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[137]: Sent: 111943.662116055 Recv: 111948.707931433 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[138]: Sent: 111943.756275722 Recv: 111948.971079141 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[139]: Sent: 111943.846998097 Recv: 111943.901550097 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 15   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[140]: Sent: 111943.908823347 Recv: 111949.220631308 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[141]: Sent: 111943.927443139 Recv: 111949.470598475 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[142]: Sent: 111944.102807472 Recv: 111949.524108350 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No HASH: 07713d772d0b67e8304db40f99efce2f
[#CLIENT#] R[143]: Sent: 111944.313470306 Recv: 111949.643647808 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[144]: Sent: 111944.421167431 Recv: 111949.644399308 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[145]: Sent: 111944.571848139 Recv: 111950.135168600 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[146]: Sent: 111944.698764223 Recv: 111950.189415725 Opcode: IMG_BLUR        OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[147]: Sent: 111944.793593473 Recv: 111950.208128892 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No HASH: ac3c20fe392ffe1675d760e0acc0325d
[#CLIENT#] R[148]: Sent: 111944.946071473 Recv: 111950.208139808 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[149]: Sent: 111944.997418598 Recv: 111950.360285725 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[150]: Sent: 111945.023756431 Recv: 111950.447052392 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[151]: Sent: 111945.040614306 Recv: 111950.472074517 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[152]: Sent: 111945.088486848 Recv: 111950.626655684 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[153]: Sent: 111945.222237014 Recv: 111951.157035059 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[154]: Sent: 111945.302642889 Recv: 111951.277324309 Opcode: IMG_BLUR        OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[155]: Sent: 111945.468655806 Recv: 111951.763367226 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[156]: Sent: 111945.572544265 Recv: 111951.868920309 Opcode: IMG_BLUR        OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[157]: Sent: 111945.758360556 Recv: 111951.927301268 Opcode: IMG_BLUR        OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[158]: Sent: 111945.831523515 Recv: 111952.414669101 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[159]: Sent: 111945.958488098 Recv: 111952.676977310 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[160]: Sent: 111945.975117306 Recv: 111953.146860727 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[161]: Sent: 111946.090903807 Recv: 111953.230727310 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[162]: Sent: 111946.211451182 Recv: 111953.529862435 Opcode: IMG_BLUR        OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[163]: Sent: 111946.212064015 Recv: 111946.264621723 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 16   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[164]: Sent: 111946.371158348 Recv: 111953.779796977 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[165]: Sent: 111946.412952848 Recv: 111946.431095973 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 17   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[166]: Sent: 111946.537035973 Recv: 111953.951804935 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[167]: Sent: 111946.557687057 Recv: 111954.114942519 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[168]: Sent: 111946.734309015 Recv: 111954.198757060 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[169]: Sent: 111946.755602015 Recv: 111954.217461144 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No HASH: 2b87ba29a04361673e6c89b35bde43d4
[#CLIENT#] R[170]: Sent: 111946.958884307 Recv: 111954.685790394 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[171]: Sent: 111947.228557432 Recv: 111954.772496769 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[172]: Sent: 111947.308808890 Recv: 111954.856175394 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[173]: Sent: 111947.389281474 Recv: 111954.882619436 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[174]: Sent: 111947.557602432 Recv: 111954.990750227 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No HASH: a70bdc3cdf2b54142b30883214c9c99c
[#CLIENT#] R[175]: Sent: 111948.093709057 Recv: 111948.112287057 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 18   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[176]: Sent: 111948.319635183 Recv: 111954.990759102 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[177]: Sent: 111948.462175683 Recv: 111955.032730311 Opcode: IMG_BLUR        OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[178]: Sent: 111948.494604516 Recv: 111955.138403769 Opcode: IMG_BLUR        OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[179]: Sent: 111948.512904058 Recv: 111955.181530228 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[180]: Sent: 111948.719315016 Recv: 111955.199862353 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No HASH: 18743a90a1c8b73697150fda5f9497ce
[#CLIENT#] R[181]: Sent: 111948.814046724 Recv: 111955.302452894 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No HASH: 13498c3ae65af1245b92c44175fe9e20
[#CLIENT#] R[182]: Sent: 111948.891428391 Recv: 111955.302472061 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[183]: Sent: 111948.894822350 Recv: 111948.912509058 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 19   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[184]: Sent: 111949.091263058 Recv: 111955.547278478 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[185]: Sent: 111949.158603558 Recv: 111955.566262186 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No HASH: fe98aaa171a54ea15946e81aba274db1
[#CLIENT#] R[186]: Sent: 111949.327027725 Recv: 111955.584870978 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No HASH: 18743a90a1c8b73697150fda5f9497ce
[#CLIENT#] R[187]: Sent: 111949.387250766 Recv: 111955.798207394 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[188]: Sent: 111949.415664350 Recv: 111955.854673103 Opcode: IMG_BLUR        OW: 1 ClientImgID: 17   ServerImgID: 17   Rejected: No
[#CLIENT#] R[189]: Sent: 111949.542150850 Recv: 111949.643643308 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 20   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[190]: Sent: 111949.731062183 Recv: 111949.836415517 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 21   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[191]: Sent: 111950.369620309 Recv: 111956.325219936 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[192]: Sent: 111950.472042225 Recv: 111956.481693770 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[193]: Sent: 111950.496906725 Recv: 111956.565677728 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[194]: Sent: 111950.630867934 Recv: 111956.584720478 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[195]: Sent: 111950.821025934 Recv: 111956.603221437 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 17   ServerImgID: 17   Rejected: No HASH: 1d58d784c91555c8541eca0755b4bb5a
[#CLIENT#] R[196]: Sent: 111951.050423851 Recv: 111951.157029351 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 22   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[197]: Sent: 111951.233920642 Recv: 111956.621094478 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No HASH: d0786a5de39ca03211ddc5c71ef9d5da
[#CLIENT#] R[198]: Sent: 111951.533235601 Recv: 111956.658270687 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[199]: Sent: 111951.875275643 Recv: 111951.927278934 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 23   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[200]: Sent: 111952.078815893 Recv: 111956.741592020 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[201]: Sent: 111952.108665768 Recv: 111956.760198020 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 17   ServerImgID: 17   Rejected: No HASH: 1d58d784c91555c8541eca0755b4bb5a
[#CLIENT#] R[202]: Sent: 111952.149033434 Recv: 111956.991579603 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[203]: Sent: 111952.229917309 Recv: 111957.049462437 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No HASH: dbc5cfa2ed2144a04653f8fe75f6fb2e
[#CLIENT#] R[204]: Sent: 111952.294960684 Recv: 111957.104583603 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No HASH: 83af9aa159e73eca99768998d53faa35
[#CLIENT#] R[205]: Sent: 111952.543317601 Recv: 111957.104590687 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 17   ServerImgID: 17   Rejected: No
[#CLIENT#] R[206]: Sent: 111952.743951143 Recv: 111957.122479937 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No HASH: d0786a5de39ca03211ddc5c71ef9d5da
[#CLIENT#] R[207]: Sent: 111952.766187976 Recv: 111957.140333978 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No HASH: 9501a7ff4534a1193b3fc6fa69efaad3
[#CLIENT#] R[208]: Sent: 111952.879093393 Recv: 111957.140348895 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[209]: Sent: 111952.961426560 Recv: 111953.067537143 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 24   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[210]: Sent: 111953.069450268 Recv: 111957.178765603 Opcode: IMG_BLUR        OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[211]: Sent: 111953.326828435 Recv: 111957.351726604 Opcode: IMG_BLUR        OW: 1 ClientImgID: 16   ServerImgID: 16   Rejected: No
[#CLIENT#] R[212]: Sent: 111953.545102685 Recv: 111957.602816937 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[213]: Sent: 111953.604566685 Recv: 111957.686880104 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[214]: Sent: 111953.706500018 Recv: 111958.155077229 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 21   ServerImgID: 21   Rejected: No
[#CLIENT#] R[215]: Sent: 111953.741203477 Recv: 111958.328064937 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[216]: Sent: 111953.970931810 Recv: 111958.354666896 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[217]: Sent: 111954.002848644 Recv: 111958.438744396 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[218]: Sent: 111954.217477769 Recv: 111958.459561271 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[219]: Sent: 111954.475947269 Recv: 111958.946170063 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[220]: Sent: 111954.494298977 Recv: 111958.954159146 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[221]: Sent: 111954.513724561 Recv: 111958.961567146 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No
[#CLIENT#] R[222]: Sent: 111954.807385936 Recv: 111959.260272604 Opcode: IMG_BLUR        OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[223]: Sent: 111954.820225311 Recv: 111959.349119646 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[224]: Sent: 111955.067074686 Recv: 111959.367841063 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No HASH: 56dce5d5ef77a4d1b70bb5f0ede39c26
[#CLIENT#] R[225]: Sent: 111955.074461269 Recv: 111959.423094813 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No HASH: 9559d5665fccb0cf0ca4a5cb2425a4e9
[#CLIENT#] R[226]: Sent: 111955.131871436 Recv: 111959.423157896 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No
[#CLIENT#] R[227]: Sent: 111955.375411228 Recv: 111959.820310938 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 22   ServerImgID: 22   Rejected: No
[#CLIENT#] R[228]: Sent: 111955.378997603 Recv: 111959.828383730 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[229]: Sent: 111955.519033519 Recv: 111959.836377146 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[230]: Sent: 111955.522710519 Recv: 111960.400344813 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[231]: Sent: 111955.631213061 Recv: 111960.400349105 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[232]: Sent: 111955.851429061 Recv: 111960.516934647 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[233]: Sent: 111955.856624770 Recv: 111960.600768230 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[234]: Sent: 111955.976630895 Recv: 111961.067066939 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[235]: Sent: 111956.014203895 Recv: 111961.169769147 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 21   ServerImgID: 21   Rejected: No HASH: 22286fe7eb8d021fb7fb11f7614799bf
[#CLIENT#] R[236]: Sent: 111956.179985436 Recv: 111961.169777230 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 16   ServerImgID: 16   Rejected: No
[#CLIENT#] R[237]: Sent: 111956.185521686 Recv: 111956.238124145 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 25   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[238]: Sent: 111956.266122853 Recv: 111961.169788189 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[239]: Sent: 111956.272168811 Recv: 111961.185157772 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[240]: Sent: 111956.277959228 Recv: 111961.294361939 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[241]: Sent: 111956.307678686 Recv: 111956.325212603 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 26   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[242]: Sent: 111956.412996853 Recv: 111961.435058939 Opcode: IMG_BLUR        OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[243]: Sent: 111956.673506228 Recv: 111961.523364856 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[244]: Sent: 111956.804263853 Recv: 111961.570036356 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 22   ServerImgID: 22   Rejected: No
[#CLIENT#] R[245]: Sent: 111956.904724353 Recv: 111962.057920939 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[246]: Sent: 111957.172894520 Recv: 111962.144569814 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[247]: Sent: 111957.246882062 Recv: 111957.351715479 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 27   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[248]: Sent: 111957.465646062 Recv: 111962.235591898 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No
[#CLIENT#] R[249]: Sent: 111957.497017395 Recv: 111962.535330356 Opcode: IMG_BLUR        OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[250]: Sent: 111957.521183270 Recv: 111962.998576065 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[251]: Sent: 111957.636279520 Recv: 111963.461686398 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 22   ServerImgID: 22   Rejected: No
[#CLIENT#] R[252]: Sent: 111957.827674895 Recv: 111963.553930773 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No
[#CLIENT#] R[253]: Sent: 111957.937977854 Recv: 111963.639124190 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[254]: Sent: 111957.966821729 Recv: 111963.658443482 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No HASH: 56dce5d5ef77a4d1b70bb5f0ede39c26
[#CLIENT#] R[255]: Sent: 111958.039118812 Recv: 111963.902893357 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[256]: Sent: 111958.114901729 Recv: 111963.993128107 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[257]: Sent: 111958.248408729 Recv: 111964.011701065 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No HASH: 98b9ed3ea6eae02e2969162cccbd71f7
[#CLIENT#] R[258]: Sent: 111958.252935729 Recv: 111964.489174065 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 22   ServerImgID: 22   Rejected: No
[#CLIENT#] R[259]: Sent: 111958.319786437 Recv: 111964.651661232 Opcode: IMG_BLUR        OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[260]: Sent: 111958.491435187 Recv: 111964.690779815 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[261]: Sent: 111958.499650437 Recv: 111964.952665566 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 16   ServerImgID: 16   Rejected: No
[#CLIENT#] R[262]: Sent: 111958.756581063 Recv: 111965.036547316 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[263]: Sent: 111958.784711521 Recv: 111965.335356357 Opcode: IMG_BLUR        OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[264]: Sent: 111958.794488688 Recv: 111958.828711188 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 28   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[265]: Sent: 111958.846884396 Recv: 111965.389897232 Opcode: IMG_BLUR        OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[266]: Sent: 111958.997239771 Recv: 111965.495037607 Opcode: IMG_BLUR        OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[267]: Sent: 111959.130652438 Recv: 111965.513611399 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No HASH: 6eea4bd5c0b7ead532c334eea7ccd250
[#CLIENT#] R[268]: Sent: 111959.140877146 Recv: 111965.581860524 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[269]: Sent: 111959.151645188 Recv: 111965.637870399 Opcode: IMG_BLUR        OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[270]: Sent: 111959.317626604 Recv: 111965.724913441 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No
[#CLIENT#] R[271]: Sent: 111959.423109396 Recv: 111965.831302608 Opcode: IMG_BLUR        OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[272]: Sent: 111959.566251271 Recv: 111959.676035146 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 29   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[273]: Sent: 111959.862663646 Recv: 111965.870320358 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[274]: Sent: 111959.923788480 Recv: 111959.975607855 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 30   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[275]: Sent: 111960.014734605 Recv: 111966.120113399 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[276]: Sent: 111960.023274355 Recv: 111966.419438441 Opcode: IMG_BLUR        OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[277]: Sent: 111960.131154355 Recv: 111966.555011316 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 29   ServerImgID: 29   Rejected: No
[#CLIENT#] R[278]: Sent: 111960.218551438 Recv: 111966.923915316 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 29   ServerImgID: 29   Rejected: No
[#CLIENT#] R[279]: Sent: 111960.293909188 Recv: 111960.400340438 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 31   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[280]: Sent: 111960.546539147 Recv: 111967.095658733 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[281]: Sent: 111960.618955730 Recv: 111967.390496025 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[282]: Sent: 111960.679275938 Recv: 111960.784296855 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 32   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[283]: Sent: 111960.841177314 Recv: 111967.402295150 Opcode: IMG_BLUR        OW: 1 ClientImgID: 26   ServerImgID: 26   Rejected: No
[#CLIENT#] R[284]: Sent: 111960.854734689 Recv: 111967.486281942 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[285]: Sent: 111961.006292605 Recv: 111967.955908441 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 22   ServerImgID: 22   Rejected: No
[#CLIENT#] R[286]: Sent: 111961.247391855 Recv: 111968.418700775 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[287]: Sent: 111961.252278230 Recv: 111961.269973439 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 33   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[288]: Sent: 111961.532906897 Recv: 111968.472051442 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 25   ServerImgID: 25   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[289]: Sent: 111961.623623314 Recv: 111968.472058400 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 33   ServerImgID: 33   Rejected: No
[#CLIENT#] R[290]: Sent: 111961.701186856 Recv: 111968.515488067 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[291]: Sent: 111961.787431439 Recv: 111968.569757733 Opcode: IMG_BLUR        OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[292]: Sent: 111961.943185647 Recv: 111968.587767108 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 33   ServerImgID: 33   Rejected: No HASH: a46fa185b469892706544a2d486bf142
[#CLIENT#] R[293]: Sent: 111961.953537981 Recv: 111961.988246939 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 34   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[294]: Sent: 111962.125706397 Recv: 111969.031957442 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No
[#CLIENT#] R[295]: Sent: 111962.303879231 Recv: 111969.071870067 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 21   ServerImgID: 21   Rejected: No
[#CLIENT#] R[296]: Sent: 111962.376545606 Recv: 111969.535701067 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[297]: Sent: 111962.463057148 Recv: 111969.554097442 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 17   ServerImgID: 17   Rejected: No HASH: 87504e6eb7330f31ab17020c33a18aa9
[#CLIENT#] R[298]: Sent: 111962.604139064 Recv: 111969.659819775 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[299]: Sent: 111962.619792523 Recv: 111969.819674317 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[300]: Sent: 111962.805840689 Recv: 111970.120853317 Opcode: IMG_BLUR        OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No
[#CLIENT#] R[301]: Sent: 111962.915777231 Recv: 111970.204646359 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[302]: Sent: 111963.135144523 Recv: 111970.668259526 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No
[#CLIENT#] R[303]: Sent: 111963.166719648 Recv: 111970.709039318 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[304]: Sent: 111963.273947731 Recv: 111970.709044026 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 28   ServerImgID: 28   Rejected: No
[#CLIENT#] R[305]: Sent: 111963.344702981 Recv: 111970.761653859 Opcode: IMG_BLUR        OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[306]: Sent: 111963.360076940 Recv: 111971.011096234 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[307]: Sent: 111963.463546315 Recv: 111963.481637398 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 35   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[308]: Sent: 111963.593731148 Recv: 111971.097506568 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[309]: Sent: 111963.761438065 Recv: 111963.795418565 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 36   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[310]: Sent: 111963.884690482 Recv: 111963.902885523 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 37   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[311]: Sent: 111964.051795398 Recv: 111971.259976360 Opcode: IMG_BLUR        OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[312]: Sent: 111964.263893065 Recv: 111971.522681193 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[313]: Sent: 111964.308539940 Recv: 111971.628686110 Opcode: IMG_BLUR        OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[314]: Sent: 111964.412885274 Recv: 111971.933618777 Opcode: IMG_BLUR        OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[315]: Sent: 111964.616579399 Recv: 111972.397010443 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[316]: Sent: 111964.780557690 Recv: 111972.860144777 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 29   ServerImgID: 29   Rejected: No
[#CLIENT#] R[317]: Sent: 111964.826317524 Recv: 111964.844201357 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 38   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[318]: Sent: 111964.935698315 Recv: 111972.898889819 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[319]: Sent: 111964.992376816 Recv: 111973.004694985 Opcode: IMG_BLUR        OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[320]: Sent: 111965.054173732 Recv: 111973.125026110 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[321]: Sent: 111965.079649899 Recv: 111973.555370777 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No
[#CLIENT#] R[322]: Sent: 111965.115529566 Recv: 111973.639825986 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 35   ServerImgID: 35   Rejected: No
[#CLIENT#] R[323]: Sent: 111965.181012107 Recv: 111973.723650777 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[324]: Sent: 111965.376856941 Recv: 111973.775560527 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 28   ServerImgID: 28   Rejected: No
[#CLIENT#] R[325]: Sent: 111965.397299649 Recv: 111973.825208361 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 38   ServerImgID: 38   Rejected: No
[#CLIENT#] R[326]: Sent: 111965.431406274 Recv: 111973.850911319 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[327]: Sent: 111965.547753899 Recv: 111974.113477028 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 23   ServerImgID: 23   Rejected: No
[#CLIENT#] R[328]: Sent: 111965.868984649 Recv: 111974.120309819 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[329]: Sent: 111966.066617524 Recv: 111966.084571108 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 39   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[330]: Sent: 111966.161350649 Recv: 111974.204614236 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[331]: Sent: 111966.337746399 Recv: 111974.211819444 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No
[#CLIENT#] R[332]: Sent: 111966.389760525 Recv: 111974.314589319 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No HASH: 443973423be9f977eba85b1a8c0f41a9
[#CLIENT#] R[333]: Sent: 111966.406614233 Recv: 111974.314598861 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[334]: Sent: 111966.449314525 Recv: 111966.554999566 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 40   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[335]: Sent: 111966.657299900 Recv: 111974.342049528 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 17   ServerImgID: 17   Rejected: No
[#CLIENT#] R[336]: Sent: 111966.735271941 Recv: 111974.352146528 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 27   ServerImgID: 27   Rejected: No
[#CLIENT#] R[337]: Sent: 111966.756587233 Recv: 111974.454406403 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No HASH: 15cbf08ec384eb4822b847c3b349f691
[#CLIENT#] R[338]: Sent: 111966.783580608 Recv: 111974.518711444 Opcode: IMG_BLUR        OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[339]: Sent: 111966.826587233 Recv: 111974.602459069 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 26   ServerImgID: 26   Rejected: No
[#CLIENT#] R[340]: Sent: 111966.868748316 Recv: 111974.851755736 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 16   ServerImgID: 16   Rejected: No
[#CLIENT#] R[341]: Sent: 111967.034569483 Recv: 111967.052930775 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 41   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[342]: Sent: 111967.126593067 Recv: 111967.179035233 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 42   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[343]: Sent: 111967.223473233 Recv: 111974.935771695 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[344]: Sent: 111967.338456858 Recv: 111967.390491108 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 43   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[345]: Sent: 111967.405612650 Recv: 111975.406553487 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[346]: Sent: 111967.497405983 Recv: 111975.460501112 Opcode: IMG_BLUR        OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[347]: Sent: 111967.700803525 Recv: 111967.718317608 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 44   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[348]: Sent: 111967.755891816 Recv: 111975.923912570 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 22   ServerImgID: 22   Rejected: No
[#CLIENT#] R[349]: Sent: 111967.831950316 Recv: 111976.026502237 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No HASH: 09265369a030e219fcd2d80a99ded564
[#CLIENT#] R[350]: Sent: 111968.150829900 Recv: 111976.026510278 Opcode: IMG_BLUR        OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[351]: Sent: 111968.156358691 Recv: 111968.262844066 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 45   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[352]: Sent: 111968.266910400 Recv: 111976.282326820 Opcode: IMG_BLUR        OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[353]: Sent: 111968.291785691 Recv: 111968.396431858 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 46   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[354]: Sent: 111968.404077942 Recv: 111976.768831737 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No
[#CLIENT#] R[355]: Sent: 111968.472066358 Recv: 111976.940726279 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[356]: Sent: 111968.554957442 Recv: 111977.047348154 Opcode: IMG_BLUR        OW: 1 ClientImgID: 34   ServerImgID: 34   Rejected: No
[#CLIENT#] R[357]: Sent: 111968.666651650 Recv: 111977.136225987 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[358]: Sent: 111968.731208150 Recv: 111968.749395775 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 47   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[359]: Sent: 111969.016578525 Recv: 111977.386007321 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 25   ServerImgID: 25   Rejected: No
[#CLIENT#] R[360]: Sent: 111969.247866900 Recv: 111977.404183487 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No HASH: 17f53b44873a51687c7b7eb59caa78d4
[#CLIENT#] R[361]: Sent: 111969.502305484 Recv: 111977.473296113 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No
[#CLIENT#] R[362]: Sent: 111969.674390192 Recv: 111977.490817988 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No HASH: e86ac01aa209232d9ecce0271f9ce47b
[#CLIENT#] R[363]: Sent: 111969.674899109 Recv: 111977.593572363 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No HASH: 2dd00aef69f7247958b4025a2a00fe32
[#CLIENT#] R[364]: Sent: 111969.773717275 Recv: 111977.593581571 Opcode: IMG_BLUR        OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No
[#CLIENT#] R[365]: Sent: 111969.777472109 Recv: 111977.850444446 Opcode: IMG_BLUR        OW: 1 ClientImgID: 21   ServerImgID: 21   Rejected: No
[#CLIENT#] R[366]: Sent: 111969.983123901 Recv: 111977.868374613 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No HASH: e86ac01aa209232d9ecce0271f9ce47b
[#CLIENT#] R[367]: Sent: 111970.095646192 Recv: 111970.113981692 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 48   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[368]: Sent: 111970.215560901 Recv: 111977.896753029 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[369]: Sent: 111970.768801776 Recv: 111970.802769443 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 49   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[370]: Sent: 111970.813229901 Recv: 111978.386322905 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No
[#CLIENT#] R[371]: Sent: 111970.847695151 Recv: 111978.386332280 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 23   ServerImgID: 23   Rejected: No
[#CLIENT#] R[372]: Sent: 111970.895664318 Recv: 111978.488722946 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No HASH: 8aedd77e65db0bdf11484030beb7f7d2
[#CLIENT#] R[373]: Sent: 111971.116035193 Recv: 111978.636454696 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 42   ServerImgID: 42   Rejected: No
[#CLIENT#] R[374]: Sent: 111971.135526443 Recv: 111978.724910071 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[375]: Sent: 111971.395103068 Recv: 111978.813928113 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[376]: Sent: 111971.427439235 Recv: 111978.832241988 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 26   ServerImgID: 26   Rejected: No HASH: 9d73e97ac536ed43ec67b869dac562a7
[#CLIENT#] R[377]: Sent: 111971.603868526 Recv: 111978.902978738 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 33   ServerImgID: 33   Rejected: No
[#CLIENT#] R[378]: Sent: 111971.664185110 Recv: 111978.989560322 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[379]: Sent: 111971.726090735 Recv: 111971.744059360 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 50   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[380]: Sent: 111971.792943776 Recv: 111979.045606238 Opcode: IMG_BLUR        OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No
[#CLIENT#] R[381]: Sent: 111971.813780901 Recv: 111979.085456447 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[382]: Sent: 111972.063188652 Recv: 111979.104113988 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No HASH: 2ec8a864904a738fd306d50b3cd3cf7e
[#CLIENT#] R[383]: Sent: 111972.158830152 Recv: 111972.211235152 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 51   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[384]: Sent: 111972.280933610 Recv: 111979.104127905 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 17   ServerImgID: 17   Rejected: No
[#CLIENT#] R[385]: Sent: 111972.386011777 Recv: 111979.122026863 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 33   ServerImgID: 33   Rejected: No HASH: 0ca2b17283ae8bada714cf75628b9380
[#CLIENT#] R[386]: Sent: 111972.459466777 Recv: 111979.147669655 Opcode: IMG_BLUR        OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[387]: Sent: 111972.572033652 Recv: 111979.610210155 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[388]: Sent: 111972.727323152 Recv: 111979.618282489 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 33   ServerImgID: 33   Rejected: No
[#CLIENT#] R[389]: Sent: 111972.768020319 Recv: 111980.107461030 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[390]: Sent: 111972.795974985 Recv: 111980.145068905 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No HASH: 94cf2cdf5b2100fc3b24dff8d66c2ed5
[#CLIENT#] R[391]: Sent: 111972.850129069 Recv: 111980.192307114 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[392]: Sent: 111973.000633319 Recv: 111980.677107531 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[393]: Sent: 111973.016355777 Recv: 111980.840199447 Opcode: IMG_BLUR        OW: 1 ClientImgID: 43   ServerImgID: 43   Rejected: No
[#CLIENT#] R[394]: Sent: 111973.090582527 Recv: 111973.132041194 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 52   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[395]: Sent: 111973.203087235 Recv: 111980.924178531 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[396]: Sent: 111973.229981652 Recv: 111981.030304531 Opcode: IMG_BLUR        OW: 1 ClientImgID: 34   ServerImgID: 34   Rejected: No
[#CLIENT#] R[397]: Sent: 111973.294795152 Recv: 111981.493357239 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 40   ServerImgID: 40   Rejected: No
[#CLIENT#] R[398]: Sent: 111973.578284986 Recv: 111981.956750115 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 40   ServerImgID: 40   Rejected: No
[#CLIENT#] R[399]: Sent: 111973.609324861 Recv: 111982.255588406 Opcode: IMG_BLUR        OW: 1 ClientImgID: 22   ServerImgID: 22   Rejected: No
[#CLIENT#] R[400]: Sent: 111973.668864402 Recv: 111982.310770240 Opcode: IMG_BLUR        OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[401]: Sent: 111973.757223152 Recv: 111973.775571486 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 53   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[402]: Sent: 111974.132501861 Recv: 111982.329529406 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No HASH: 63462aae85d7bb2238584f421e5321b0
[#CLIENT#] R[403]: Sent: 111974.552386153 Recv: 111982.636539532 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 51   ServerImgID: 51   Rejected: No
[#CLIENT#] R[404]: Sent: 111974.624906028 Recv: 111974.677335653 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 54   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[405]: Sent: 111974.812052403 Recv: 111982.723979365 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 49   ServerImgID: 49   Rejected: No
[#CLIENT#] R[406]: Sent: 111974.899901820 Recv: 111982.885268823 Opcode: IMG_BLUR        OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[407]: Sent: 111974.939063528 Recv: 111982.969095948 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 38   ServerImgID: 38   Rejected: No
[#CLIENT#] R[408]: Sent: 111975.093860320 Recv: 111983.006200365 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[409]: Sent: 111975.149642861 Recv: 111983.153063240 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 49   ServerImgID: 49   Rejected: No
[#CLIENT#] R[410]: Sent: 111975.271858820 Recv: 111983.237315282 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 39   ServerImgID: 39   Rejected: No
[#CLIENT#] R[411]: Sent: 111975.272684570 Recv: 111983.283034657 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No
[#CLIENT#] R[412]: Sent: 111975.346686028 Recv: 111983.385417699 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 40   ServerImgID: 40   Rejected: No HASH: c805a881624da3f0e7f8f6fc6f74044a
[#CLIENT#] R[413]: Sent: 111975.365022695 Recv: 111983.385431699 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 26   ServerImgID: 26   Rejected: No
[#CLIENT#] R[414]: Sent: 111975.446448612 Recv: 111983.458908407 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No
[#CLIENT#] R[415]: Sent: 111975.468010570 Recv: 111983.561975740 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No HASH: d2c3d5995b9441fdf8a21ca59f5bfb21
[#CLIENT#] R[416]: Sent: 111975.597984195 Recv: 111983.726561115 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 42   ServerImgID: 42   Rejected: No
[#CLIENT#] R[417]: Sent: 111975.711403403 Recv: 111984.193788657 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 29   ServerImgID: 29   Rejected: No
[#CLIENT#] R[418]: Sent: 111975.839296570 Recv: 111975.890968028 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 55   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[419]: Sent: 111976.994739404 Recv: 111984.233549324 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[420]: Sent: 111977.148270737 Recv: 111977.255199696 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 56   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[421]: Sent: 111977.303273487 Recv: 111984.395071199 Opcode: IMG_BLUR        OW: 1 ClientImgID: 23   ServerImgID: 23   Rejected: No
[#CLIENT#] R[422]: Sent: 111977.593590113 Recv: 111984.449778241 Opcode: IMG_BLUR        OW: 1 ClientImgID: 35   ServerImgID: 35   Rejected: No
[#CLIENT#] R[423]: Sent: 111977.992405696 Recv: 111984.913557616 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[424]: Sent: 111978.229945363 Recv: 111978.264386405 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 57   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[425]: Sent: 111978.281254196 Recv: 111978.386251696 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 58   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[426]: Sent: 111978.488739238 Recv: 111985.085017574 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 52   ServerImgID: 52   Rejected: No
[#CLIENT#] R[427]: Sent: 111978.553970321 Recv: 111985.139251658 Opcode: IMG_BLUR        OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[428]: Sent: 111978.585072321 Recv: 111985.152550449 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 52   ServerImgID: 52   Rejected: No
[#CLIENT#] R[429]: Sent: 111978.670241613 Recv: 111985.661067658 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[430]: Sent: 111978.779133363 Recv: 111985.865846867 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 43   ServerImgID: 43   Rejected: No
[#CLIENT#] R[431]: Sent: 111979.205682613 Recv: 111986.358233283 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[432]: Sent: 111979.219399072 Recv: 111986.393583492 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 36   ServerImgID: 36   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[433]: Sent: 111979.225659905 Recv: 111986.608979200 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[434]: Sent: 111979.372283613 Recv: 111986.643122617 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 36   ServerImgID: 36   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[435]: Sent: 111979.518986447 Recv: 111986.744322117 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No HASH: 265c37ce11140c300e85e1d7606634c6
[#CLIENT#] R[436]: Sent: 111979.680450822 Recv: 111979.698437947 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 59   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[437]: Sent: 111979.757919364 Recv: 111979.792144280 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 60   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[438]: Sent: 111979.795763822 Recv: 111986.744328867 Opcode: IMG_BLUR        OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No
[#CLIENT#] R[439]: Sent: 111979.838816447 Recv: 111986.744367325 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[440]: Sent: 111980.009125780 Recv: 111986.794346659 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[441]: Sent: 111980.024908197 Recv: 111986.880913450 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[442]: Sent: 111980.066550489 Recv: 111986.899115325 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 33   ServerImgID: 33   Rejected: No HASH: 8424c5f06ec75b6d7be01c9662dba8cc
[#CLIENT#] R[443]: Sent: 111980.326057989 Recv: 111986.972393534 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[444]: Sent: 111980.333118614 Recv: 111987.061199950 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[445]: Sent: 111980.372336989 Recv: 111987.524435951 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 22   ServerImgID: 22   Rejected: No
[#CLIENT#] R[446]: Sent: 111980.591639489 Recv: 111987.544834826 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 25   ServerImgID: 25   Rejected: No
[#CLIENT#] R[447]: Sent: 111980.658599781 Recv: 111987.631240159 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No
[#CLIENT#] R[448]: Sent: 111980.819690697 Recv: 111988.094087284 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No
[#CLIENT#] R[449]: Sent: 111980.899016989 Recv: 111988.113044951 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No HASH: 99904a9a04062db3ec5b5af7eda23f71
[#CLIENT#] R[450]: Sent: 111980.946045197 Recv: 111988.558688701 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 56   ServerImgID: 56   Rejected: No
[#CLIENT#] R[451]: Sent: 111980.953063364 Recv: 111980.970706656 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 61   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[452]: Sent: 111980.971360364 Recv: 111988.858549576 Opcode: IMG_BLUR        OW: 1 ClientImgID: 21   ServerImgID: 21   Rejected: No
[#CLIENT#] R[453]: Sent: 111980.976186989 Recv: 111988.945130410 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No
[#CLIENT#] R[454]: Sent: 111980.994738156 Recv: 111988.984422868 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[455]: Sent: 111981.027800739 Recv: 111989.446856660 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No
[#CLIENT#] R[456]: Sent: 111981.105089489 Recv: 111989.696323077 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 23   ServerImgID: 23   Rejected: No
[#CLIENT#] R[457]: Sent: 111981.128237364 Recv: 111989.784822327 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[458]: Sent: 111981.273059364 Recv: 111989.884882993 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 29   ServerImgID: 29   Rejected: No HASH: 93c6c71a0c9f784606e4a999406c05c6
[#CLIENT#] R[459]: Sent: 111981.338714614 Recv: 111989.884902160 Opcode: IMG_BLUR        OW: 1 ClientImgID: 50   ServerImgID: 50   Rejected: No
[#CLIENT#] R[460]: Sent: 111981.601888323 Recv: 111990.095709452 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 55   ServerImgID: 55   Rejected: No
[#CLIENT#] R[461]: Sent: 111981.748437948 Recv: 111990.109236535 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 57   ServerImgID: 57   Rejected: No
[#CLIENT#] R[462]: Sent: 111982.204026490 Recv: 111990.209456994 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No HASH: 769e766e455d7911c84b1647970036eb
[#CLIENT#] R[463]: Sent: 111982.330604031 Recv: 111990.363983660 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 42   ServerImgID: 42   Rejected: No
[#CLIENT#] R[464]: Sent: 111982.332068198 Recv: 111982.366434157 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 62   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[465]: Sent: 111982.470718323 Recv: 111990.404042077 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 54   ServerImgID: 54   Rejected: No
[#CLIENT#] R[466]: Sent: 111982.519775573 Recv: 111990.443807827 Opcode: IMG_BLUR        OW: 1 ClientImgID: 44   ServerImgID: 44   Rejected: No
[#CLIENT#] R[467]: Sent: 111982.523297907 Recv: 111990.451044785 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 59   ServerImgID: 59   Rejected: No
[#CLIENT#] R[468]: Sent: 111982.527051698 Recv: 111982.636534990 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 63   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[469]: Sent: 111982.692690282 Recv: 111990.752270494 Opcode: IMG_BLUR        OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[470]: Sent: 111982.775573865 Recv: 111991.068360286 Opcode: IMG_BLUR        OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No
[#CLIENT#] R[471]: Sent: 111982.805039448 Recv: 111991.086279702 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 39   ServerImgID: 39   Rejected: No HASH: d4f94469bfe2b5ed7246046002f99653
[#CLIENT#] R[472]: Sent: 111982.910109198 Recv: 111991.146113661 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 44   ServerImgID: 44   Rejected: No
[#CLIENT#] R[473]: Sent: 111982.919515198 Recv: 111991.603124536 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[474]: Sent: 111982.988441282 Recv: 111983.030059782 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 64   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[475]: Sent: 111983.385439657 Recv: 111983.419366699 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 65   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[476]: Sent: 111983.561991699 Recv: 111991.687185578 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 38   ServerImgID: 38   Rejected: No
[#CLIENT#] R[477]: Sent: 111983.725346949 Recv: 111992.173695620 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[478]: Sent: 111983.816265116 Recv: 111992.230323786 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 30   ServerImgID: 30   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[479]: Sent: 111984.077193532 Recv: 111984.095703116 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 66   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[480]: Sent: 111984.137167907 Recv: 111992.230332620 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[481]: Sent: 111984.161201657 Recv: 111992.480671370 Opcode: IMG_BLUR        OW: 1 ClientImgID: 40   ServerImgID: 40   Rejected: No
[#CLIENT#] R[482]: Sent: 111984.256189616 Recv: 111992.567408453 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[483]: Sent: 111984.335260574 Recv: 111992.655577495 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 39   ServerImgID: 39   Rejected: No
[#CLIENT#] R[484]: Sent: 111984.341391574 Recv: 111992.761293328 Opcode: IMG_BLUR        OW: 1 ClientImgID: 65   ServerImgID: 65   Rejected: No
[#CLIENT#] R[485]: Sent: 111984.380136157 Recv: 111992.869088578 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No HASH: 5fbf731145da02fb096ea1d97a956e1e
[#CLIENT#] R[486]: Sent: 111984.475177491 Recv: 111992.869096870 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 49   ServerImgID: 49   Rejected: No
[#CLIENT#] R[487]: Sent: 111984.539431366 Recv: 111992.956638828 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 52   ServerImgID: 52   Rejected: No
[#CLIENT#] R[488]: Sent: 111984.551018658 Recv: 111993.196620328 Opcode: IMG_BLUR        OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[489]: Sent: 111984.584450408 Recv: 111993.290328328 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No
[#CLIENT#] R[490]: Sent: 111984.649769991 Recv: 111993.310866453 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 42   ServerImgID: 42   Rejected: No
[#CLIENT#] R[491]: Sent: 111984.747547533 Recv: 111993.474041495 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 60   ServerImgID: 60   Rejected: No
[#CLIENT#] R[492]: Sent: 111984.814043158 Recv: 111993.943103870 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 21   ServerImgID: 21   Rejected: No
[#CLIENT#] R[493]: Sent: 111984.819677199 Recv: 111993.981754454 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 21   ServerImgID: 21   Rejected: No
[#CLIENT#] R[494]: Sent: 111984.824613908 Recv: 111994.035087329 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No HASH: 8ee92d5fe2cf8dcafc52abe575e551a9
[#CLIENT#] R[495]: Sent: 111984.890080241 Recv: 111994.246304121 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[496]: Sent: 111985.608540491 Recv: 111985.661060241 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 67   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[497]: Sent: 111986.148448492 Recv: 111994.261197454 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 65   ServerImgID: 65   Rejected: No
[#CLIENT#] R[498]: Sent: 111986.216658033 Recv: 111986.234979408 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 68   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[499]: Sent: 111986.312679700 Recv: 111986.347415283 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 69   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[500]: Sent: 111986.429755950 Recv: 111986.447796700 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 70   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[501]: Sent: 111986.460508658 Recv: 111994.422459121 Opcode: IMG_BLUR        OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[502]: Sent: 111986.524156617 Recv: 111994.463051621 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[503]: Sent: 111986.554913408 Recv: 111994.549206121 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 50   ServerImgID: 50   Rejected: No
[#CLIENT#] R[504]: Sent: 111986.744337242 Recv: 111995.013601413 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[505]: Sent: 111987.037780200 Recv: 111995.116449788 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No HASH: d7748f1a206eb62d36a79102083cf548
[#CLIENT#] R[506]: Sent: 111987.070148367 Recv: 111995.116459079 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 57   ServerImgID: 57   Rejected: No
[#CLIENT#] R[507]: Sent: 111987.109912784 Recv: 111987.128239075 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 71   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[508]: Sent: 111987.365236909 Recv: 111995.520241329 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 27   ServerImgID: 27   Rejected: No
[#CLIENT#] R[509]: Sent: 111987.459278867 Recv: 111995.533800829 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 36   ServerImgID: 36   Rejected: No
[#CLIENT#] R[510]: Sent: 111987.504283867 Recv: 111995.697176163 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 65   ServerImgID: 65   Rejected: No
[#CLIENT#] R[511]: Sent: 111987.574719367 Recv: 111996.159872080 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 45   ServerImgID: 45   Rejected: No
[#CLIENT#] R[512]: Sent: 111987.603797867 Recv: 111996.180281580 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[513]: Sent: 111987.628038576 Recv: 111996.200926621 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 16   ServerImgID: 16   Rejected: No
[#CLIENT#] R[514]: Sent: 111987.910836201 Recv: 111996.287798663 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 17   ServerImgID: 17   Rejected: No
[#CLIENT#] R[515]: Sent: 111987.977922076 Recv: 111996.451135163 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 28   ServerImgID: 28   Rejected: No
[#CLIENT#] R[516]: Sent: 111987.997670868 Recv: 111996.700268080 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[517]: Sent: 111988.113056034 Recv: 111996.735531538 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No HASH: 434ea3af0e2fce0af8833464e6fda832
[#CLIENT#] R[518]: Sent: 111988.149077534 Recv: 111996.755389330 Opcode: IMG_BLUR        OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[519]: Sent: 111988.187370534 Recv: 111996.839150705 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[520]: Sent: 111988.501213534 Recv: 111996.846259955 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[521]: Sent: 111988.620952659 Recv: 111996.948788913 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No HASH: 2f188c6767b30436ddf1bb7dddb39792
[#CLIENT#] R[522]: Sent: 111988.639036284 Recv: 111996.948797163 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 69   ServerImgID: 69   Rejected: No
[#CLIENT#] R[523]: Sent: 111988.824794993 Recv: 111996.948843705 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 30   ServerImgID: 30   Rejected: No
[#CLIENT#] R[524]: Sent: 111988.980245243 Recv: 111997.004489705 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 51   ServerImgID: 51   Rejected: No HASH: be2f2892be0a6d85742dab3365fb5d6a
[#CLIENT#] R[525]: Sent: 111988.985105535 Recv: 111997.004494580 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 21   ServerImgID: 21   Rejected: No
[#CLIENT#] R[526]: Sent: 111988.995544868 Recv: 111997.004498955 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No
[#CLIENT#] R[527]: Sent: 111989.283581951 Recv: 111989.301435910 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 72   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[528]: Sent: 111989.386828743 Recv: 111997.034378955 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[529]: Sent: 111989.452984785 Recv: 111997.283699039 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 51   ServerImgID: 51   Rejected: No
[#CLIENT#] R[530]: Sent: 111989.476935202 Recv: 111997.302446289 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 47   ServerImgID: 47   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[531]: Sent: 111989.515838243 Recv: 111997.375400247 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 66   ServerImgID: 66   Rejected: No
[#CLIENT#] R[532]: Sent: 111989.783749743 Recv: 111997.838306955 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 29   ServerImgID: 29   Rejected: No
[#CLIENT#] R[533]: Sent: 111989.884910285 Recv: 111997.931769371 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 53   ServerImgID: 53   Rejected: No
[#CLIENT#] R[534]: Sent: 111989.924495910 Recv: 111997.973927205 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[535]: Sent: 111990.268317994 Recv: 111998.321565663 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 51   ServerImgID: 51   Rejected: No
[#CLIENT#] R[536]: Sent: 111990.316468535 Recv: 111998.321572330 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 72   ServerImgID: 72   Rejected: No
[#CLIENT#] R[537]: Sent: 111990.502624410 Recv: 111998.340233330 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No HASH: 0d3d7d856df5680b1b6a63fd5b3314b5
[#CLIENT#] R[538]: Sent: 111990.617845077 Recv: 111998.393353205 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 51   ServerImgID: 51   Rejected: No HASH: 8e0e76c9075fd45334543ee2a3edaf7f
[#CLIENT#] R[539]: Sent: 111990.782048452 Recv: 111998.803085622 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 58   ServerImgID: 58   Rejected: No
[#CLIENT#] R[540]: Sent: 111990.954209244 Recv: 111999.064882413 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 43   ServerImgID: 43   Rejected: No
[#CLIENT#] R[541]: Sent: 111990.963739577 Recv: 111991.068355952 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 73   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[542]: Sent: 111991.086292952 Recv: 111999.151970664 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[543]: Sent: 111991.103788952 Recv: 111991.121368577 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 74   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[544]: Sent: 111991.177152661 Recv: 111999.190655372 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 66   ServerImgID: 66   Rejected: No
[#CLIENT#] R[545]: Sent: 111991.375939494 Recv: 111999.646957205 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 40   ServerImgID: 40   Rejected: No
[#CLIENT#] R[546]: Sent: 111991.684400578 Recv: 112000.108946664 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No
[#CLIENT#] R[547]: Sent: 111991.896998286 Recv: 112000.395706581 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 43   ServerImgID: 43   Rejected: No
[#CLIENT#] R[548]: Sent: 111991.928217119 Recv: 112000.621306789 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 55   ServerImgID: 55   Rejected: No
[#CLIENT#] R[549]: Sent: 111991.982282786 Recv: 112000.705574914 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[550]: Sent: 111992.086781786 Recv: 112000.724021831 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No HASH: 2534f3b4744ebd76878f4b516855f50e
[#CLIENT#] R[551]: Sent: 111992.334821661 Recv: 111992.386814620 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 75   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[552]: Sent: 111992.638756953 Recv: 112000.752791414 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 73   ServerImgID: 73   Rejected: No
[#CLIENT#] R[553]: Sent: 111992.869104995 Recv: 112000.759763123 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 72   ServerImgID: 72   Rejected: No
[#CLIENT#] R[554]: Sent: 111992.932695412 Recv: 112000.882122998 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 47   ServerImgID: 47   Rejected: No
[#CLIENT#] R[555]: Sent: 111993.037825287 Recv: 112001.314757331 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 63   ServerImgID: 63   Rejected: No
[#CLIENT#] R[556]: Sent: 111993.090624287 Recv: 111993.196615495 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 76   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[557]: Sent: 111993.384983578 Recv: 112001.422473915 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No HASH: bac05c6033777c730e76ff3b22f12369
[#CLIENT#] R[558]: Sent: 111993.623764287 Recv: 112001.788592540 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[559]: Sent: 111993.641813162 Recv: 112001.844884123 Opcode: IMG_BLUR        OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No
[#CLIENT#] R[560]: Sent: 111993.652547662 Recv: 112002.097734915 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 43   ServerImgID: 43   Rejected: No
[#CLIENT#] R[561]: Sent: 111993.919974370 Recv: 112002.269156165 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 34   ServerImgID: 34   Rejected: No
[#CLIENT#] R[562]: Sent: 111994.290459079 Recv: 112002.435347415 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 34   ServerImgID: 34   Rejected: No
[#CLIENT#] R[563]: Sent: 111994.308638371 Recv: 112002.685874874 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[564]: Sent: 111994.310087704 Recv: 112002.989873582 Opcode: IMG_BLUR        OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No
[#CLIENT#] R[565]: Sent: 111994.497286787 Recv: 112002.997819832 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 44   ServerImgID: 44   Rejected: No
[#CLIENT#] R[566]: Sent: 111994.596871871 Recv: 111994.614615621 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 77   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[567]: Sent: 111994.752656829 Recv: 112003.161236124 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 57   ServerImgID: 57   Rejected: No
[#CLIENT#] R[568]: Sent: 111994.757324579 Recv: 112003.263482665 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No HASH: bb2bb45c3407997b8d9e65123dc1b341
[#CLIENT#] R[569]: Sent: 111994.780131246 Recv: 112003.466645124 Opcode: IMG_BLUR        OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[570]: Sent: 111994.783264537 Recv: 112003.485040457 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No HASH: 09455cf5848b5aa244104a6b118f9bfb
[#CLIENT#] R[571]: Sent: 111994.825966454 Recv: 112003.628507666 Opcode: IMG_BLUR        OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[572]: Sent: 111994.853996662 Recv: 112003.792693374 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 60   ServerImgID: 60   Rejected: No
[#CLIENT#] R[573]: Sent: 111995.116468121 Recv: 112003.813062832 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 43   ServerImgID: 43   Rejected: No
[#CLIENT#] R[574]: Sent: 111995.151517038 Recv: 112003.900066749 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[575]: Sent: 111995.155416163 Recv: 111995.189319746 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 78   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[576]: Sent: 111995.456161371 Recv: 112003.908116207 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[577]: Sent: 111995.718926580 Recv: 111995.736923705 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 79   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[578]: Sent: 111995.977410080 Recv: 111996.029659788 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 80   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[579]: Sent: 111996.045241955 Recv: 112003.926650082 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 71   ServerImgID: 71   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[580]: Sent: 111996.050282955 Recv: 112003.926657374 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 52   ServerImgID: 52   Rejected: No
[#CLIENT#] R[581]: Sent: 111996.081975413 Recv: 112003.930112874 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[582]: Sent: 111996.212432580 Recv: 112003.948026166 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 26   ServerImgID: 26   Rejected: No HASH: 55348f8ec458faee8aef206c3daa6f14
[#CLIENT#] R[583]: Sent: 111996.253988538 Recv: 112004.019108291 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[584]: Sent: 111996.516622997 Recv: 112004.037236333 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No HASH: b52bf2575572cfd08cd9725b1ec1a230
[#CLIENT#] R[585]: Sent: 111996.845382497 Recv: 112004.507886166 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[586]: Sent: 111996.948804955 Recv: 112004.552300624 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No
[#CLIENT#] R[587]: Sent: 111997.081772664 Recv: 112004.636653958 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 64   ServerImgID: 64   Rejected: No
[#CLIENT#] R[588]: Sent: 111997.213102372 Recv: 112004.887224416 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 55   ServerImgID: 55   Rejected: No
[#CLIENT#] R[589]: Sent: 111997.675356039 Recv: 112005.136462541 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 54   ServerImgID: 54   Rejected: No
[#CLIENT#] R[590]: Sent: 111997.788687080 Recv: 112005.222848958 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 66   ServerImgID: 66   Rejected: No
[#CLIENT#] R[591]: Sent: 111998.014154330 Recv: 112005.236176125 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[592]: Sent: 111998.099361663 Recv: 112005.254206916 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 79   ServerImgID: 79   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[593]: Sent: 111998.215701955 Recv: 111998.321547246 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 81   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[594]: Sent: 111998.393373663 Recv: 112005.322834250 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No
[#CLIENT#] R[595]: Sent: 111998.526534205 Recv: 112005.573462583 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 51   ServerImgID: 51   Rejected: No
[#CLIENT#] R[596]: Sent: 111998.602107747 Recv: 112005.657718208 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 77   ServerImgID: 77   Rejected: No
[#CLIENT#] R[597]: Sent: 111998.656088497 Recv: 112005.746938375 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 61   ServerImgID: 61   Rejected: No
[#CLIENT#] R[598]: Sent: 111998.671762622 Recv: 111998.689555580 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 82   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[599]: Sent: 111998.831571580 Recv: 112005.802938750 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 75   ServerImgID: 75   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[600]: Sent: 111998.893596497 Recv: 112006.050973000 Opcode: IMG_BLUR        OW: 1 ClientImgID: 76   ServerImgID: 76   Rejected: No
[#CLIENT#] R[601]: Sent: 111998.927245622 Recv: 112006.222853667 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No
[#CLIENT#] R[602]: Sent: 111999.013209788 Recv: 112006.241391417 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 74   ServerImgID: 74   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[603]: Sent: 111999.099811289 Recv: 112006.390771250 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 28   ServerImgID: 28   Rejected: No
[#CLIENT#] R[604]: Sent: 111999.114143414 Recv: 112006.407697209 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 51   ServerImgID: 51   Rejected: No
[#CLIENT#] R[605]: Sent: 111999.190485247 Recv: 112006.515047334 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[606]: Sent: 111999.361475497 Recv: 112006.515059959 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 63   ServerImgID: 63   Rejected: No
[#CLIENT#] R[607]: Sent: 111999.612945247 Recv: 112006.954269792 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[608]: Sent: 111999.756786205 Recv: 111999.775273747 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 83   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[609]: Sent: 111999.805082331 Recv: 112006.972482876 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No HASH: b52bf2575572cfd08cd9725b1ec1a230
[#CLIENT#] R[610]: Sent: 111999.885094206 Recv: 112007.118844834 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 34   ServerImgID: 34   Rejected: No
[#CLIENT#] R[611]: Sent: 112000.001822539 Recv: 112007.137860584 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 70   ServerImgID: 70   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[612]: Sent: 112000.289550206 Recv: 112007.172646126 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No HASH: cc8b12cd931a024df74ed947b274d736
[#CLIENT#] R[613]: Sent: 112000.294188206 Recv: 112000.395670081 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 84   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[614]: Sent: 112000.435788581 Recv: 112007.172651209 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 66   ServerImgID: 66   Rejected: No
[#CLIENT#] R[615]: Sent: 112000.566587039 Recv: 112007.390203834 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[616]: Sent: 112000.589465289 Recv: 112007.640319376 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 75   ServerImgID: 75   Rejected: No
[#CLIENT#] R[617]: Sent: 112000.779012748 Recv: 112008.113673793 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 45   ServerImgID: 45   Rejected: No
[#CLIENT#] R[618]: Sent: 112000.830354206 Recv: 112000.882096206 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 85   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[619]: Sent: 112000.971275373 Recv: 112008.155217001 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[620]: Sent: 112001.023397748 Recv: 112008.419020418 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[621]: Sent: 112001.098252581 Recv: 112008.439783501 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 43   ServerImgID: 43   Rejected: No
[#CLIENT#] R[622]: Sent: 112001.286444415 Recv: 112008.739056501 Opcode: IMG_BLUR        OW: 1 ClientImgID: 81   ServerImgID: 81   Rejected: No
[#CLIENT#] R[623]: Sent: 112001.570095956 Recv: 112009.202724502 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 84   ServerImgID: 84   Rejected: No
[#CLIENT#] R[624]: Sent: 112001.638629790 Recv: 112009.289279002 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 68   ServerImgID: 68   Rejected: No
[#CLIENT#] R[625]: Sent: 112001.883312457 Recv: 112009.525151835 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No
[#CLIENT#] R[626]: Sent: 112002.150600915 Recv: 112009.525155627 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[627]: Sent: 112002.158826748 Recv: 112009.633916419 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 52   ServerImgID: 52   Rejected: No
[#CLIENT#] R[628]: Sent: 112002.306428873 Recv: 112002.324679248 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 86   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[629]: Sent: 112002.341567207 Recv: 112009.798439294 Opcode: IMG_BLUR        OW: 1 ClientImgID: 55   ServerImgID: 55   Rejected: No
[#CLIENT#] R[630]: Sent: 112002.786931582 Recv: 112009.817033085 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 68   ServerImgID: 68   Rejected: No HASH: 78a7633528e7dc2fc020b73ae9ed6596
[#CLIENT#] R[631]: Sent: 112002.918801915 Recv: 112009.885347919 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No
[#CLIENT#] R[632]: Sent: 112003.030398707 Recv: 112009.939895877 Opcode: IMG_BLUR        OW: 1 ClientImgID: 64   ServerImgID: 64   Rejected: No
[#CLIENT#] R[633]: Sent: 112003.078980249 Recv: 112010.030882210 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 83   ServerImgID: 83   Rejected: No
[#CLIENT#] R[634]: Sent: 112003.138641790 Recv: 112010.134295877 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No HASH: 416c13671c31bb9bb45ea4b2c6e57530
[#CLIENT#] R[635]: Sent: 112003.767563374 Recv: 112010.527248002 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No
[#CLIENT#] R[636]: Sent: 112003.851094291 Recv: 112010.538440836 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No
[#CLIENT#] R[637]: Sent: 112004.205390458 Recv: 112010.584268669 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[638]: Sent: 112004.219673166 Recv: 112010.755298586 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 49   ServerImgID: 49   Rejected: No
[#CLIENT#] R[639]: Sent: 112004.387047833 Recv: 112010.862710002 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[640]: Sent: 112004.418419833 Recv: 112010.985187211 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No HASH: 4c67d9a86c38a6a55fed1e0ec9f7d27e
[#CLIENT#] R[641]: Sent: 112004.423731249 Recv: 112010.985216461 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 70   ServerImgID: 70   Rejected: No
[#CLIENT#] R[642]: Sent: 112004.613408458 Recv: 112011.482633753 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 21   ServerImgID: 21   Rejected: No
[#CLIENT#] R[643]: Sent: 112004.706987375 Recv: 112011.973196128 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 84   ServerImgID: 84   Rejected: No
[#CLIENT#] R[644]: Sent: 112004.752997666 Recv: 112012.252145128 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[645]: Sent: 112004.815321625 Recv: 112012.275708711 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 23   ServerImgID: 23   Rejected: No
[#CLIENT#] R[646]: Sent: 112004.912591708 Recv: 112004.946390250 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 87   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[647]: Sent: 112004.951270583 Recv: 112012.741983420 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 40   ServerImgID: 40   Rejected: No
[#CLIENT#] R[648]: Sent: 112005.040725833 Recv: 112005.058479666 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 88   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[649]: Sent: 112005.164188750 Recv: 112005.181604041 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 89   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[650]: Sent: 112005.354711875 Recv: 112012.906294170 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[651]: Sent: 112005.425637750 Recv: 112013.371581587 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 76   ServerImgID: 76   Rejected: No
[#CLIENT#] R[652]: Sent: 112005.452313542 Recv: 112013.456717837 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 74   ServerImgID: 74   Rejected: No
[#CLIENT#] R[653]: Sent: 112005.641371375 Recv: 112013.755555837 Opcode: IMG_BLUR        OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[654]: Sent: 112005.676242667 Recv: 112013.773913546 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 26   ServerImgID: 26   Rejected: No HASH: 55348f8ec458faee8aef206c3daa6f14
[#CLIENT#] R[655]: Sent: 112005.682948250 Recv: 112013.920225712 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No
[#CLIENT#] R[656]: Sent: 112005.690657583 Recv: 112005.743747958 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 90   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[657]: Sent: 112005.802954125 Recv: 112014.012152504 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 47   ServerImgID: 47   Rejected: No
[#CLIENT#] R[658]: Sent: 112005.917015083 Recv: 112005.934605458 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 91   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[659]: Sent: 112005.948064875 Recv: 112014.174742921 Opcode: IMG_BLUR        OW: 1 ClientImgID: 43   ServerImgID: 43   Rejected: No
[#CLIENT#] R[660]: Sent: 112006.085166084 Recv: 112014.265878296 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No
[#CLIENT#] R[661]: Sent: 112006.160429042 Recv: 112014.273970212 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No
[#CLIENT#] R[662]: Sent: 112006.183537459 Recv: 112014.292358754 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 79   ServerImgID: 79   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[663]: Sent: 112006.243375042 Recv: 112014.361712796 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[664]: Sent: 112006.347117584 Recv: 112006.381463875 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 92   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[665]: Sent: 112006.409032125 Recv: 112006.515055792 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 93   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[666]: Sent: 112006.541802167 Recv: 112014.445879546 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[667]: Sent: 112006.563276084 Recv: 112014.551928129 Opcode: IMG_BLUR        OW: 1 ClientImgID: 92   ServerImgID: 92   Rejected: No
[#CLIENT#] R[668]: Sent: 112006.572294667 Recv: 112014.592043754 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 92   ServerImgID: 92   Rejected: No
[#CLIENT#] R[669]: Sent: 112006.577131209 Recv: 112014.816731463 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[670]: Sent: 112006.796058751 Recv: 112015.066858213 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 42   ServerImgID: 42   Rejected: No
[#CLIENT#] R[671]: Sent: 112007.005767126 Recv: 112015.155521463 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[672]: Sent: 112007.012646251 Recv: 112015.462622213 Opcode: IMG_BLUR        OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[673]: Sent: 112007.048938167 Recv: 112015.497599213 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 78   ServerImgID: 78   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[674]: Sent: 112007.071180126 Recv: 112015.515924213 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 50   ServerImgID: 50   Rejected: No HASH: 718d34266062049362b6c40493e775e1
[#CLIENT#] R[675]: Sent: 112007.083962667 Recv: 112015.953409588 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[676]: Sent: 112007.172659751 Recv: 112007.282015292 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 94   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[677]: Sent: 112007.286988876 Recv: 112016.044582130 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No
[#CLIENT#] R[678]: Sent: 112007.416603876 Recv: 112016.100680047 Opcode: IMG_BLUR        OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[679]: Sent: 112007.433197709 Recv: 112016.192270922 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 70   ServerImgID: 70   Rejected: No
[#CLIENT#] R[680]: Sent: 112007.826063168 Recv: 112016.249551088 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 51   ServerImgID: 51   Rejected: No HASH: 546b5df34b55d9683741c2a2fb3984e8
[#CLIENT#] R[681]: Sent: 112007.829397918 Recv: 112016.249563922 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 75   ServerImgID: 75   Rejected: No
[#CLIENT#] R[682]: Sent: 112007.998735709 Recv: 112008.017040959 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 95   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[683]: Sent: 112008.100478876 Recv: 112016.300430422 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 72   ServerImgID: 72   Rejected: No
[#CLIENT#] R[684]: Sent: 112008.114502918 Recv: 112016.356051255 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 16   ServerImgID: 16   Rejected: No HASH: 4b2c35b86d903c301597d0ec3e9cb745
[#CLIENT#] R[685]: Sent: 112008.277261543 Recv: 112016.634560589 Opcode: IMG_BLUR        OW: 1 ClientImgID: 94   ServerImgID: 94   Rejected: No
[#CLIENT#] R[686]: Sent: 112008.382373585 Recv: 112016.688419714 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 77   ServerImgID: 77   Rejected: No
[#CLIENT#] R[687]: Sent: 112008.518813168 Recv: 112008.553248918 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 96   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[688]: Sent: 112008.594650460 Recv: 112017.151335422 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[689]: Sent: 112008.606881460 Recv: 112017.172361339 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[690]: Sent: 112008.628868001 Recv: 112017.255793964 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 89   ServerImgID: 89   Rejected: No
[#CLIENT#] R[691]: Sent: 112008.669345543 Recv: 112017.310649006 Opcode: IMG_BLUR        OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[692]: Sent: 112008.674498543 Recv: 112017.797316881 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 84   ServerImgID: 84   Rejected: No
[#CLIENT#] R[693]: Sent: 112008.755475210 Recv: 112017.905118672 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 84   ServerImgID: 84   Rejected: No HASH: 724f8c7da6816ec84a846429e542b3af
[#CLIENT#] R[694]: Sent: 112008.790848626 Recv: 112008.842477418 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 97   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[695]: Sent: 112009.099969085 Recv: 112017.969320923 Opcode: IMG_BLUR        OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[696]: Sent: 112009.212237835 Recv: 112018.432009256 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 76   ServerImgID: 76   Rejected: No
[#CLIENT#] R[697]: Sent: 112009.365304502 Recv: 112018.486338339 Opcode: IMG_BLUR        OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[698]: Sent: 112009.424150585 Recv: 112009.525147293 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 98   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[699]: Sent: 112009.661046835 Recv: 112009.712702752 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 99   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[700]: Sent: 112009.842379627 Recv: 112018.570291381 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 39   ServerImgID: 39   Rejected: No
[#CLIENT#] R[701]: Sent: 112009.875662419 Recv: 112018.819685756 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 75   ServerImgID: 75   Rejected: No
[#CLIENT#] R[702]: Sent: 112009.909782502 Recv: 112018.845328465 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 26   ServerImgID: 26   Rejected: No
[#CLIENT#] R[703]: Sent: 112010.134311627 Recv: 112010.186080419 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 100  Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[704]: Sent: 112010.202627544 Recv: 112019.088187631 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 75   ServerImgID: 75   Rejected: No
[#CLIENT#] R[705]: Sent: 112010.274665044 Recv: 112019.139125006 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 40   ServerImgID: 40   Rejected: No
[#CLIENT#] R[706]: Sent: 112010.275951711 Recv: 112019.436405173 Opcode: IMG_BLUR        OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No
[#CLIENT#] R[707]: Sent: 112010.295720211 Recv: 112019.686616173 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 75   ServerImgID: 75   Rejected: No
[#CLIENT#] R[708]: Sent: 112010.302172377 Recv: 112010.407398377 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 101  Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[709]: Sent: 112010.456408794 Recv: 112019.704911757 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 35   ServerImgID: 35   Rejected: No HASH: e91603ff2577620f87e773d162cbb1b8
[#CLIENT#] R[710]: Sent: 112010.493198461 Recv: 112010.527240127 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 102  Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[711]: Sent: 112010.689509502 Recv: 112019.937775882 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 54   ServerImgID: 54   Rejected: No
[#CLIENT#] R[712]: Sent: 112010.985225628 Recv: 112011.004184294 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 103  Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[713]: Sent: 112011.060700461 Recv: 112020.021745965 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[714]: Sent: 112011.353670753 Recv: 112011.387782669 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 104  Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[715]: Sent: 112011.474764544 Recv: 112020.105687965 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[716]: Sent: 112011.489695086 Recv: 112020.269322632 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 104  ServerImgID: 104  Rejected: No
[#CLIENT#] R[717]: Sent: 112011.520905711 Recv: 112020.569881257 Opcode: IMG_BLUR        OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[718]: Sent: 112011.646228669 Recv: 112021.056595049 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No
[#CLIENT#] R[719]: Sent: 112011.815966836 Recv: 112011.868154128 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 105  Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[720]: Sent: 112011.985138045 Recv: 112021.307109591 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 25   ServerImgID: 25   Rejected: No
[#CLIENT#] R[721]: Sent: 112012.060733795 Recv: 112021.409994341 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 73   ServerImgID: 73   Rejected: No HASH: a475f010c4c086a083fedd66f3725234
[#CLIENT#] R[722]: Sent: 112012.171956378 Recv: 112012.231615753 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 106  Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[723]: Sent: 112012.249258420 Recv: 112021.410019132 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 74   ServerImgID: 74   Rejected: No
[#CLIENT#] R[724]: Sent: 112012.330914461 Recv: 112021.444850841 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 60   ServerImgID: 60   Rejected: No HASH: b1b45b2076c3827d711962b82aa208f4
[#CLIENT#] R[725]: Sent: 112012.347986295 Recv: 112021.444860091 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No
[#CLIENT#] R[726]: Sent: 112012.561488462 Recv: 112021.462951633 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 91   ServerImgID: 91   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[727]: Sent: 112012.613970128 Recv: 112021.583676133 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 69   ServerImgID: 69   Rejected: No
[#CLIENT#] R[728]: Sent: 112012.686991712 Recv: 112021.832467758 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 80   ServerImgID: 80   Rejected: No
[#CLIENT#] R[729]: Sent: 112012.793979753 Recv: 112021.996050799 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 36   ServerImgID: 36   Rejected: No
[#CLIENT#] R[730]: Sent: 112012.877731462 Recv: 112022.082879424 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 47   ServerImgID: 47   Rejected: No
[#CLIENT#] R[731]: Sent: 112013.247570462 Recv: 112022.332694425 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 25   ServerImgID: 25   Rejected: No
[#CLIENT#] R[732]: Sent: 112013.265656337 Recv: 112022.416993633 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 72   ServerImgID: 72   Rejected: No
[#CLIENT#] R[733]: Sent: 112013.320879754 Recv: 112022.548970341 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 103  ServerImgID: 103  Rejected: No
[#CLIENT#] R[734]: Sent: 112013.403986962 Recv: 112022.772396383 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[735]: Sent: 112013.537760462 Recv: 112013.555384295 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 107  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[736]: Sent: 112013.616386504 Recv: 112022.882865800 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[737]: Sent: 112013.749125337 Recv: 112022.882908592 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[738]: Sent: 112013.887867087 Recv: 112022.917788342 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 34   ServerImgID: 34   Rejected: No HASH: 6af9501a868a53fa1aad440e6858e798
[#CLIENT#] R[739]: Sent: 112013.971222879 Recv: 112022.952478592 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 92   ServerImgID: 92   Rejected: No HASH: 2ed48485c391a80bfb05fe3b8525c2eb
[#CLIENT#] R[740]: Sent: 112014.055042629 Recv: 112023.347933050 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 27   ServerImgID: 27   Rejected: No
[#CLIENT#] R[741]: Sent: 112014.061666754 Recv: 112014.079425796 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 108  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[742]: Sent: 112014.273996421 Recv: 112023.355048092 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No
[#CLIENT#] R[743]: Sent: 112014.465714254 Recv: 112023.516119508 Opcode: IMG_BLUR        OW: 1 ClientImgID: 25   ServerImgID: 25   Rejected: No
[#CLIENT#] R[744]: Sent: 112014.531604421 Recv: 112023.600044300 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 89   ServerImgID: 89   Rejected: No
[#CLIENT#] R[745]: Sent: 112014.649512088 Recv: 112023.639021384 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No
[#CLIENT#] R[746]: Sent: 112014.656108588 Recv: 112023.686891467 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 84   ServerImgID: 84   Rejected: No
[#CLIENT#] R[747]: Sent: 112014.788133963 Recv: 112023.793145050 Opcode: IMG_BLUR        OW: 1 ClientImgID: 102  ServerImgID: 102  Rejected: No
[#CLIENT#] R[748]: Sent: 112015.136589504 Recv: 112023.836259592 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 93   ServerImgID: 93   Rejected: No
[#CLIENT#] R[749]: Sent: 112015.203334421 Recv: 112023.942338425 Opcode: IMG_BLUR        OW: 1 ClientImgID: 69   ServerImgID: 69   Rejected: No
[#CLIENT#] R[750]: Sent: 112015.214086838 Recv: 112023.999082592 Opcode: IMG_BLUR        OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No
[#CLIENT#] R[751]: Sent: 112015.284122338 Recv: 112024.084859884 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[752]: Sent: 112015.309347755 Recv: 112024.169956967 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 107  ServerImgID: 107  Rejected: No
[#CLIENT#] R[753]: Sent: 112015.573374588 Recv: 112024.256837842 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 82   ServerImgID: 82   Rejected: No
[#CLIENT#] R[754]: Sent: 112015.726723921 Recv: 112024.300756176 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 93   ServerImgID: 93   Rejected: No
[#CLIENT#] R[755]: Sent: 112015.769246088 Recv: 112024.385012551 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 72   ServerImgID: 72   Rejected: No
[#CLIENT#] R[756]: Sent: 112015.916604713 Recv: 112024.472156592 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No
[#CLIENT#] R[757]: Sent: 112016.249572797 Recv: 112024.507803092 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 69   ServerImgID: 69   Rejected: No HASH: 08d5145482ee2b793c663934d28ba736
[#CLIENT#] R[758]: Sent: 112016.279877213 Recv: 112024.556332051 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 89   ServerImgID: 89   Rejected: No
[#CLIENT#] R[759]: Sent: 112016.356067255 Recv: 112024.611052592 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 75   ServerImgID: 75   Rejected: No HASH: adc23dc6dc33b962db7266b6c30d2722
[#CLIENT#] R[760]: Sent: 112016.440446963 Recv: 112024.611131217 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No
[#CLIENT#] R[761]: Sent: 112016.592087339 Recv: 112016.609619089 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 109  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[762]: Sent: 112016.806062547 Recv: 112024.717720051 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 29   ServerImgID: 29   Rejected: No HASH: 9d278f693acd1c3d933d5bcbd5e97aef
[#CLIENT#] R[763]: Sent: 112017.163918589 Recv: 112025.075474176 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 40   ServerImgID: 40   Rejected: No
[#CLIENT#] R[764]: Sent: 112017.241972089 Recv: 112025.167192634 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[765]: Sent: 112017.256182630 Recv: 112025.417355301 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 23   ServerImgID: 23   Rejected: No
[#CLIENT#] R[766]: Sent: 112017.321792881 Recv: 112025.880174051 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 56   ServerImgID: 56   Rejected: No
[#CLIENT#] R[767]: Sent: 112017.326434631 Recv: 112026.181991968 Opcode: IMG_BLUR        OW: 1 ClientImgID: 94   ServerImgID: 94   Rejected: No
[#CLIENT#] R[768]: Sent: 112017.408211464 Recv: 112026.285024343 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 22   ServerImgID: 22   Rejected: No HASH: 8ad3ff104f1f02bc48625a0d3278d7ca
[#CLIENT#] R[769]: Sent: 112017.555876797 Recv: 112026.285035051 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 78   ServerImgID: 78   Rejected: No
[#CLIENT#] R[770]: Sent: 112017.584611131 Recv: 112026.285086718 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[771]: Sent: 112017.666612964 Recv: 112026.328844010 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 107  ServerImgID: 107  Rejected: No
[#CLIENT#] R[772]: Sent: 112017.905134339 Recv: 112026.419897843 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[773]: Sent: 112018.033900923 Recv: 112026.473273135 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 67   ServerImgID: 67   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[774]: Sent: 112018.067994673 Recv: 112026.491623010 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 59   ServerImgID: 59   Rejected: No HASH: ca8dabad272577686d07ecf7bb519b7f
[#CLIENT#] R[775]: Sent: 112018.351594673 Recv: 112026.506612218 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[776]: Sent: 112018.398573214 Recv: 112026.525027843 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 74   ServerImgID: 74   Rejected: No HASH: 3b3e20aa776ada5ed79da1b1242d54fd
[#CLIENT#] R[777]: Sent: 112018.503808881 Recv: 112026.580245427 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 16   ServerImgID: 16   Rejected: No HASH: 4b2c35b86d903c301597d0ec3e9cb745
[#CLIENT#] R[778]: Sent: 112018.573819548 Recv: 112026.596691635 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[779]: Sent: 112018.805075048 Recv: 112027.059747552 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 93   ServerImgID: 93   Rejected: No
[#CLIENT#] R[780]: Sent: 112018.845293298 Recv: 112027.520741594 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[781]: Sent: 112019.069706423 Recv: 112027.985986926 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[782]: Sent: 112019.079635215 Recv: 112028.128262676 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[783]: Sent: 112019.096315965 Recv: 112028.146607801 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 50   ServerImgID: 50   Rejected: No HASH: 718d34266062049362b6c40493e775e1
[#CLIENT#] R[784]: Sent: 112019.096374798 Recv: 112019.114955756 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 110  Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[785]: Sent: 112019.169295798 Recv: 112028.381470260 Opcode: IMG_BLUR        OW: 1 ClientImgID: 45   ServerImgID: 45   Rejected: No
[#CLIENT#] R[786]: Sent: 112019.310272798 Recv: 112028.437875802 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 97   ServerImgID: 97   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[787]: Sent: 112019.462030548 Recv: 112028.871396843 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No
[#CLIENT#] R[788]: Sent: 112019.518958882 Recv: 112029.333874927 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 101  ServerImgID: 101  Rejected: No
[#CLIENT#] R[789]: Sent: 112019.891807590 Recv: 112029.420885135 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 53   ServerImgID: 53   Rejected: No
[#CLIENT#] R[790]: Sent: 112019.999679090 Recv: 112029.477157719 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 43   ServerImgID: 43   Rejected: No HASH: 1832c766ca31fff55366ca0b5ebfe998
[#CLIENT#] R[791]: Sent: 112020.005249965 Recv: 112029.477169510 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 23   ServerImgID: 23   Rejected: No
[#CLIENT#] R[792]: Sent: 112020.285191674 Recv: 112029.748814802 Opcode: IMG_BLUR        OW: 1 ClientImgID: 27   ServerImgID: 27   Rejected: No
[#CLIENT#] R[793]: Sent: 112020.304538049 Recv: 112029.783935719 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No HASH: e0d35013596353b35647792dfb1d70fb
[#CLIENT#] R[794]: Sent: 112020.437322590 Recv: 112030.211876511 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 81   ServerImgID: 81   Rejected: No
[#CLIENT#] R[795]: Sent: 112020.454667799 Recv: 112030.266508469 Opcode: IMG_BLUR        OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[796]: Sent: 112020.541174382 Recv: 112030.350899719 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 39   ServerImgID: 39   Rejected: No
[#CLIENT#] R[797]: Sent: 112020.605923757 Recv: 112030.405158636 Opcode: IMG_BLUR        OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[798]: Sent: 112020.832428049 Recv: 112020.850064091 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 111  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[799]: Sent: 112020.900500924 Recv: 112030.492100886 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 35   ServerImgID: 35   Rejected: No
[#CLIENT#] R[800]: Sent: 112021.038358424 Recv: 112030.957601844 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[801]: Sent: 112021.060816216 Recv: 112031.420384386 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 98   ServerImgID: 98   Rejected: No
[#CLIENT#] R[802]: Sent: 112021.098547674 Recv: 112031.671489470 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 16   ServerImgID: 16   Rejected: No
[#CLIENT#] R[803]: Sent: 112021.290083216 Recv: 112031.763680261 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[804]: Sent: 112021.410030549 Recv: 112031.805999803 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 81   ServerImgID: 81   Rejected: No
[#CLIENT#] R[805]: Sent: 112021.519739216 Recv: 112031.890512512 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 74   ServerImgID: 74   Rejected: No
[#CLIENT#] R[806]: Sent: 112021.538451633 Recv: 112032.054720845 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[807]: Sent: 112021.594344424 Recv: 112032.073036845 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 72   ServerImgID: 72   Rejected: No HASH: 60ea7ced6c2564b47808ed9c0f294ac5
[#CLIENT#] R[808]: Sent: 112021.603806424 Recv: 112032.126374178 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 23   ServerImgID: 23   Rejected: No HASH: 5e5931dcd1b1bc70190585de0496669f
[#CLIENT#] R[809]: Sent: 112021.711479591 Recv: 112032.142782512 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 68   ServerImgID: 68   Rejected: No
[#CLIENT#] R[810]: Sent: 112021.715241674 Recv: 112032.316431387 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[811]: Sent: 112021.795749966 Recv: 112032.360016928 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 63   ServerImgID: 63   Rejected: No
[#CLIENT#] R[812]: Sent: 112021.806521841 Recv: 112032.847036887 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 93   ServerImgID: 93   Rejected: No
[#CLIENT#] R[813]: Sent: 112021.956815674 Recv: 112032.931235637 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 33   ServerImgID: 33   Rejected: No
[#CLIENT#] R[814]: Sent: 112022.089054841 Recv: 112032.987711387 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 42   ServerImgID: 42   Rejected: No HASH: be9bcb384b494d77de72bf72c984488a
[#CLIENT#] R[815]: Sent: 112022.439253508 Recv: 112022.548953258 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 112  Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[816]: Sent: 112022.785608800 Recv: 112022.882899425 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 113  Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[817]: Sent: 112022.952492883 Recv: 112033.396541971 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 81   ServerImgID: 81   Rejected: No
[#CLIENT#] R[818]: Sent: 112023.212730217 Recv: 112033.419645346 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 106  ServerImgID: 106  Rejected: No
[#CLIENT#] R[819]: Sent: 112023.238108133 Recv: 112033.437742721 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 79   ServerImgID: 79   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[820]: Sent: 112023.256385675 Recv: 112033.506864429 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No
[#CLIENT#] R[821]: Sent: 112023.310093342 Recv: 112033.976834221 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[822]: Sent: 112023.312418967 Recv: 112034.017602179 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[823]: Sent: 112023.574550134 Recv: 112034.063827179 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 22   ServerImgID: 22   Rejected: No
[#CLIENT#] R[824]: Sent: 112023.611076050 Recv: 112034.109999638 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 27   ServerImgID: 27   Rejected: No
[#CLIENT#] R[825]: Sent: 112023.833754925 Recv: 112034.600083763 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No
[#CLIENT#] R[826]: Sent: 112024.020494300 Recv: 112034.862931930 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 55   ServerImgID: 55   Rejected: No
[#CLIENT#] R[827]: Sent: 112024.156920967 Recv: 112035.162372263 Opcode: IMG_BLUR        OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[828]: Sent: 112024.163722884 Recv: 112035.412588388 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 97   ServerImgID: 97   Rejected: No
[#CLIENT#] R[829]: Sent: 112024.285520301 Recv: 112035.503863055 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No
[#CLIENT#] R[830]: Sent: 112024.291444509 Recv: 112035.990061347 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 76   ServerImgID: 76   Rejected: No
[#CLIENT#] R[831]: Sent: 112024.507820467 Recv: 112036.078238597 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[832]: Sent: 112024.550936134 Recv: 112036.119099847 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[833]: Sent: 112024.717742717 Recv: 112036.385134014 Opcode: IMG_BLUR        OW: 1 ClientImgID: 58   ServerImgID: 58   Rejected: No
[#CLIENT#] R[834]: Sent: 112024.727090551 Recv: 112024.744693092 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 114  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[835]: Sent: 112024.880659384 Recv: 112036.546755555 Opcode: IMG_BLUR        OW: 1 ClientImgID: 16   ServerImgID: 16   Rejected: No
[#CLIENT#] R[836]: Sent: 112024.937507551 Recv: 112036.633785805 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No
[#CLIENT#] R[837]: Sent: 112024.977492551 Recv: 112036.754763639 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 35   ServerImgID: 35   Rejected: No
[#CLIENT#] R[838]: Sent: 112025.173679759 Recv: 112036.889243389 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 49   ServerImgID: 49   Rejected: No
[#CLIENT#] R[839]: Sent: 112025.185758426 Recv: 112036.973626972 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 108  ServerImgID: 108  Rejected: No
[#CLIENT#] R[840]: Sent: 112025.324538384 Recv: 112037.275848556 Opcode: IMG_BLUR        OW: 1 ClientImgID: 93   ServerImgID: 93   Rejected: No
[#CLIENT#] R[841]: Sent: 112025.488941759 Recv: 112037.365131472 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[842]: Sent: 112025.669417385 Recv: 112037.529602223 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 36   ServerImgID: 36   Rejected: No
[#CLIENT#] R[843]: Sent: 112025.947285510 Recv: 112037.552430223 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[844]: Sent: 112026.169498510 Recv: 112038.019122556 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 84   ServerImgID: 84   Rejected: No
[#CLIENT#] R[845]: Sent: 112026.285045843 Recv: 112038.182543890 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 65   ServerImgID: 65   Rejected: No
[#CLIENT#] R[846]: Sent: 112026.358987718 Recv: 112038.347083806 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 36   ServerImgID: 36   Rejected: No
[#CLIENT#] R[847]: Sent: 112026.366880427 Recv: 112038.360649473 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 28   ServerImgID: 28   Rejected: No
[#CLIENT#] R[848]: Sent: 112026.415870427 Recv: 112038.463379931 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No HASH: 9cc30f3f41b6c1664957f515b67bb06b
[#CLIENT#] R[849]: Sent: 112026.491634302 Recv: 112038.463396348 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 50   ServerImgID: 50   Rejected: No
[#CLIENT#] R[850]: Sent: 112026.580261593 Recv: 112038.541504723 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 77   ServerImgID: 77   Rejected: No
[#CLIENT#] R[851]: Sent: 112026.611070135 Recv: 112038.630795056 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[852]: Sent: 112026.743019260 Recv: 112038.719901806 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 39   ServerImgID: 39   Rejected: No
[#CLIENT#] R[853]: Sent: 112026.867657593 Recv: 112038.823294473 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No HASH: 44c02a40a3054f600a746dd4283071ab
[#CLIENT#] R[854]: Sent: 112026.881762093 Recv: 112038.823310848 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 72   ServerImgID: 72   Rejected: No
[#CLIENT#] R[855]: Sent: 112026.916735302 Recv: 112038.987045265 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 28   ServerImgID: 28   Rejected: No
[#CLIENT#] R[856]: Sent: 112026.926815635 Recv: 112039.004857390 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 39   ServerImgID: 39   Rejected: No HASH: 7fba26df9b8d47e422afff7b6044e9c1
[#CLIENT#] R[857]: Sent: 112026.974339635 Recv: 112039.108296348 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 56   ServerImgID: 56   Rejected: No HASH: 09265369a030e219fcd2d80a99ded564
[#CLIENT#] R[858]: Sent: 112027.192255969 Recv: 112027.209868552 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 115  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[859]: Sent: 112027.326059594 Recv: 112039.495413598 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 63   ServerImgID: 63   Rejected: No
[#CLIENT#] R[860]: Sent: 112027.392076969 Recv: 112039.658102474 Opcode: IMG_BLUR        OW: 1 ClientImgID: 85   ServerImgID: 85   Rejected: No
[#CLIENT#] R[861]: Sent: 112027.432244594 Recv: 112039.821810182 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[862]: Sent: 112027.443062177 Recv: 112039.875726432 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 75   ServerImgID: 75   Rejected: No HASH: adc23dc6dc33b962db7266b6c30d2722
[#CLIENT#] R[863]: Sent: 112027.459109302 Recv: 112039.907372557 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 88   ServerImgID: 88   Rejected: No
[#CLIENT#] R[864]: Sent: 112027.490791927 Recv: 112040.070943224 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 60   ServerImgID: 60   Rejected: No
[#CLIENT#] R[865]: Sent: 112027.573389552 Recv: 112040.608220641 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[866]: Sent: 112027.717450426 Recv: 112040.643634807 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 108  ServerImgID: 108  Rejected: No
[#CLIENT#] R[867]: Sent: 112027.754266343 Recv: 112027.806057093 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 116  Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[868]: Sent: 112027.880504135 Recv: 112040.749593557 Opcode: IMG_BLUR        OW: 1 ClientImgID: 102  ServerImgID: 102  Rejected: No
[#CLIENT#] R[869]: Sent: 112027.912661760 Recv: 112041.212838016 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 45   ServerImgID: 45   Rejected: No
[#CLIENT#] R[870]: Sent: 112028.023312093 Recv: 112028.128254301 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 117  Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[871]: Sent: 112028.189815676 Recv: 112041.299772683 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[872]: Sent: 112028.250118760 Recv: 112041.765429058 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No
[#CLIENT#] R[873]: Sent: 112028.316122426 Recv: 112041.849883308 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 109  ServerImgID: 109  Rejected: No
[#CLIENT#] R[874]: Sent: 112028.437897427 Recv: 112028.472398260 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 118  Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[875]: Sent: 112028.517172093 Recv: 112041.867403766 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 49   ServerImgID: 49   Rejected: No
[#CLIENT#] R[876]: Sent: 112028.593011552 Recv: 112041.903119016 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 52   ServerImgID: 52   Rejected: No HASH: a8668745537ff91a7572d7046ad701bb
[#CLIENT#] R[877]: Sent: 112028.666487843 Recv: 112041.922779683 Opcode: IMG_BLUR        OW: 1 ClientImgID: 74   ServerImgID: 74   Rejected: No
[#CLIENT#] R[878]: Sent: 112028.718162010 Recv: 112041.996549975 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 27   ServerImgID: 27   Rejected: No
[#CLIENT#] R[879]: Sent: 112028.802036052 Recv: 112028.820348135 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 119  Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[880]: Sent: 112028.870794385 Recv: 112042.047948058 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 111  ServerImgID: 111  Rejected: No
[#CLIENT#] R[881]: Sent: 112028.890200593 Recv: 112028.908414302 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 120  Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[882]: Sent: 112028.927161927 Recv: 112042.102282516 Opcode: IMG_BLUR        OW: 1 ClientImgID: 74   ServerImgID: 74   Rejected: No
[#CLIENT#] R[883]: Sent: 112028.939364968 Recv: 112042.191193141 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 79   ServerImgID: 79   Rejected: No
[#CLIENT#] R[884]: Sent: 112029.066133510 Recv: 112042.654454142 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 94   ServerImgID: 94   Rejected: No
[#CLIENT#] R[885]: Sent: 112029.078312718 Recv: 112042.673240017 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 50   ServerImgID: 50   Rejected: No HASH: 9db28b1eaa63f07ad95591ec3ed72587
[#CLIENT#] R[886]: Sent: 112029.169102427 Recv: 112042.741536350 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No
[#CLIENT#] R[887]: Sent: 112029.199371427 Recv: 112029.251254385 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 121  Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[888]: Sent: 112029.317700719 Recv: 112042.828642933 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 50   ServerImgID: 50   Rejected: No
[#CLIENT#] R[889]: Sent: 112029.334765385 Recv: 112042.882984308 Opcode: IMG_BLUR        OW: 1 ClientImgID: 61   ServerImgID: 61   Rejected: No
[#CLIENT#] R[890]: Sent: 112029.658961760 Recv: 112042.891020933 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 26   ServerImgID: 26   Rejected: No
[#CLIENT#] R[891]: Sent: 112029.707192219 Recv: 112042.934361767 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 40   ServerImgID: 40   Rejected: No
[#CLIENT#] R[892]: Sent: 112029.845472844 Recv: 112043.397538559 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[893]: Sent: 112029.863494594 Recv: 112043.503737642 Opcode: IMG_BLUR        OW: 1 ClientImgID: 96   ServerImgID: 96   Rejected: No
[#CLIENT#] R[894]: Sent: 112030.013063886 Recv: 112043.521866017 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 35   ServerImgID: 35   Rejected: No HASH: f02548bdc1d694bf2aa0e1d35726601f
[#CLIENT#] R[895]: Sent: 112030.205475511 Recv: 112043.591028559 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[896]: Sent: 112030.529152136 Recv: 112043.754468517 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 34   ServerImgID: 34   Rejected: No
[#CLIENT#] R[897]: Sent: 112030.725333969 Recv: 112030.743610053 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 122  Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[898]: Sent: 112030.938225636 Recv: 112044.249868309 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[899]: Sent: 112031.003551428 Recv: 112031.113132594 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 123  Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[900]: Sent: 112031.909394220 Recv: 112044.341497142 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[901]: Sent: 112031.918637553 Recv: 112044.360224851 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 59   ServerImgID: 59   Rejected: No HASH: ca8dabad272577686d07ecf7bb519b7f
[#CLIENT#] R[902]: Sent: 112031.941400470 Recv: 112031.959192303 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 124  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[903]: Sent: 112032.126389428 Recv: 112044.644462809 Opcode: IMG_BLUR        OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No
[#CLIENT#] R[904]: Sent: 112032.170444137 Recv: 112044.894240643 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 55   ServerImgID: 55   Rejected: No
[#CLIENT#] R[905]: Sent: 112032.215867470 Recv: 112044.948656726 Opcode: IMG_BLUR        OW: 1 ClientImgID: 33   ServerImgID: 33   Rejected: No
[#CLIENT#] R[906]: Sent: 112032.236553345 Recv: 112045.057327393 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 58   ServerImgID: 58   Rejected: No HASH: 0e2dd886b2225341ca50f8f37103dbce
[#CLIENT#] R[907]: Sent: 112032.280052595 Recv: 112045.075303809 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 91   ServerImgID: 91   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[908]: Sent: 112032.328301637 Recv: 112045.124621143 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No
[#CLIENT#] R[909]: Sent: 112032.442089512 Recv: 112045.143289226 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 53   ServerImgID: 53   Rejected: No HASH: cb8a2ae1d35da5dc317ed9a391166950
[#CLIENT#] R[910]: Sent: 112032.608422970 Recv: 112045.374925851 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 42   ServerImgID: 42   Rejected: No
[#CLIENT#] R[911]: Sent: 112032.627429470 Recv: 112045.483477726 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 27   ServerImgID: 27   Rejected: No HASH: 113ea43c7c52e20533fd5c0a6c5bc11e
[#CLIENT#] R[912]: Sent: 112032.905962012 Recv: 112045.483484935 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[913]: Sent: 112032.987725262 Recv: 112045.483497143 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No
[#CLIENT#] R[914]: Sent: 112033.025768762 Recv: 112033.077638762 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 125  Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[915]: Sent: 112033.220246470 Recv: 112045.518623560 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[916]: Sent: 112033.350024262 Recv: 112045.782359060 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[917]: Sent: 112033.517846929 Recv: 112033.536059971 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 126  Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[918]: Sent: 112033.568983804 Recv: 112045.869359102 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No
[#CLIENT#] R[919]: Sent: 112033.664160387 Recv: 112045.974501310 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No HASH: a669a8b1c741bbd02a88795289a0e8ac
[#CLIENT#] R[920]: Sent: 112034.011832221 Recv: 112045.974512977 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 51   ServerImgID: 51   Rejected: No
[#CLIENT#] R[921]: Sent: 112034.048678846 Recv: 112045.988135560 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 71   ServerImgID: 71   Rejected: No
[#CLIENT#] R[922]: Sent: 112034.049831304 Recv: 112046.450545227 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 81   ServerImgID: 81   Rejected: No
[#CLIENT#] R[923]: Sent: 112034.225480554 Recv: 112046.537397518 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 126  ServerImgID: 126  Rejected: No
[#CLIENT#] R[924]: Sent: 112034.480416804 Recv: 112046.837270644 Opcode: IMG_BLUR        OW: 1 ClientImgID: 58   ServerImgID: 58   Rejected: No
[#CLIENT#] R[925]: Sent: 112034.487712346 Recv: 112046.891607852 Opcode: IMG_BLUR        OW: 1 ClientImgID: 77   ServerImgID: 77   Rejected: No
[#CLIENT#] R[926]: Sent: 112034.501137179 Recv: 112047.141571977 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 23   ServerImgID: 23   Rejected: No
[#CLIENT#] R[927]: Sent: 112034.506162096 Recv: 112047.604381602 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 101  ServerImgID: 101  Rejected: No
[#CLIENT#] R[928]: Sent: 112034.626354471 Recv: 112047.710198811 Opcode: IMG_BLUR        OW: 1 ClientImgID: 57   ServerImgID: 57   Rejected: No
[#CLIENT#] R[929]: Sent: 112034.898697805 Recv: 112047.815651144 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No HASH: 601af64569241055b07d9a99f0c670a1
[#CLIENT#] R[930]: Sent: 112034.925287513 Recv: 112047.980413561 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[931]: Sent: 112035.015709430 Recv: 112048.000800644 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[932]: Sent: 112035.027188888 Recv: 112048.469862603 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No
[#CLIENT#] R[933]: Sent: 112035.395618972 Recv: 112048.477303436 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[934]: Sent: 112035.916235805 Recv: 112048.530256144 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No HASH: 12c73cb1e8f64e1922959be2a9d982a0
[#CLIENT#] R[935]: Sent: 112035.990276138 Recv: 112048.530321936 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 51   ServerImgID: 51   Rejected: No
[#CLIENT#] R[936]: Sent: 112036.247935097 Recv: 112048.548814686 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No HASH: 9a2938e4f0d7513d21fe58144e3560d3
[#CLIENT#] R[937]: Sent: 112036.296629805 Recv: 112048.566740061 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 26   ServerImgID: 26   Rejected: No HASH: 2cc529524a171427ba242fcf8a09b6ff
[#CLIENT#] R[938]: Sent: 112036.326591930 Recv: 112048.601669478 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No HASH: 2767be6f95d5d7f6dee66214219c59a2
[#CLIENT#] R[939]: Sent: 112036.587850555 Recv: 112048.792420103 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 116  ServerImgID: 116  Rejected: No
[#CLIENT#] R[940]: Sent: 112036.595087639 Recv: 112048.877069478 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[941]: Sent: 112036.663533555 Recv: 112049.126961436 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 54   ServerImgID: 54   Rejected: No
[#CLIENT#] R[942]: Sent: 112036.711061847 Recv: 112036.745338389 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 127  Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[943]: Sent: 112036.851427639 Recv: 112049.218098270 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 53   ServerImgID: 53   Rejected: No
[#CLIENT#] R[944]: Sent: 112036.944554847 Recv: 112049.304927436 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 66   ServerImgID: 66   Rejected: No
[#CLIENT#] R[945]: Sent: 112037.024357681 Recv: 112049.555397853 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[946]: Sent: 112037.052454681 Recv: 112049.562153103 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 107  ServerImgID: 107  Rejected: No
[#CLIENT#] R[947]: Sent: 112037.106514306 Recv: 112049.725273812 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 118  ServerImgID: 118  Rejected: No
[#CLIENT#] R[948]: Sent: 112037.319918639 Recv: 112049.743611395 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 38   ServerImgID: 38   Rejected: No HASH: b8104132493de7040858ff7f6ba4b1e0
[#CLIENT#] R[949]: Sent: 112037.569339806 Recv: 112049.810121145 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 114  ServerImgID: 114  Rejected: No
[#CLIENT#] R[950]: Sent: 112037.584321264 Recv: 112049.896672603 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 122  ServerImgID: 122  Rejected: No
[#CLIENT#] R[951]: Sent: 112037.656544514 Recv: 112049.915891395 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 114  ServerImgID: 114  Rejected: No HASH: 392626c80f548779a200c8ec6e46c645
[#CLIENT#] R[952]: Sent: 112037.699915889 Recv: 112049.985192562 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 38   ServerImgID: 38   Rejected: No
[#CLIENT#] R[953]: Sent: 112037.808317598 Recv: 112049.992037103 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 88   ServerImgID: 88   Rejected: No
[#CLIENT#] R[954]: Sent: 112037.840040389 Recv: 112050.155775937 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 92   ServerImgID: 92   Rejected: No
[#CLIENT#] R[955]: Sent: 112037.850932389 Recv: 112050.240088270 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 82   ServerImgID: 82   Rejected: No
[#CLIENT#] R[956]: Sent: 112037.876505639 Recv: 112050.326857937 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[957]: Sent: 112038.021344056 Recv: 112038.126838598 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 128  Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[958]: Sent: 112038.273763640 Recv: 112050.590201479 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 67   ServerImgID: 67   Rejected: No
[#CLIENT#] R[959]: Sent: 112038.554280390 Recv: 112050.597292270 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 38   ServerImgID: 38   Rejected: No
[#CLIENT#] R[960]: Sent: 112038.577697431 Recv: 112050.759385187 Opcode: IMG_BLUR        OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[961]: Sent: 112038.823321265 Recv: 112050.846123479 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 47   ServerImgID: 47   Rejected: No
[#CLIENT#] R[962]: Sent: 112038.864295556 Recv: 112051.309313437 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[963]: Sent: 112039.108314848 Recv: 112051.392779979 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 91   ServerImgID: 91   Rejected: No
[#CLIENT#] R[964]: Sent: 112039.171584348 Recv: 112051.447238562 Opcode: IMG_BLUR        OW: 1 ClientImgID: 77   ServerImgID: 77   Rejected: No
[#CLIENT#] R[965]: Sent: 112039.176065640 Recv: 112051.460495646 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 49   ServerImgID: 49   Rejected: No
[#CLIENT#] R[966]: Sent: 112039.191743723 Recv: 112039.209894723 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 129  Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[967]: Sent: 112039.329163848 Recv: 112051.565891521 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 128  ServerImgID: 128  Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[968]: Sent: 112039.337961140 Recv: 112051.601173771 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 87   ServerImgID: 87   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[969]: Sent: 112039.421095598 Recv: 112039.439230140 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 130  Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[970]: Sent: 112039.446014015 Recv: 112051.634047521 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No
[#CLIENT#] R[971]: Sent: 112039.552784473 Recv: 112051.795786979 Opcode: IMG_BLUR        OW: 1 ClientImgID: 43   ServerImgID: 43   Rejected: No
[#CLIENT#] R[972]: Sent: 112039.730487099 Recv: 112052.057968396 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 85   ServerImgID: 85   Rejected: No
[#CLIENT#] R[973]: Sent: 112040.073891974 Recv: 112052.076130604 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 86   ServerImgID: 86   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[974]: Sent: 112040.201458849 Recv: 112052.142362604 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[975]: Sent: 112040.320260891 Recv: 112040.373302974 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 131  Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[976]: Sent: 112040.431332016 Recv: 112052.226482605 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 33   ServerImgID: 33   Rejected: No
[#CLIENT#] R[977]: Sent: 112040.453754516 Recv: 112052.282684230 Opcode: IMG_BLUR        OW: 1 ClientImgID: 120  ServerImgID: 120  Rejected: No
[#CLIENT#] R[978]: Sent: 112040.503691557 Recv: 112040.608214974 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 132  Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[979]: Sent: 112040.837983557 Recv: 112052.300764896 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 88   ServerImgID: 88   Rejected: No HASH: 3b3e20aa776ada5ed79da1b1242d54fd
[#CLIENT#] R[980]: Sent: 112040.939469599 Recv: 112052.369935063 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[981]: Sent: 112041.076044224 Recv: 112052.453843855 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 72   ServerImgID: 72   Rejected: No
[#CLIENT#] R[982]: Sent: 112041.209333224 Recv: 112052.756042771 Opcode: IMG_BLUR        OW: 1 ClientImgID: 101  ServerImgID: 101  Rejected: No
[#CLIENT#] R[983]: Sent: 112041.539058558 Recv: 112041.573867058 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 133  Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[984]: Sent: 112041.582983641 Recv: 112052.774168271 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 79   ServerImgID: 79   Rejected: No HASH: ef8229e5c754a6f351669a8d377268c2
[#CLIENT#] R[985]: Sent: 112041.630722724 Recv: 112053.006279688 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 80   ServerImgID: 80   Rejected: No
[#CLIENT#] R[986]: Sent: 112041.915041975 Recv: 112053.271501105 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[987]: Sent: 112041.915181266 Recv: 112053.291345938 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 53   ServerImgID: 53   Rejected: No HASH: 1f1c8796819b3be90020a1649fbceb45
[#CLIENT#] R[988]: Sent: 112041.953934225 Recv: 112041.971689683 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 134  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[989]: Sent: 112042.083190058 Recv: 112053.570806314 Opcode: IMG_BLUR        OW: 1 ClientImgID: 63   ServerImgID: 63   Rejected: No
[#CLIENT#] R[990]: Sent: 112042.587644142 Recv: 112053.655041272 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 89   ServerImgID: 89   Rejected: No
[#CLIENT#] R[991]: Sent: 112042.673252308 Recv: 112053.711963647 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 90   ServerImgID: 90   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[992]: Sent: 112043.066433725 Recv: 112043.119150725 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 135  Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[993]: Sent: 112043.275190350 Recv: 112053.955662480 Opcode: IMG_BLUR        OW: 1 ClientImgID: 84   ServerImgID: 84   Rejected: No
[#CLIENT#] R[994]: Sent: 112043.446445600 Recv: 112054.039891022 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 124  ServerImgID: 124  Rejected: No
[#CLIENT#] R[995]: Sent: 112043.523654642 Recv: 112054.058279855 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 72   ServerImgID: 72   Rejected: No HASH: 5ea1fa06c4cda67fa5c705c720733694
[#CLIENT#] R[996]: Sent: 112043.962678976 Recv: 112054.303733731 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 85   ServerImgID: 85   Rejected: No
[#CLIENT#] R[997]: Sent: 112044.000520184 Recv: 112054.604265397 Opcode: IMG_BLUR        OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[998]: Sent: 112044.024707434 Recv: 112054.640409189 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 102  ServerImgID: 102  Rejected: No HASH: 2789dd1ef70d8504357a520edd47d455
[#CLIENT#] R[999]: Sent: 112044.172334934 Recv: 112044.190140309 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 136  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31"""

run2 = """[#CLIENT#] R[0]: Sent: 112079.232141200 Recv: 112079.250688658 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 0    Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[1]: Sent: 112079.434029408 Recv: 112079.521456158 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[2]: Sent: 112079.586991450 Recv: 112079.679139575 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[3]: Sent: 112079.609058867 Recv: 112079.771785450 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[4]: Sent: 112079.641641200 Recv: 112079.790712825 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No HASH: 2326e8a964742d53375a7edba55f44a4
[#CLIENT#] R[5]: Sent: 112079.740836242 Recv: 112079.759678742 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 1    Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[6]: Sent: 112080.063663033 Recv: 112080.119805617 Opcode: IMG_BLUR        OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[7]: Sent: 112080.190212909 Recv: 112080.223968742 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[8]: Sent: 112080.225612825 Recv: 112080.331779409 Opcode: IMG_BLUR        OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[9]: Sent: 112080.388728700 Recv: 112080.406483825 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[10]: Sent: 112080.406534700 Recv: 112080.493613825 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[11]: Sent: 112080.431195950 Recv: 112080.657068242 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[12]: Sent: 112080.526077117 Recv: 112080.698080492 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[13]: Sent: 112080.600474450 Recv: 112080.719513575 Opcode: IMG_BLUR        OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[14]: Sent: 112080.635142659 Recv: 112080.883384617 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[15]: Sent: 112080.782122992 Recv: 112081.055228659 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[16]: Sent: 112080.815496076 Recv: 112081.111340159 Opcode: IMG_BLUR        OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[17]: Sent: 112081.066896659 Recv: 112081.195369451 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[18]: Sent: 112081.141619326 Recv: 112081.236155617 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[19]: Sent: 112081.250502492 Recv: 112081.336216701 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[20]: Sent: 112081.257170784 Recv: 112081.392300409 Opcode: IMG_BLUR        OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[21]: Sent: 112081.263719034 Recv: 112081.555558618 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[22]: Sent: 112081.496278909 Recv: 112081.675957951 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[23]: Sent: 112081.573963201 Recv: 112081.675903243 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 3    Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[24]: Sent: 112081.747783576 Recv: 112081.802384201 Opcode: IMG_BLUR        OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[25]: Sent: 112081.751847201 Recv: 112081.908122326 Opcode: IMG_BLUR        OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[26]: Sent: 112082.019053451 Recv: 112082.125161993 Opcode: IMG_BLUR        OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[27]: Sent: 112082.153300493 Recv: 112082.244309410 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[28]: Sent: 112082.269782618 Recv: 112082.358277535 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[29]: Sent: 112082.481973701 Recv: 112082.588907243 Opcode: IMG_BLUR        OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[30]: Sent: 112082.508066743 Recv: 112082.729026618 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[31]: Sent: 112082.624202410 Recv: 112082.729021160 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[32]: Sent: 112082.836142118 Recv: 112082.920048785 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[33]: Sent: 112083.093934493 Recv: 112083.111450410 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 5    Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[34]: Sent: 112083.226743910 Recv: 112083.717945785 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[35]: Sent: 112083.251122660 Recv: 112083.801480619 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[36]: Sent: 112083.267121077 Recv: 112083.893145327 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[37]: Sent: 112083.323700452 Recv: 112083.901170535 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[38]: Sent: 112083.477924660 Recv: 112083.919598410 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No HASH: c9e9acb37a12747a13739fb3fe21a308
[#CLIENT#] R[39]: Sent: 112083.503608702 Recv: 112084.016954244 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No HASH: 55f606719c1033a44269b8e4136e8211
[#CLIENT#] R[40]: Sent: 112083.584945160 Recv: 112084.385193911 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[41]: Sent: 112083.822304869 Recv: 112084.851496077 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[42]: Sent: 112083.890767452 Recv: 112084.940111911 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[43]: Sent: 112084.164184327 Recv: 112085.402569911 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[44]: Sent: 112084.302830827 Recv: 112085.866777745 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[45]: Sent: 112084.329331786 Recv: 112084.347841202 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 6    Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[46]: Sent: 112084.364119577 Recv: 112085.950835161 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[47]: Sent: 112084.521929077 Recv: 112086.437876370 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[48]: Sent: 112084.529737952 Recv: 112086.928318162 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[49]: Sent: 112084.603516202 Recv: 112087.414076912 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[50]: Sent: 112084.763458369 Recv: 112087.585775204 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[51]: Sent: 112085.105928244 Recv: 112088.055511953 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[52]: Sent: 112085.115805828 Recv: 112088.073510953 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No HASH: 88580d74c84ac71f83f497a49312521b
[#CLIENT#] R[53]: Sent: 112085.123998411 Recv: 112085.229931036 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 7    Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[54]: Sent: 112085.291848869 Recv: 112088.354989620 Opcode: IMG_BLUR        OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[55]: Sent: 112085.432845203 Recv: 112088.443840620 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[56]: Sent: 112086.628442870 Recv: 112088.946728079 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[57]: Sent: 112086.641938787 Recv: 112089.392633787 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[58]: Sent: 112086.846436912 Recv: 112086.864891078 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 8    Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[59]: Sent: 112087.121422829 Recv: 112089.431669204 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[60]: Sent: 112087.139369662 Recv: 112089.505861246 Opcode: IMG_BLUR        OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[61]: Sent: 112087.310738120 Recv: 112089.523997371 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No HASH: 88580d74c84ac71f83f497a49312521b
[#CLIENT#] R[62]: Sent: 112087.397469412 Recv: 112089.971075538 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[63]: Sent: 112087.408032370 Recv: 112090.027086413 Opcode: IMG_BLUR        OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[64]: Sent: 112087.444354079 Recv: 112090.067503579 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[65]: Sent: 112087.654469370 Recv: 112090.530825121 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[66]: Sent: 112087.658122370 Recv: 112090.618013788 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[67]: Sent: 112087.917757995 Recv: 112090.725761746 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No HASH: 3b45556ca43a453c23cddf80da7af879
[#CLIENT#] R[68]: Sent: 112088.306340078 Recv: 112090.760924996 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No HASH: 732a5bde390f582e4cfff5c80094733c
[#CLIENT#] R[69]: Sent: 112088.717484037 Recv: 112090.928674871 Opcode: IMG_BLUR        OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[70]: Sent: 112088.735456912 Recv: 112088.787423829 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 9    Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[71]: Sent: 112088.795441954 Recv: 112091.393404288 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[72]: Sent: 112088.894778787 Recv: 112088.946703495 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 10   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[73]: Sent: 112088.984756995 Recv: 112091.434073080 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[74]: Sent: 112088.992502162 Recv: 112091.664733997 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[75]: Sent: 112089.097830912 Recv: 112091.699487372 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No HASH: 732a5bde390f582e4cfff5c80094733c
[#CLIENT#] R[76]: Sent: 112089.130715996 Recv: 112091.699507413 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[77]: Sent: 112089.142769204 Recv: 112091.921881539 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[78]: Sent: 112089.431622996 Recv: 112092.384903539 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[79]: Sent: 112089.619874454 Recv: 112092.402924497 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No HASH: 5270006985a5f40de12fea9382d69f27
[#CLIENT#] R[80]: Sent: 112089.662241954 Recv: 112092.402944622 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[81]: Sent: 112089.688912621 Recv: 112092.476503664 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[82]: Sent: 112089.754728121 Recv: 112092.938722414 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[83]: Sent: 112089.775043829 Recv: 112093.402650998 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[84]: Sent: 112089.828512954 Recv: 112093.445892164 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[85]: Sent: 112089.930078621 Recv: 112089.947541496 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 11   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[86]: Sent: 112090.041488329 Recv: 112093.502381789 Opcode: IMG_BLUR        OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[87]: Sent: 112090.081363829 Recv: 112093.589365539 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[88]: Sent: 112090.335149079 Recv: 112093.695367081 Opcode: IMG_BLUR        OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[89]: Sent: 112090.364950121 Recv: 112093.752218789 Opcode: IMG_BLUR        OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[90]: Sent: 112090.395169204 Recv: 112093.807950331 Opcode: IMG_BLUR        OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[91]: Sent: 112090.405039079 Recv: 112093.852951789 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[92]: Sent: 112090.491036704 Recv: 112093.941462664 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[93]: Sent: 112090.525151330 Recv: 112094.102860165 Opcode: IMG_BLUR        OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[94]: Sent: 112090.565192163 Recv: 112094.266644331 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[95]: Sent: 112090.565593413 Recv: 112094.570431040 Opcode: IMG_BLUR        OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[96]: Sent: 112090.586462871 Recv: 112095.033982457 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[97]: Sent: 112090.837737955 Recv: 112095.052106790 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No HASH: 70cf2014ae70367eb9f0b3a744d9fc82
[#CLIENT#] R[98]: Sent: 112090.850711871 Recv: 112095.497892999 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[99]: Sent: 112090.999606288 Recv: 112095.602636374 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[100]: Sent: 112091.197704080 Recv: 112095.676781957 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[101]: Sent: 112091.277202122 Recv: 112095.733317415 Opcode: IMG_BLUR        OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[102]: Sent: 112091.517695872 Recv: 112095.820201874 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[103]: Sent: 112091.603610622 Recv: 112091.637944163 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 12   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[104]: Sent: 112091.837869330 Recv: 112095.826971249 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[105]: Sent: 112092.026960914 Recv: 112095.911015624 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[106]: Sent: 112092.046898580 Recv: 112095.953950915 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[107]: Sent: 112092.061907205 Recv: 112096.040455457 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[108]: Sent: 112092.244110080 Recv: 112096.290190666 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[109]: Sent: 112092.269369580 Recv: 112096.398932457 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No HASH: 57886e6e07fbc6d6f889d8409e86a1dd
[#CLIENT#] R[110]: Sent: 112092.284283205 Recv: 112096.398941457 Opcode: IMG_BLUR        OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[111]: Sent: 112092.553023372 Recv: 112096.842583666 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[112]: Sent: 112092.734433914 Recv: 112096.883055041 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[113]: Sent: 112092.775311206 Recv: 112092.793069039 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 13   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[114]: Sent: 112092.886968497 Recv: 112097.181767708 Opcode: IMG_BLUR        OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[115]: Sent: 112092.894586747 Recv: 112097.343066166 Opcode: IMG_BLUR        OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[116]: Sent: 112092.939800456 Recv: 112097.806916791 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[117]: Sent: 112092.949398456 Recv: 112097.895121208 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[118]: Sent: 112093.037062122 Recv: 112098.056792041 Opcode: IMG_BLUR        OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[119]: Sent: 112093.180564289 Recv: 112098.113348666 Opcode: IMG_BLUR        OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[120]: Sent: 112093.395239873 Recv: 112098.219946125 Opcode: IMG_BLUR        OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[121]: Sent: 112093.418623623 Recv: 112098.683992208 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[122]: Sent: 112093.595869206 Recv: 112099.148035792 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[123]: Sent: 112093.635399914 Recv: 112099.250718500 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No HASH: abaacf2afea051f6c7f8d2df54564402
[#CLIENT#] R[124]: Sent: 112094.054434498 Recv: 112099.250726750 Opcode: IMG_BLUR        OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[125]: Sent: 112094.069157040 Recv: 112099.250737084 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[126]: Sent: 112094.222168498 Recv: 112099.322768334 Opcode: IMG_BLUR        OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[127]: Sent: 112094.234431456 Recv: 112099.585793209 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[128]: Sent: 112094.239490331 Recv: 112099.850780334 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[129]: Sent: 112094.362604123 Recv: 112100.100356334 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[130]: Sent: 112094.563146665 Recv: 112100.184579126 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[131]: Sent: 112094.611580623 Recv: 112100.203683084 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No HASH: 60a1e239cb4ca19a0edb461e80133d15
[#CLIENT#] R[132]: Sent: 112094.777283123 Recv: 112100.269534667 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[133]: Sent: 112094.782840790 Recv: 112094.835751748 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 14   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[134]: Sent: 112094.953528165 Recv: 112100.312457793 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[135]: Sent: 112095.052116707 Recv: 112100.319516584 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[136]: Sent: 112095.142569498 Recv: 112100.411036543 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[137]: Sent: 112095.362267540 Recv: 112100.417812334 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[138]: Sent: 112095.456457957 Recv: 112100.681673126 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[139]: Sent: 112095.547185999 Recv: 112095.602600957 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 15   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[140]: Sent: 112095.609872624 Recv: 112100.931783334 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[141]: Sent: 112095.628507874 Recv: 112101.181600668 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[142]: Sent: 112095.803854040 Recv: 112101.235281001 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No HASH: 07713d772d0b67e8304db40f99efce2f
[#CLIENT#] R[143]: Sent: 112096.014512207 Recv: 112101.353116668 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[144]: Sent: 112096.122219499 Recv: 112101.355469626 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[145]: Sent: 112096.272907291 Recv: 112101.845333752 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[146]: Sent: 112096.398950541 Recv: 112101.899786960 Opcode: IMG_BLUR        OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[147]: Sent: 112096.493806082 Recv: 112101.918718543 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No HASH: ac3c20fe392ffe1675d760e0acc0325d
[#CLIENT#] R[148]: Sent: 112096.646312416 Recv: 112101.918730127 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[149]: Sent: 112096.697636791 Recv: 112102.071068168 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[150]: Sent: 112096.723941249 Recv: 112102.157720960 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[151]: Sent: 112096.740789624 Recv: 112102.179057252 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[152]: Sent: 112096.788659999 Recv: 112102.337985710 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[153]: Sent: 112096.922438541 Recv: 112102.862890169 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[154]: Sent: 112097.002865416 Recv: 112102.989698210 Opcode: IMG_BLUR        OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[155]: Sent: 112097.168880583 Recv: 112103.476205461 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[156]: Sent: 112097.272759916 Recv: 112103.633865419 Opcode: IMG_BLUR        OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[157]: Sent: 112097.458606999 Recv: 112103.638455419 Opcode: IMG_BLUR        OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[158]: Sent: 112097.531778708 Recv: 112104.128602586 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[159]: Sent: 112097.658733708 Recv: 112104.391619794 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[160]: Sent: 112097.675377166 Recv: 112104.862367128 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[161]: Sent: 112097.791185291 Recv: 112104.946163753 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[162]: Sent: 112097.911735250 Recv: 112105.246159337 Opcode: IMG_BLUR        OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[163]: Sent: 112097.912348500 Recv: 112097.965052458 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 16   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[164]: Sent: 112098.071583833 Recv: 112105.496174128 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[165]: Sent: 112098.113366541 Recv: 112098.131544041 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 17   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[166]: Sent: 112098.237497292 Recv: 112105.668613212 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[167]: Sent: 112098.258152375 Recv: 112105.832565337 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[168]: Sent: 112098.434764083 Recv: 112105.916144295 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[169]: Sent: 112098.456009708 Recv: 112105.934933004 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No HASH: 2b87ba29a04361673e6c89b35bde43d4
[#CLIENT#] R[170]: Sent: 112098.659293708 Recv: 112106.404478129 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[171]: Sent: 112098.928937084 Recv: 112106.491611837 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[172]: Sent: 112099.009205417 Recv: 112106.575957171 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[173]: Sent: 112099.089708375 Recv: 112106.600916504 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[174]: Sent: 112099.258050667 Recv: 112106.707987629 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No HASH: a70bdc3cdf2b54142b30883214c9c99c
[#CLIENT#] R[175]: Sent: 112099.794136542 Recv: 112099.812654334 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 18   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[176]: Sent: 112100.020012084 Recv: 112106.707996671 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[177]: Sent: 112100.162583126 Recv: 112106.750819171 Opcode: IMG_BLUR        OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[178]: Sent: 112100.203693042 Recv: 112106.856808462 Opcode: IMG_BLUR        OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[179]: Sent: 112100.221990626 Recv: 112106.896175754 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[180]: Sent: 112100.428404126 Recv: 112106.914335171 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No HASH: 18743a90a1c8b73697150fda5f9497ce
[#CLIENT#] R[181]: Sent: 112100.523124126 Recv: 112107.016502379 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No HASH: 13498c3ae65af1245b92c44175fe9e20
[#CLIENT#] R[182]: Sent: 112100.600525251 Recv: 112107.016515046 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[183]: Sent: 112100.603943793 Recv: 112100.621714543 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 19   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[184]: Sent: 112100.800470459 Recv: 112107.261134962 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[185]: Sent: 112100.867810293 Recv: 112107.279542921 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No HASH: fe98aaa171a54ea15946e81aba274db1
[#CLIENT#] R[186]: Sent: 112101.036260918 Recv: 112107.298051671 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No HASH: 18743a90a1c8b73697150fda5f9497ce
[#CLIENT#] R[187]: Sent: 112101.096477835 Recv: 112107.512246129 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[188]: Sent: 112101.124884251 Recv: 112107.568816713 Opcode: IMG_BLUR        OW: 1 ClientImgID: 17   ServerImgID: 17   Rejected: No
[#CLIENT#] R[189]: Sent: 112101.251369085 Recv: 112101.353111960 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 20   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[190]: Sent: 112101.440516710 Recv: 112101.543408835 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 21   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[191]: Sent: 112102.076609043 Recv: 112108.032813588 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[192]: Sent: 112102.179035460 Recv: 112108.196704796 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[193]: Sent: 112102.203891585 Recv: 112108.280623255 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[194]: Sent: 112102.337857127 Recv: 112108.299251880 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[195]: Sent: 112102.528039752 Recv: 112108.317952838 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 17   ServerImgID: 17   Rejected: No HASH: 1d58d784c91555c8541eca0755b4bb5a
[#CLIENT#] R[196]: Sent: 112102.757494419 Recv: 112102.862884835 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 22   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[197]: Sent: 112102.939788377 Recv: 112108.335851671 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No HASH: d0786a5de39ca03211ddc5c71ef9d5da
[#CLIENT#] R[198]: Sent: 112103.239131169 Recv: 112108.372415963 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[199]: Sent: 112103.581223919 Recv: 112103.633874961 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 23   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[200]: Sent: 112103.785403336 Recv: 112108.456152171 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[201]: Sent: 112103.815225378 Recv: 112108.474762130 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 17   ServerImgID: 17   Rejected: No HASH: 1d58d784c91555c8541eca0755b4bb5a
[#CLIENT#] R[202]: Sent: 112103.855570336 Recv: 112108.706233755 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[203]: Sent: 112103.936519711 Recv: 112108.763458130 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No HASH: dbc5cfa2ed2144a04653f8fe75f6fb2e
[#CLIENT#] R[204]: Sent: 112104.001586669 Recv: 112108.820667297 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No HASH: 83af9aa159e73eca99768998d53faa35
[#CLIENT#] R[205]: Sent: 112104.249975878 Recv: 112108.820679588 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 17   ServerImgID: 17   Rejected: No
[#CLIENT#] R[206]: Sent: 112104.450667711 Recv: 112108.839720880 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No HASH: d0786a5de39ca03211ddc5c71ef9d5da
[#CLIENT#] R[207]: Sent: 112104.472913211 Recv: 112108.857808880 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No HASH: 9501a7ff4534a1193b3fc6fa69efaad3
[#CLIENT#] R[208]: Sent: 112104.585830128 Recv: 112108.857817797 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[209]: Sent: 112104.668169253 Recv: 112104.774145211 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 24   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[210]: Sent: 112104.776064086 Recv: 112108.861332422 Opcode: IMG_BLUR        OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[211]: Sent: 112105.033439170 Recv: 112109.043603213 Opcode: IMG_BLUR        OW: 1 ClientImgID: 16   ServerImgID: 16   Rejected: No
[#CLIENT#] R[212]: Sent: 112105.251703587 Recv: 112109.285587672 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[213]: Sent: 112105.311175170 Recv: 112109.369237339 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[214]: Sent: 112105.413106503 Recv: 112109.835939214 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 21   ServerImgID: 21   Rejected: No
[#CLIENT#] R[215]: Sent: 112105.447800503 Recv: 112110.007335505 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[216]: Sent: 112105.677533837 Recv: 112110.027913255 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[217]: Sent: 112105.709453170 Recv: 112110.118740797 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[218]: Sent: 112105.910235170 Recv: 112110.143549047 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[219]: Sent: 112106.168742337 Recv: 112110.646918547 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[220]: Sent: 112106.187117379 Recv: 112110.653936756 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[221]: Sent: 112106.206524920 Recv: 112110.661730589 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No
[#CLIENT#] R[222]: Sent: 112106.500168795 Recv: 112111.020630423 Opcode: IMG_BLUR        OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[223]: Sent: 112106.513009795 Recv: 112111.131084923 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[224]: Sent: 112106.759826754 Recv: 112111.150546423 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No HASH: 56dce5d5ef77a4d1b70bb5f0ede39c26
[#CLIENT#] R[225]: Sent: 112106.767179837 Recv: 112111.211700964 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No HASH: 9559d5665fccb0cf0ca4a5cb2425a4e9
[#CLIENT#] R[226]: Sent: 112106.824586337 Recv: 112111.211719298 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No
[#CLIENT#] R[227]: Sent: 112107.068121712 Recv: 112111.621963215 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 22   ServerImgID: 22   Rejected: No
[#CLIENT#] R[228]: Sent: 112107.071697462 Recv: 112111.621972756 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[229]: Sent: 112107.211710671 Recv: 112111.629733506 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[230]: Sent: 112107.215406921 Recv: 112112.128265131 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[231]: Sent: 112107.323878004 Recv: 112112.151463006 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[232]: Sent: 112107.544063296 Recv: 112112.326216423 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[233]: Sent: 112107.549253838 Recv: 112112.431716673 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[234]: Sent: 112107.669267004 Recv: 112112.891288590 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[235]: Sent: 112107.706841254 Recv: 112112.994826840 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 21   ServerImgID: 21   Rejected: No HASH: 22286fe7eb8d021fb7fb11f7614799bf
[#CLIENT#] R[236]: Sent: 112107.872623921 Recv: 112112.994846340 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 16   ServerImgID: 16   Rejected: No
[#CLIENT#] R[237]: Sent: 112107.878155588 Recv: 112107.930564838 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 25   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[238]: Sent: 112107.958569671 Recv: 112112.994897174 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[239]: Sent: 112107.964612088 Recv: 112113.043600507 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[240]: Sent: 112107.970402463 Recv: 112113.108485632 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[241]: Sent: 112108.000125421 Recv: 112108.017719338 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 26   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[242]: Sent: 112108.105463588 Recv: 112113.276343882 Opcode: IMG_BLUR        OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[243]: Sent: 112108.365966796 Recv: 112113.366195924 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[244]: Sent: 112108.496755421 Recv: 112113.411265674 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 22   ServerImgID: 22   Rejected: No
[#CLIENT#] R[245]: Sent: 112108.597248338 Recv: 112113.897459591 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[246]: Sent: 112108.865438422 Recv: 112113.984168091 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[247]: Sent: 112108.939427838 Recv: 112109.043521338 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 27   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[248]: Sent: 112109.157461672 Recv: 112114.075062257 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No
[#CLIENT#] R[249]: Sent: 112109.188847380 Recv: 112114.375010716 Opcode: IMG_BLUR        OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[250]: Sent: 112109.213021255 Recv: 112114.838124633 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[251]: Sent: 112109.328125672 Recv: 112115.307974258 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 22   ServerImgID: 22   Rejected: No
[#CLIENT#] R[252]: Sent: 112109.519521797 Recv: 112115.401643258 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No
[#CLIENT#] R[253]: Sent: 112109.629856464 Recv: 112115.485675091 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[254]: Sent: 112109.658704339 Recv: 112115.504094258 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No HASH: 56dce5d5ef77a4d1b70bb5f0ede39c26
[#CLIENT#] R[255]: Sent: 112109.731044005 Recv: 112115.749360383 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[256]: Sent: 112109.806868297 Recv: 112115.840007342 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[257]: Sent: 112109.940432255 Recv: 112115.858245050 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No HASH: 98b9ed3ea6eae02e2969162cccbd71f7
[#CLIENT#] R[258]: Sent: 112109.944987797 Recv: 112116.330809175 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 22   ServerImgID: 22   Rejected: No
[#CLIENT#] R[259]: Sent: 112110.011811339 Recv: 112116.492544634 Opcode: IMG_BLUR        OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[260]: Sent: 112110.183450589 Recv: 112116.533326300 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[261]: Sent: 112110.191677839 Recv: 112116.795134300 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 16   ServerImgID: 16   Rejected: No
[#CLIENT#] R[262]: Sent: 112110.448631797 Recv: 112116.879551717 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[263]: Sent: 112110.476822131 Recv: 112117.181080551 Opcode: IMG_BLUR        OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[264]: Sent: 112110.486669506 Recv: 112110.522310881 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 28   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[265]: Sent: 112110.540499589 Recv: 112117.235546842 Opcode: IMG_BLUR        OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[266]: Sent: 112110.690891464 Recv: 112117.340889801 Opcode: IMG_BLUR        OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[267]: Sent: 112110.824393089 Recv: 112117.360275384 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No HASH: 6eea4bd5c0b7ead532c334eea7ccd250
[#CLIENT#] R[268]: Sent: 112110.834657714 Recv: 112117.428510301 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[269]: Sent: 112110.845501464 Recv: 112117.484788884 Opcode: IMG_BLUR        OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[270]: Sent: 112111.011559923 Recv: 112117.571155384 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No
[#CLIENT#] R[271]: Sent: 112111.044131214 Recv: 112117.677197801 Opcode: IMG_BLUR        OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[272]: Sent: 112111.211730214 Recv: 112111.321596423 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 29   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[273]: Sent: 112111.508233506 Recv: 112117.717470842 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[274]: Sent: 112111.569318840 Recv: 112111.621956631 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 30   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[275]: Sent: 112111.661090631 Recv: 112117.966649800 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[276]: Sent: 112111.669649923 Recv: 112118.305109467 Opcode: IMG_BLUR        OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[277]: Sent: 112111.777549090 Recv: 112118.306329467 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 29   ServerImgID: 29   Rejected: No
[#CLIENT#] R[278]: Sent: 112111.864981298 Recv: 112118.769043592 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 29   ServerImgID: 29   Rejected: No
[#CLIENT#] R[279]: Sent: 112111.940363715 Recv: 112112.048025090 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 31   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[280]: Sent: 112112.194227173 Recv: 112118.941811884 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[281]: Sent: 112112.266688007 Recv: 112119.195144092 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[282]: Sent: 112112.327022507 Recv: 112112.431666507 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 32   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[283]: Sent: 112112.488577465 Recv: 112119.250235217 Opcode: IMG_BLUR        OW: 1 ClientImgID: 26   ServerImgID: 26   Rejected: No
[#CLIENT#] R[284]: Sent: 112112.502181298 Recv: 112119.334437759 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[285]: Sent: 112112.653809465 Recv: 112119.803440259 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 22   ServerImgID: 22   Rejected: No
[#CLIENT#] R[286]: Sent: 112112.994857215 Recv: 112120.269716218 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[287]: Sent: 112112.999765757 Recv: 112113.018185507 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 33   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[288]: Sent: 112113.281129840 Recv: 112120.324753801 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 25   ServerImgID: 25   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[289]: Sent: 112113.371874132 Recv: 112120.324764634 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 33   ServerImgID: 33   Rejected: No
[#CLIENT#] R[290]: Sent: 112113.449466757 Recv: 112120.367226676 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[291]: Sent: 112113.535731215 Recv: 112120.422465759 Opcode: IMG_BLUR        OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[292]: Sent: 112113.691511216 Recv: 112120.440964843 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 33   ServerImgID: 33   Rejected: No HASH: a46fa185b469892706544a2d486bf142
[#CLIENT#] R[293]: Sent: 112113.701848424 Recv: 112113.737078549 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 34   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[294]: Sent: 112113.874570674 Recv: 112120.887187551 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No
[#CLIENT#] R[295]: Sent: 112114.052743424 Recv: 112120.930314718 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 21   ServerImgID: 21   Rejected: No
[#CLIENT#] R[296]: Sent: 112114.125410049 Recv: 112121.394425218 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[297]: Sent: 112114.211944841 Recv: 112121.412811260 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 17   ServerImgID: 17   Rejected: No HASH: 87504e6eb7330f31ab17020c33a18aa9
[#CLIENT#] R[298]: Sent: 112114.353048341 Recv: 112121.518871968 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[299]: Sent: 112114.368673716 Recv: 112121.679434635 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[300]: Sent: 112114.554777633 Recv: 112121.980289302 Opcode: IMG_BLUR        OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No
[#CLIENT#] R[301]: Sent: 112114.664791424 Recv: 112122.064380094 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[302]: Sent: 112114.884183633 Recv: 112122.527281302 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No
[#CLIENT#] R[303]: Sent: 112114.915772841 Recv: 112122.552460552 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[304]: Sent: 112115.023057633 Recv: 112122.566592885 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 28   ServerImgID: 28   Rejected: No
[#CLIENT#] R[305]: Sent: 112115.093891300 Recv: 112122.656530969 Opcode: IMG_BLUR        OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[306]: Sent: 112115.109339383 Recv: 112122.872538636 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[307]: Sent: 112115.212872925 Recv: 112115.230510341 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 35   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[308]: Sent: 112115.342626925 Recv: 112122.959164052 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[309]: Sent: 112115.510377341 Recv: 112115.544429508 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 36   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[310]: Sent: 112115.633727300 Recv: 112115.652116466 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 37   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[311]: Sent: 112115.801057467 Recv: 112123.122126886 Opcode: IMG_BLUR        OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[312]: Sent: 112116.013181092 Recv: 112123.386533344 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[313]: Sent: 112116.057844050 Recv: 112123.492542219 Opcode: IMG_BLUR        OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[314]: Sent: 112116.162190800 Recv: 112123.796987844 Opcode: IMG_BLUR        OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[315]: Sent: 112116.365880425 Recv: 112124.262261053 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[316]: Sent: 112116.529867759 Recv: 112124.725984887 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 29   ServerImgID: 29   Rejected: No
[#CLIENT#] R[317]: Sent: 112116.575647592 Recv: 112116.593484259 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 38   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[318]: Sent: 112116.684978759 Recv: 112124.774523095 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[319]: Sent: 112116.741654759 Recv: 112124.880371303 Opcode: IMG_BLUR        OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[320]: Sent: 112116.803432050 Recv: 112124.980191095 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[321]: Sent: 112116.828873009 Recv: 112125.430613137 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No
[#CLIENT#] R[322]: Sent: 112116.864740842 Recv: 112125.515178970 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 35   ServerImgID: 35   Rejected: No
[#CLIENT#] R[323]: Sent: 112116.930225925 Recv: 112125.599340554 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[324]: Sent: 112117.126111134 Recv: 112125.643818887 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 28   ServerImgID: 28   Rejected: No
[#CLIENT#] R[325]: Sent: 112117.146595092 Recv: 112125.702177762 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 38   ServerImgID: 38   Rejected: No
[#CLIENT#] R[326]: Sent: 112117.180733509 Recv: 112125.722934762 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[327]: Sent: 112117.297126551 Recv: 112125.985917929 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 23   ServerImgID: 23   Rejected: No
[#CLIENT#] R[328]: Sent: 112117.618385759 Recv: 112125.992744887 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[329]: Sent: 112117.815986425 Recv: 112117.833659133 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 39   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[330]: Sent: 112117.910448508 Recv: 112126.077138679 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[331]: Sent: 112118.086899592 Recv: 112126.084456929 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No
[#CLIENT#] R[332]: Sent: 112118.138971342 Recv: 112126.188403762 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No HASH: 443973423be9f977eba85b1a8c0f41a9
[#CLIENT#] R[333]: Sent: 112118.155918175 Recv: 112126.188425804 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[334]: Sent: 112118.198675342 Recv: 112118.305103175 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 40   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[335]: Sent: 112118.407378384 Recv: 112126.188431179 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 17   ServerImgID: 17   Rejected: No
[#CLIENT#] R[336]: Sent: 112118.485357384 Recv: 112126.225309721 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 27   ServerImgID: 27   Rejected: No
[#CLIENT#] R[337]: Sent: 112118.506662884 Recv: 112126.328020637 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No HASH: 15cbf08ec384eb4822b847c3b349f691
[#CLIENT#] R[338]: Sent: 112118.533665217 Recv: 112126.391716721 Opcode: IMG_BLUR        OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[339]: Sent: 112118.576688509 Recv: 112126.520893679 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 26   ServerImgID: 26   Rejected: No
[#CLIENT#] R[340]: Sent: 112118.618831759 Recv: 112126.724253512 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 16   ServerImgID: 16   Rejected: No
[#CLIENT#] R[341]: Sent: 112118.784665134 Recv: 112118.803021800 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 41   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[342]: Sent: 112118.876702342 Recv: 112118.928625259 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 42   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[343]: Sent: 112118.973097509 Recv: 112126.808210013 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[344]: Sent: 112119.088123050 Recv: 112119.140427426 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 43   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[345]: Sent: 112119.155550926 Recv: 112127.275740388 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[346]: Sent: 112119.247344134 Recv: 112127.330371971 Opcode: IMG_BLUR        OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[347]: Sent: 112119.450754092 Recv: 112119.468548884 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 44   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[348]: Sent: 112119.506118301 Recv: 112127.793627471 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 22   ServerImgID: 22   Rejected: No
[#CLIENT#] R[349]: Sent: 112119.582215967 Recv: 112127.896589013 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No HASH: 09265369a030e219fcd2d80a99ded564
[#CLIENT#] R[350]: Sent: 112119.901131218 Recv: 112127.896598221 Opcode: IMG_BLUR        OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[351]: Sent: 112119.906654384 Recv: 112120.013099093 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 45   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[352]: Sent: 112120.017164259 Recv: 112128.155154346 Opcode: IMG_BLUR        OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[353]: Sent: 112120.042074593 Recv: 112120.147816759 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 46   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[354]: Sent: 112120.155469884 Recv: 112128.638357763 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No
[#CLIENT#] R[355]: Sent: 112120.217182176 Recv: 112128.810797638 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[356]: Sent: 112120.324775343 Recv: 112128.917661555 Opcode: IMG_BLUR        OW: 1 ClientImgID: 34   ServerImgID: 34   Rejected: No
[#CLIENT#] R[357]: Sent: 112120.440983634 Recv: 112129.006846347 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[358]: Sent: 112120.505555718 Recv: 112120.524124926 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 47   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[359]: Sent: 112120.791317051 Recv: 112129.257014139 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 25   ServerImgID: 25   Rejected: No
[#CLIENT#] R[360]: Sent: 112121.022600301 Recv: 112129.275155389 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No HASH: 17f53b44873a51687c7b7eb59caa78d4
[#CLIENT#] R[361]: Sent: 112121.277143177 Recv: 112129.344139097 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No
[#CLIENT#] R[362]: Sent: 112121.518889302 Recv: 112129.361717389 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No HASH: e86ac01aa209232d9ecce0271f9ce47b
[#CLIENT#] R[363]: Sent: 112121.519421802 Recv: 112129.463693055 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No HASH: 2dd00aef69f7247958b4025a2a00fe32
[#CLIENT#] R[364]: Sent: 112121.618209593 Recv: 112129.463700764 Opcode: IMG_BLUR        OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No
[#CLIENT#] R[365]: Sent: 112121.621971343 Recv: 112129.720806389 Opcode: IMG_BLUR        OW: 1 ClientImgID: 21   ServerImgID: 21   Rejected: No
[#CLIENT#] R[366]: Sent: 112121.827636635 Recv: 112129.739010556 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No HASH: e86ac01aa209232d9ecce0271f9ce47b
[#CLIENT#] R[367]: Sent: 112121.940222135 Recv: 112121.957904052 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 48   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[368]: Sent: 112122.059478510 Recv: 112129.761959972 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[369]: Sent: 112122.612734427 Recv: 112122.646839344 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 49   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[370]: Sent: 112122.657327302 Recv: 112130.226152556 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No
[#CLIENT#] R[371]: Sent: 112122.691766344 Recv: 112130.247187472 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 23   ServerImgID: 23   Rejected: No
[#CLIENT#] R[372]: Sent: 112122.739712427 Recv: 112130.350632681 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No HASH: 8aedd77e65db0bdf11484030beb7f7d2
[#CLIENT#] R[373]: Sent: 112122.960043844 Recv: 112130.503053889 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 42   ServerImgID: 42   Rejected: No
[#CLIENT#] R[374]: Sent: 112122.979547261 Recv: 112130.623528056 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[375]: Sent: 112123.239118302 Recv: 112130.681697181 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[376]: Sent: 112123.271441802 Recv: 112130.700195098 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 26   ServerImgID: 26   Rejected: No HASH: 9d73e97ac536ed43ec67b869dac562a7
[#CLIENT#] R[377]: Sent: 112123.447868553 Recv: 112130.771407639 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 33   ServerImgID: 33   Rejected: No
[#CLIENT#] R[378]: Sent: 112123.508196011 Recv: 112130.858334514 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[379]: Sent: 112123.570088178 Recv: 112123.588344344 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 50   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[380]: Sent: 112123.637234344 Recv: 112130.914137473 Opcode: IMG_BLUR        OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No
[#CLIENT#] R[381]: Sent: 112123.658082053 Recv: 112130.953938431 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[382]: Sent: 112123.907487386 Recv: 112130.972523139 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No HASH: 2ec8a864904a738fd306d50b3cd3cf7e
[#CLIENT#] R[383]: Sent: 112124.003205345 Recv: 112124.055716136 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 51   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[384]: Sent: 112124.125410053 Recv: 112130.972538098 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 17   ServerImgID: 17   Rejected: No
[#CLIENT#] R[385]: Sent: 112124.230492636 Recv: 112130.990359098 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 33   ServerImgID: 33   Rejected: No HASH: 0ca2b17283ae8bada714cf75628b9380
[#CLIENT#] R[386]: Sent: 112124.304020803 Recv: 112131.015414640 Opcode: IMG_BLUR        OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[387]: Sent: 112124.416598428 Recv: 112131.478408598 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[388]: Sent: 112124.571938511 Recv: 112131.486434640 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 33   ServerImgID: 33   Rejected: No
[#CLIENT#] R[389]: Sent: 112124.612672595 Recv: 112131.975255598 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[390]: Sent: 112124.640633845 Recv: 112132.011975557 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No HASH: 94cf2cdf5b2100fc3b24dff8d66c2ed5
[#CLIENT#] R[391]: Sent: 112124.694761387 Recv: 112132.058987473 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[392]: Sent: 112124.845252262 Recv: 112132.543899099 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[393]: Sent: 112124.860971970 Recv: 112132.711510515 Opcode: IMG_BLUR        OW: 1 ClientImgID: 43   ServerImgID: 43   Rejected: No
[#CLIENT#] R[394]: Sent: 112124.935189220 Recv: 112124.969255012 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 52   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[395]: Sent: 112125.047316470 Recv: 112132.795620474 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[396]: Sent: 112125.074223428 Recv: 112132.901324599 Opcode: IMG_BLUR        OW: 1 ClientImgID: 34   ServerImgID: 34   Rejected: No
[#CLIENT#] R[397]: Sent: 112125.139035428 Recv: 112133.464957724 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 40   ServerImgID: 40   Rejected: No
[#CLIENT#] R[398]: Sent: 112125.422547720 Recv: 112133.859927308 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 40   ServerImgID: 40   Rejected: No
[#CLIENT#] R[399]: Sent: 112125.453615262 Recv: 112134.155598933 Opcode: IMG_BLUR        OW: 1 ClientImgID: 22   ServerImgID: 22   Rejected: No
[#CLIENT#] R[400]: Sent: 112125.513144345 Recv: 112134.185868933 Opcode: IMG_BLUR        OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[401]: Sent: 112125.601505470 Recv: 112125.619857387 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 53   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[402]: Sent: 112125.976799387 Recv: 112134.204983599 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No HASH: 63462aae85d7bb2238584f421e5321b0
[#CLIENT#] R[403]: Sent: 112126.396704929 Recv: 112134.437055933 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 51   ServerImgID: 51   Rejected: No
[#CLIENT#] R[404]: Sent: 112126.469220054 Recv: 112126.520827387 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 54   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[405]: Sent: 112126.655508804 Recv: 112134.600523891 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 49   ServerImgID: 49   Rejected: No
[#CLIENT#] R[406]: Sent: 112126.743331262 Recv: 112134.762696516 Opcode: IMG_BLUR        OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[407]: Sent: 112126.782488721 Recv: 112134.846844766 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 38   ServerImgID: 38   Rejected: No
[#CLIENT#] R[408]: Sent: 112126.937266971 Recv: 112134.867398766 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[409]: Sent: 112126.993068054 Recv: 112135.031125183 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 49   ServerImgID: 49   Rejected: No
[#CLIENT#] R[410]: Sent: 112127.115298638 Recv: 112135.115383183 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 39   ServerImgID: 39   Rejected: No
[#CLIENT#] R[411]: Sent: 112127.116132638 Recv: 112135.159365600 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No
[#CLIENT#] R[412]: Sent: 112127.190135179 Recv: 112135.261827642 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 40   ServerImgID: 40   Rejected: No HASH: c805a881624da3f0e7f8f6fc6f74044a
[#CLIENT#] R[413]: Sent: 112127.208474846 Recv: 112135.261843933 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 26   ServerImgID: 26   Rejected: No
[#CLIENT#] R[414]: Sent: 112127.289908929 Recv: 112135.335889267 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No
[#CLIENT#] R[415]: Sent: 112127.311455096 Recv: 112135.438376475 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No HASH: d2c3d5995b9441fdf8a21ca59f5bfb21
[#CLIENT#] R[416]: Sent: 112127.441458971 Recv: 112135.603788767 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 42   ServerImgID: 42   Rejected: No
[#CLIENT#] R[417]: Sent: 112127.554893596 Recv: 112136.067420642 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 29   ServerImgID: 29   Rejected: No
[#CLIENT#] R[418]: Sent: 112127.682786263 Recv: 112127.735300138 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 55   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[419]: Sent: 112127.896607305 Recv: 112136.108064600 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[420]: Sent: 112128.050134430 Recv: 112128.155149763 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 56   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[421]: Sent: 112128.203225097 Recv: 112136.268348642 Opcode: IMG_BLUR        OW: 1 ClientImgID: 23   ServerImgID: 23   Rejected: No
[#CLIENT#] R[422]: Sent: 112128.396166138 Recv: 112136.322594934 Opcode: IMG_BLUR        OW: 1 ClientImgID: 35   ServerImgID: 35   Rejected: No
[#CLIENT#] R[423]: Sent: 112128.794981763 Recv: 112136.785937851 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[424]: Sent: 112129.032534347 Recv: 112129.066918514 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 57   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[425]: Sent: 112129.083785764 Recv: 112129.188718430 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 58   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[426]: Sent: 112129.219796430 Recv: 112136.957775392 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 52   ServerImgID: 52   Rejected: No
[#CLIENT#] R[427]: Sent: 112129.285022514 Recv: 112137.012252142 Opcode: IMG_BLUR        OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[428]: Sent: 112129.316137847 Recv: 112137.025637017 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 52   ServerImgID: 52   Rejected: No
[#CLIENT#] R[429]: Sent: 112129.463708972 Recv: 112137.489721143 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[430]: Sent: 112129.572591139 Recv: 112137.739317226 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 43   ServerImgID: 43   Rejected: No
[#CLIENT#] R[431]: Sent: 112129.999157597 Recv: 112138.233496226 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[432]: Sent: 112130.012917514 Recv: 112138.268697768 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 36   ServerImgID: 36   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[433]: Sent: 112130.019184972 Recv: 112138.484658310 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[434]: Sent: 112130.165800431 Recv: 112138.518844768 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 36   ServerImgID: 36   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[435]: Sent: 112130.350647681 Recv: 112138.624396976 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No HASH: 265c37ce11140c300e85e1d7606634c6
[#CLIENT#] R[436]: Sent: 112130.512031389 Recv: 112130.529919014 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 59   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[437]: Sent: 112130.589401764 Recv: 112130.623521306 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 60   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[438]: Sent: 112130.627139931 Recv: 112138.624404935 Opcode: IMG_BLUR        OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No
[#CLIENT#] R[439]: Sent: 112130.670203723 Recv: 112138.624415060 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[440]: Sent: 112130.840491264 Recv: 112138.670734643 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[441]: Sent: 112130.856266306 Recv: 112138.757252143 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[442]: Sent: 112130.897898306 Recv: 112138.775306935 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 33   ServerImgID: 33   Rejected: No HASH: 8424c5f06ec75b6d7be01c9662dba8cc
[#CLIENT#] R[443]: Sent: 112131.157431890 Recv: 112138.848709352 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[444]: Sent: 112131.164509306 Recv: 112138.936991268 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[445]: Sent: 112131.203702681 Recv: 112139.400938060 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 22   ServerImgID: 22   Rejected: No
[#CLIENT#] R[446]: Sent: 112131.423028015 Recv: 112139.423401019 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 25   ServerImgID: 25   Rejected: No
[#CLIENT#] R[447]: Sent: 112131.489993098 Recv: 112139.510221644 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No
[#CLIENT#] R[448]: Sent: 112131.651098765 Recv: 112139.972480685 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No
[#CLIENT#] R[449]: Sent: 112131.730455807 Recv: 112139.991212102 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No HASH: 99904a9a04062db3ec5b5af7eda23f71
[#CLIENT#] R[450]: Sent: 112131.777528848 Recv: 112140.436160144 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 56   ServerImgID: 56   Rejected: No
[#CLIENT#] R[451]: Sent: 112131.784591223 Recv: 112131.802421807 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 61   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[452]: Sent: 112131.803064432 Recv: 112140.773142269 Opcode: IMG_BLUR        OW: 1 ClientImgID: 21   ServerImgID: 21   Rejected: No
[#CLIENT#] R[453]: Sent: 112131.807925682 Recv: 112140.864641769 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No
[#CLIENT#] R[454]: Sent: 112131.826517515 Recv: 112140.908353978 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[455]: Sent: 112131.859606807 Recv: 112141.375437061 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No
[#CLIENT#] R[456]: Sent: 112131.936921390 Recv: 112141.629447020 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 23   ServerImgID: 23   Rejected: No
[#CLIENT#] R[457]: Sent: 112131.960245098 Recv: 112141.720192103 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[458]: Sent: 112132.105092890 Recv: 112141.824209895 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 29   ServerImgID: 29   Rejected: No HASH: 93c6c71a0c9f784606e4a999406c05c6
[#CLIENT#] R[459]: Sent: 112132.170777765 Recv: 112141.824221561 Opcode: IMG_BLUR        OW: 1 ClientImgID: 50   ServerImgID: 50   Rejected: No
[#CLIENT#] R[460]: Sent: 112132.433970057 Recv: 112142.035858186 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 55   ServerImgID: 55   Rejected: No
[#CLIENT#] R[461]: Sent: 112132.580533432 Recv: 112142.050686061 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 57   ServerImgID: 57   Rejected: No
[#CLIENT#] R[462]: Sent: 112133.036137849 Recv: 112142.157768228 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No HASH: 769e766e455d7911c84b1647970036eb
[#CLIENT#] R[463]: Sent: 112133.162773349 Recv: 112142.317967395 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 42   ServerImgID: 42   Rejected: No
[#CLIENT#] R[464]: Sent: 112133.164255349 Recv: 112133.198814974 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 62   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[465]: Sent: 112133.303148474 Recv: 112142.344266020 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 54   ServerImgID: 54   Rejected: No
[#CLIENT#] R[466]: Sent: 112133.352250266 Recv: 112142.399211103 Opcode: IMG_BLUR        OW: 1 ClientImgID: 44   ServerImgID: 44   Rejected: No
[#CLIENT#] R[467]: Sent: 112133.355771932 Recv: 112142.406830978 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 59   ServerImgID: 59   Rejected: No
[#CLIENT#] R[468]: Sent: 112133.359521891 Recv: 112133.464952641 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 63   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[469]: Sent: 112133.521109516 Recv: 112142.710161937 Opcode: IMG_BLUR        OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[470]: Sent: 112133.603975891 Recv: 112143.009145395 Opcode: IMG_BLUR        OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No
[#CLIENT#] R[471]: Sent: 112133.633432807 Recv: 112143.027309854 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 39   ServerImgID: 39   Rejected: No HASH: d4f94469bfe2b5ed7246046002f99653
[#CLIENT#] R[472]: Sent: 112133.738520599 Recv: 112143.097704312 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 44   ServerImgID: 44   Rejected: No
[#CLIENT#] R[473]: Sent: 112133.747931974 Recv: 112143.567050896 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[474]: Sent: 112133.816864808 Recv: 112133.834631308 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 64   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[475]: Sent: 112134.121308308 Recv: 112134.155580224 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 65   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[476]: Sent: 112134.293916391 Recv: 112143.653837021 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 38   ServerImgID: 38   Rejected: No
[#CLIENT#] R[477]: Sent: 112134.457264474 Recv: 112144.142561937 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[478]: Sent: 112134.548182933 Recv: 112144.198225062 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 30   ServerImgID: 30   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[479]: Sent: 112134.809010225 Recv: 112134.827354600 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 66   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[480]: Sent: 112134.868835100 Recv: 112144.198234521 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[481]: Sent: 112134.892844725 Recv: 112144.449563938 Opcode: IMG_BLUR        OW: 1 ClientImgID: 40   ServerImgID: 40   Rejected: No
[#CLIENT#] R[482]: Sent: 112134.987820725 Recv: 112144.536561688 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[483]: Sent: 112135.066868641 Recv: 112144.625486063 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 39   ServerImgID: 39   Rejected: No
[#CLIENT#] R[484]: Sent: 112135.072996100 Recv: 112144.731422479 Opcode: IMG_BLUR        OW: 1 ClientImgID: 65   ServerImgID: 65   Rejected: No
[#CLIENT#] R[485]: Sent: 112135.111753558 Recv: 112144.839057854 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No HASH: 5fbf731145da02fb096ea1d97a956e1e
[#CLIENT#] R[486]: Sent: 112135.261852350 Recv: 112144.839068729 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 49   ServerImgID: 49   Rejected: No
[#CLIENT#] R[487]: Sent: 112135.326112642 Recv: 112144.926989396 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 52   ServerImgID: 52   Rejected: No
[#CLIENT#] R[488]: Sent: 112135.438393267 Recv: 112145.091182480 Opcode: IMG_BLUR        OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[489]: Sent: 112135.471839808 Recv: 112145.263485855 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No
[#CLIENT#] R[490]: Sent: 112135.537150267 Recv: 112145.284195605 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 42   ServerImgID: 42   Rejected: No
[#CLIENT#] R[491]: Sent: 112135.634928017 Recv: 112145.449821855 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 60   ServerImgID: 60   Rejected: No
[#CLIENT#] R[492]: Sent: 112135.701437975 Recv: 112145.917039730 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 21   ServerImgID: 21   Rejected: No
[#CLIENT#] R[493]: Sent: 112135.707219808 Recv: 112145.964968230 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 21   ServerImgID: 21   Rejected: No
[#CLIENT#] R[494]: Sent: 112135.712335225 Recv: 112146.018664563 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No HASH: 8ee92d5fe2cf8dcafc52abe575e551a9
[#CLIENT#] R[495]: Sent: 112135.777973642 Recv: 112146.229752730 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[496]: Sent: 112136.496435642 Recv: 112136.548942017 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 67   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[497]: Sent: 112137.036316267 Recv: 112146.270054438 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 65   ServerImgID: 65   Rejected: No
[#CLIENT#] R[498]: Sent: 112137.104558976 Recv: 112137.122874601 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 68   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[499]: Sent: 112137.200588184 Recv: 112137.235242851 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 69   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[500]: Sent: 112137.317590809 Recv: 112137.335812018 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 70   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[501]: Sent: 112137.348492768 Recv: 112146.404730939 Opcode: IMG_BLUR        OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[502]: Sent: 112137.412140934 Recv: 112146.450456272 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[503]: Sent: 112137.442901851 Recv: 112146.537448272 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 50   ServerImgID: 50   Rejected: No
[#CLIENT#] R[504]: Sent: 112137.532335684 Recv: 112147.029343647 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[505]: Sent: 112137.825835101 Recv: 112147.131858647 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No HASH: d7748f1a206eb62d36a79102083cf548
[#CLIENT#] R[506]: Sent: 112137.858213184 Recv: 112147.131870272 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 57   ServerImgID: 57   Rejected: No
[#CLIENT#] R[507]: Sent: 112137.897974559 Recv: 112137.916168476 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 71   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[508]: Sent: 112138.153207685 Recv: 112147.530662397 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 27   ServerImgID: 27   Rejected: No
[#CLIENT#] R[509]: Sent: 112138.268711560 Recv: 112147.544047481 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 36   ServerImgID: 36   Rejected: No
[#CLIENT#] R[510]: Sent: 112138.313728310 Recv: 112147.711013897 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 65   ServerImgID: 65   Rejected: No
[#CLIENT#] R[511]: Sent: 112138.384182893 Recv: 112148.195146647 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 45   ServerImgID: 45   Rejected: No
[#CLIENT#] R[512]: Sent: 112138.413301560 Recv: 112148.236084272 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[513]: Sent: 112138.437587643 Recv: 112148.245784981 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 16   ServerImgID: 16   Rejected: No
[#CLIENT#] R[514]: Sent: 112138.720391477 Recv: 112148.342093689 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 17   ServerImgID: 17   Rejected: No
[#CLIENT#] R[515]: Sent: 112138.787471768 Recv: 112148.512962856 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 28   ServerImgID: 28   Rejected: No
[#CLIENT#] R[516]: Sent: 112138.807227727 Recv: 112148.769140981 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[517]: Sent: 112138.905538685 Recv: 112148.804176981 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No HASH: 434ea3af0e2fce0af8833464e6fda832
[#CLIENT#] R[518]: Sent: 112138.941596977 Recv: 112148.824731314 Opcode: IMG_BLUR        OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[519]: Sent: 112138.979936518 Recv: 112148.908468939 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[520]: Sent: 112139.293788185 Recv: 112148.915731231 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[521]: Sent: 112139.413534769 Recv: 112149.020737523 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No HASH: 2f188c6767b30436ddf1bb7dddb39792
[#CLIENT#] R[522]: Sent: 112139.431627060 Recv: 112149.020755064 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 69   ServerImgID: 69   Rejected: No
[#CLIENT#] R[523]: Sent: 112139.617432144 Recv: 112149.020758398 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 30   ServerImgID: 30   Rejected: No
[#CLIENT#] R[524]: Sent: 112139.772972185 Recv: 112149.081622189 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 51   ServerImgID: 51   Rejected: No HASH: be2f2892be0a6d85742dab3365fb5d6a
[#CLIENT#] R[525]: Sent: 112139.777892935 Recv: 112149.081634648 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 21   ServerImgID: 21   Rejected: No
[#CLIENT#] R[526]: Sent: 112139.788346352 Recv: 112149.081640981 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No
[#CLIENT#] R[527]: Sent: 112140.076409852 Recv: 112140.094220727 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 72   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[528]: Sent: 112140.179583561 Recv: 112149.108601398 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[529]: Sent: 112140.245738602 Recv: 112149.358226731 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 51   ServerImgID: 51   Rejected: No
[#CLIENT#] R[530]: Sent: 112140.269673519 Recv: 112149.377035148 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 47   ServerImgID: 47   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[531]: Sent: 112140.308558727 Recv: 112149.450752898 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 66   ServerImgID: 66   Rejected: No
[#CLIENT#] R[532]: Sent: 112140.576475727 Recv: 112149.914033607 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 29   ServerImgID: 29   Rejected: No
[#CLIENT#] R[533]: Sent: 112140.650451477 Recv: 112150.003281065 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 53   ServerImgID: 53   Rejected: No
[#CLIENT#] R[534]: Sent: 112140.690103019 Recv: 112150.050550357 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[535]: Sent: 112141.033988894 Recv: 112150.304152940 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 51   ServerImgID: 51   Rejected: No
[#CLIENT#] R[536]: Sent: 112141.082183978 Recv: 112150.387463148 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 72   ServerImgID: 72   Rejected: No
[#CLIENT#] R[537]: Sent: 112141.268397186 Recv: 112150.406203982 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No HASH: 0d3d7d856df5680b1b6a63fd5b3314b5
[#CLIENT#] R[538]: Sent: 112141.383809436 Recv: 112150.461310940 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 51   ServerImgID: 51   Rejected: No HASH: 8e0e76c9075fd45334543ee2a3edaf7f
[#CLIENT#] R[539]: Sent: 112141.548052353 Recv: 112150.876815982 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 58   ServerImgID: 58   Rejected: No
[#CLIENT#] R[540]: Sent: 112141.720227311 Recv: 112151.151033399 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 43   ServerImgID: 43   Rejected: No
[#CLIENT#] R[541]: Sent: 112141.824231103 Recv: 112141.928136811 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 73   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[542]: Sent: 112141.940878186 Recv: 112151.242489024 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[543]: Sent: 112141.958413520 Recv: 112141.976077395 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 74   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[544]: Sent: 112142.031905603 Recv: 112151.283272066 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 66   ServerImgID: 66   Rejected: No
[#CLIENT#] R[545]: Sent: 112142.230719062 Recv: 112151.753856774 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 40   ServerImgID: 40   Rejected: No
[#CLIENT#] R[546]: Sent: 112142.539236187 Recv: 112152.216085441 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No
[#CLIENT#] R[547]: Sent: 112142.751862312 Recv: 112152.466654524 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 43   ServerImgID: 43   Rejected: No
[#CLIENT#] R[548]: Sent: 112142.783093478 Recv: 112152.729536775 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 55   ServerImgID: 55   Rejected: No
[#CLIENT#] R[549]: Sent: 112142.837212978 Recv: 112152.814210441 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[550]: Sent: 112142.941760312 Recv: 112152.833440941 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No HASH: 2534f3b4744ebd76878f4b516855f50e
[#CLIENT#] R[551]: Sent: 112143.189845645 Recv: 112143.241731020 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 75   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[552]: Sent: 112143.493694437 Recv: 112152.863706691 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 73   ServerImgID: 73   Rejected: No
[#CLIENT#] R[553]: Sent: 112143.666888854 Recv: 112152.870535275 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 72   ServerImgID: 72   Rejected: No
[#CLIENT#] R[554]: Sent: 112143.730540937 Recv: 112152.961012108 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 47   ServerImgID: 47   Rejected: No
[#CLIENT#] R[555]: Sent: 112143.835732479 Recv: 112153.426782692 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 63   ServerImgID: 63   Rejected: No
[#CLIENT#] R[556]: Sent: 112143.888583521 Recv: 112143.994584604 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 76   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[557]: Sent: 112144.198245437 Recv: 112153.529822608 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No HASH: bac05c6033777c730e76ff3b22f12369
[#CLIENT#] R[558]: Sent: 112144.437074771 Recv: 112153.894937650 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[559]: Sent: 112144.455152521 Recv: 112153.951902567 Opcode: IMG_BLUR        OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No
[#CLIENT#] R[560]: Sent: 112144.465887729 Recv: 112154.201708817 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 43   ServerImgID: 43   Rejected: No
[#CLIENT#] R[561]: Sent: 112144.839078729 Recv: 112154.365896109 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 34   ServerImgID: 34   Rejected: No
[#CLIENT#] R[562]: Sent: 112145.209578355 Recv: 112154.529678775 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 34   ServerImgID: 34   Rejected: No
[#CLIENT#] R[563]: Sent: 112145.227784813 Recv: 112154.780489901 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[564]: Sent: 112145.229221021 Recv: 112155.084855109 Opcode: IMG_BLUR        OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No
[#CLIENT#] R[565]: Sent: 112145.416457230 Recv: 112155.122042567 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 44   ServerImgID: 44   Rejected: No
[#CLIENT#] R[566]: Sent: 112145.516076896 Recv: 112145.533704896 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 77   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[567]: Sent: 112145.671765522 Recv: 112155.255113734 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 57   ServerImgID: 57   Rejected: No
[#CLIENT#] R[568]: Sent: 112145.676429105 Recv: 112155.358298067 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No HASH: bb2bb45c3407997b8d9e65123dc1b341
[#CLIENT#] R[569]: Sent: 112145.699213230 Recv: 112155.559103151 Opcode: IMG_BLUR        OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[570]: Sent: 112145.702342563 Recv: 112155.578076943 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No HASH: 09455cf5848b5aa244104a6b118f9bfb
[#CLIENT#] R[571]: Sent: 112145.745036647 Recv: 112155.722480651 Opcode: IMG_BLUR        OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[572]: Sent: 112145.773047938 Recv: 112155.886534401 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 60   ServerImgID: 60   Rejected: No
[#CLIENT#] R[573]: Sent: 112145.956302772 Recv: 112155.907058484 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 43   ServerImgID: 43   Rejected: No
[#CLIENT#] R[574]: Sent: 112146.991429397 Recv: 112155.994649609 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[575]: Sent: 112146.995382689 Recv: 112147.029257189 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 78   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[576]: Sent: 112147.296055647 Recv: 112156.002932109 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[577]: Sent: 112147.558837772 Recv: 112147.576693564 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 79   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[578]: Sent: 112147.817173981 Recv: 112147.875781356 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 80   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[579]: Sent: 112147.891377731 Recv: 112156.021378359 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 71   ServerImgID: 71   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[580]: Sent: 112147.896458022 Recv: 112156.021385901 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 52   ServerImgID: 52   Rejected: No
[#CLIENT#] R[581]: Sent: 112147.928179564 Recv: 112156.025939151 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[582]: Sent: 112148.058697981 Recv: 112156.043935776 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 26   ServerImgID: 26   Rejected: No HASH: 55348f8ec458faee8aef206c3daa6f14
[#CLIENT#] R[583]: Sent: 112148.100314314 Recv: 112156.115108443 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[584]: Sent: 112148.363012272 Recv: 112156.133202818 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No HASH: b52bf2575572cfd08cd9725b1ec1a230
[#CLIENT#] R[585]: Sent: 112148.691855731 Recv: 112156.604773360 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[586]: Sent: 112148.702027564 Recv: 112156.649822235 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No
[#CLIENT#] R[587]: Sent: 112148.835038148 Recv: 112156.734537610 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 64   ServerImgID: 64   Rejected: No
[#CLIENT#] R[588]: Sent: 112149.966377232 Recv: 112156.993889318 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 55   ServerImgID: 55   Rejected: No
[#CLIENT#] R[589]: Sent: 112150.461331190 Recv: 112157.249504068 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 54   ServerImgID: 54   Rejected: No
[#CLIENT#] R[590]: Sent: 112150.574660440 Recv: 112157.338647485 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 66   ServerImgID: 66   Rejected: No
[#CLIENT#] R[591]: Sent: 112150.800145274 Recv: 112157.352226152 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[592]: Sent: 112150.885330440 Recv: 112157.370274027 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 79   ServerImgID: 79   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[593]: Sent: 112151.001647774 Recv: 112151.117486774 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 81   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[594]: Sent: 112151.169184649 Recv: 112157.440198985 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No
[#CLIENT#] R[595]: Sent: 112151.302344316 Recv: 112157.688581235 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 51   ServerImgID: 51   Rejected: No
[#CLIENT#] R[596]: Sent: 112151.377907816 Recv: 112157.772431152 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 77   ServerImgID: 77   Rejected: No
[#CLIENT#] R[597]: Sent: 112151.431889774 Recv: 112157.861853860 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 61   ServerImgID: 61   Rejected: No
[#CLIENT#] R[598]: Sent: 112151.447562066 Recv: 112151.465506191 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 82   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[599]: Sent: 112151.607533316 Recv: 112157.919413402 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 75   ServerImgID: 75   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[600]: Sent: 112151.669589941 Recv: 112158.165226735 Opcode: IMG_BLUR        OW: 1 ClientImgID: 76   ServerImgID: 76   Rejected: No
[#CLIENT#] R[601]: Sent: 112151.703281357 Recv: 112158.336608569 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No
[#CLIENT#] R[602]: Sent: 112151.789406024 Recv: 112158.355484236 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 74   ServerImgID: 74   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[603]: Sent: 112151.876069149 Recv: 112158.536119152 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 28   ServerImgID: 28   Rejected: No
[#CLIENT#] R[604]: Sent: 112151.890419524 Recv: 112158.536160736 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 51   ServerImgID: 51   Rejected: No
[#CLIENT#] R[605]: Sent: 112151.966756358 Recv: 112158.536167236 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[606]: Sent: 112152.137613066 Recv: 112158.577091277 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 63   ServerImgID: 63   Rejected: No
[#CLIENT#] R[607]: Sent: 112152.389102483 Recv: 112159.066569361 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[608]: Sent: 112152.532893608 Recv: 112152.552243399 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 83   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[609]: Sent: 112152.582074441 Recv: 112159.085268528 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No HASH: b52bf2575572cfd08cd9725b1ec1a230
[#CLIENT#] R[610]: Sent: 112152.662097275 Recv: 112159.277190444 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 34   ServerImgID: 34   Rejected: No
[#CLIENT#] R[611]: Sent: 112152.778817358 Recv: 112159.295803653 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 70   ServerImgID: 70   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[612]: Sent: 112153.066524983 Recv: 112159.330578528 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No HASH: cc8b12cd931a024df74ed947b274d736
[#CLIENT#] R[613]: Sent: 112153.071120275 Recv: 112153.175461108 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 84   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[614]: Sent: 112153.215584941 Recv: 112159.330598194 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 66   ServerImgID: 66   Rejected: No
[#CLIENT#] R[615]: Sent: 112153.346422692 Recv: 112159.502476111 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[616]: Sent: 112153.369315317 Recv: 112159.753048861 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 75   ServerImgID: 75   Rejected: No
[#CLIENT#] R[617]: Sent: 112153.558875650 Recv: 112160.219202028 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 45   ServerImgID: 45   Rejected: No
[#CLIENT#] R[618]: Sent: 112153.610255692 Recv: 112153.662835192 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 85   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[619]: Sent: 112153.752028358 Recv: 112160.258227278 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[620]: Sent: 112153.804185858 Recv: 112160.524013903 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[621]: Sent: 112153.879034692 Recv: 112160.545969778 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 43   ServerImgID: 43   Rejected: No
[#CLIENT#] R[622]: Sent: 112154.067218775 Recv: 112160.851204612 Opcode: IMG_BLUR        OW: 1 ClientImgID: 81   ServerImgID: 81   Rejected: No
[#CLIENT#] R[623]: Sent: 112154.350888567 Recv: 112161.335111154 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 84   ServerImgID: 84   Rejected: No
[#CLIENT#] R[624]: Sent: 112154.419370567 Recv: 112161.405580154 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 68   ServerImgID: 68   Rejected: No
[#CLIENT#] R[625]: Sent: 112154.664080317 Recv: 112161.626103570 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No
[#CLIENT#] R[626]: Sent: 112154.931398151 Recv: 112161.626146029 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[627]: Sent: 112154.939605776 Recv: 112161.770809321 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 52   ServerImgID: 52   Rejected: No
[#CLIENT#] R[628]: Sent: 112155.087170026 Recv: 112155.105109567 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 86   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[629]: Sent: 112155.121988734 Recv: 112161.937687987 Opcode: IMG_BLUR        OW: 1 ClientImgID: 55   ServerImgID: 55   Rejected: No
[#CLIENT#] R[630]: Sent: 112155.578091901 Recv: 112161.956891029 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 68   ServerImgID: 68   Rejected: No HASH: 78a7633528e7dc2fc020b73ae9ed6596
[#CLIENT#] R[631]: Sent: 112155.709909776 Recv: 112162.028898529 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No
[#CLIENT#] R[632]: Sent: 112155.821487818 Recv: 112162.083483654 Opcode: IMG_BLUR        OW: 1 ClientImgID: 64   ServerImgID: 64   Rejected: No
[#CLIENT#] R[633]: Sent: 112155.870100568 Recv: 112162.175163362 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 83   ServerImgID: 83   Rejected: No
[#CLIENT#] R[634]: Sent: 112155.929754859 Recv: 112162.283745862 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No HASH: 416c13671c31bb9bb45ea4b2c6e57530
[#CLIENT#] R[635]: Sent: 112156.558666485 Recv: 112162.674093279 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No
[#CLIENT#] R[636]: Sent: 112156.642233235 Recv: 112162.687562196 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No
[#CLIENT#] R[637]: Sent: 112156.996516235 Recv: 112162.732187738 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[638]: Sent: 112157.010790110 Recv: 112162.895814904 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 49   ServerImgID: 49   Rejected: No
[#CLIENT#] R[639]: Sent: 112157.178081943 Recv: 112162.993765154 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[640]: Sent: 112157.209436277 Recv: 112163.095689571 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No HASH: 4c67d9a86c38a6a55fed1e0ec9f7d27e
[#CLIENT#] R[641]: Sent: 112157.214809193 Recv: 112163.095709363 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 70   ServerImgID: 70   Rejected: No
[#CLIENT#] R[642]: Sent: 112157.404510693 Recv: 112163.575546071 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 21   ServerImgID: 21   Rejected: No
[#CLIENT#] R[643]: Sent: 112157.498096777 Recv: 112164.066835072 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 84   ServerImgID: 84   Rejected: No
[#CLIENT#] R[644]: Sent: 112157.544134777 Recv: 112164.316743863 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[645]: Sent: 112157.606474527 Recv: 112164.340315738 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 23   ServerImgID: 23   Rejected: No
[#CLIENT#] R[646]: Sent: 112157.703754902 Recv: 112157.738506485 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 87   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[647]: Sent: 112157.743380319 Recv: 112164.810025447 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 40   ServerImgID: 40   Rejected: No
[#CLIENT#] R[648]: Sent: 112157.832775444 Recv: 112157.850679069 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 88   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[649]: Sent: 112157.956373069 Recv: 112157.974359985 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 89   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[650]: Sent: 112158.147471610 Recv: 112164.975484197 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[651]: Sent: 112158.218432361 Recv: 112165.439838072 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 76   ServerImgID: 76   Rejected: No
[#CLIENT#] R[652]: Sent: 112158.245126319 Recv: 112165.523587614 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 74   ServerImgID: 74   Rejected: No
[#CLIENT#] R[653]: Sent: 112158.434151027 Recv: 112165.821886364 Opcode: IMG_BLUR        OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[654]: Sent: 112158.469018694 Recv: 112165.839730989 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 26   ServerImgID: 26   Rejected: No HASH: 55348f8ec458faee8aef206c3daa6f14
[#CLIENT#] R[655]: Sent: 112158.475730277 Recv: 112165.985709948 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No
[#CLIENT#] R[656]: Sent: 112158.483456569 Recv: 112158.536112069 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 90   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[657]: Sent: 112158.565317986 Recv: 112166.077242073 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 47   ServerImgID: 47   Rejected: No
[#CLIENT#] R[658]: Sent: 112158.679365569 Recv: 112158.696971444 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 91   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[659]: Sent: 112158.710413069 Recv: 112166.239163156 Opcode: IMG_BLUR        OW: 1 ClientImgID: 43   ServerImgID: 43   Rejected: No
[#CLIENT#] R[660]: Sent: 112158.847517777 Recv: 112166.329774114 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No
[#CLIENT#] R[661]: Sent: 112158.922815569 Recv: 112166.337606156 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No
[#CLIENT#] R[662]: Sent: 112158.945977111 Recv: 112166.355925364 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 79   ServerImgID: 79   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[663]: Sent: 112159.005844944 Recv: 112166.424814489 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[664]: Sent: 112159.109589111 Recv: 112159.143786694 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 92   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[665]: Sent: 112159.171375903 Recv: 112159.277185694 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 93   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[666]: Sent: 112159.330609611 Recv: 112166.508484198 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[667]: Sent: 112159.352065319 Recv: 112166.615232990 Opcode: IMG_BLUR        OW: 1 ClientImgID: 92   ServerImgID: 92   Rejected: No
[#CLIENT#] R[668]: Sent: 112159.361084444 Recv: 112166.629218406 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 92   ServerImgID: 92   Rejected: No
[#CLIENT#] R[669]: Sent: 112159.365922111 Recv: 112166.882518948 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[670]: Sent: 112159.584868111 Recv: 112167.134937281 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 42   ServerImgID: 42   Rejected: No
[#CLIENT#] R[671]: Sent: 112159.794591736 Recv: 112167.225652448 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[672]: Sent: 112159.801483153 Recv: 112167.533675698 Opcode: IMG_BLUR        OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[673]: Sent: 112159.837803486 Recv: 112167.569061282 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 78   ServerImgID: 78   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[674]: Sent: 112159.860102820 Recv: 112167.587519073 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 50   ServerImgID: 50   Rejected: No HASH: 718d34266062049362b6c40493e775e1
[#CLIENT#] R[675]: Sent: 112159.872908528 Recv: 112168.028463115 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[676]: Sent: 112159.948239861 Recv: 112160.053954570 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 94   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[677]: Sent: 112160.058570403 Recv: 112168.119692615 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No
[#CLIENT#] R[678]: Sent: 112160.188205278 Recv: 112168.175689532 Opcode: IMG_BLUR        OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[679]: Sent: 112160.204821403 Recv: 112168.267193032 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 70   ServerImgID: 70   Rejected: No
[#CLIENT#] R[680]: Sent: 112160.597674945 Recv: 112168.324215657 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 51   ServerImgID: 51   Rejected: No HASH: 546b5df34b55d9683741c2a2fb3984e8
[#CLIENT#] R[681]: Sent: 112160.601007778 Recv: 112168.324237699 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 75   ServerImgID: 75   Rejected: No
[#CLIENT#] R[682]: Sent: 112160.770333695 Recv: 112160.788735487 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 95   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[683]: Sent: 112160.872169487 Recv: 112168.379849115 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 72   ServerImgID: 72   Rejected: No
[#CLIENT#] R[684]: Sent: 112160.886211320 Recv: 112168.436139407 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 16   ServerImgID: 16   Rejected: No HASH: 4b2c35b86d903c301597d0ec3e9cb745
[#CLIENT#] R[685]: Sent: 112161.048940112 Recv: 112168.680733074 Opcode: IMG_BLUR        OW: 1 ClientImgID: 94   ServerImgID: 94   Rejected: No
[#CLIENT#] R[686]: Sent: 112161.154049695 Recv: 112168.769063491 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 77   ServerImgID: 77   Rejected: No
[#CLIENT#] R[687]: Sent: 112161.290457070 Recv: 112161.324518654 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 96   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[688]: Sent: 112161.365936279 Recv: 112169.234836991 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[689]: Sent: 112161.378169195 Recv: 112169.276048449 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[690]: Sent: 112161.400174904 Recv: 112169.343103032 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 89   ServerImgID: 89   Rejected: No
[#CLIENT#] R[691]: Sent: 112161.440694529 Recv: 112169.398244991 Opcode: IMG_BLUR        OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[692]: Sent: 112161.445897487 Recv: 112169.885357158 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 84   ServerImgID: 84   Rejected: No
[#CLIENT#] R[693]: Sent: 112161.526949487 Recv: 112169.993921491 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 84   ServerImgID: 84   Rejected: No HASH: 724f8c7da6816ec84a846429e542b3af
[#CLIENT#] R[694]: Sent: 112161.562392987 Recv: 112161.625221945 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 97   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[695]: Sent: 112161.882682904 Recv: 112170.056598408 Opcode: IMG_BLUR        OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[696]: Sent: 112161.994915779 Recv: 112170.518261658 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 76   ServerImgID: 76   Rejected: No
[#CLIENT#] R[697]: Sent: 112162.147989904 Recv: 112170.572689033 Opcode: IMG_BLUR        OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[698]: Sent: 112162.283763362 Recv: 112162.390495154 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 98   Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[699]: Sent: 112162.526356029 Recv: 112162.578401863 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 99   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[700]: Sent: 112162.708096196 Recv: 112170.657454450 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 39   ServerImgID: 39   Rejected: No
[#CLIENT#] R[701]: Sent: 112162.741402738 Recv: 112170.907275367 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 75   ServerImgID: 75   Rejected: No
[#CLIENT#] R[702]: Sent: 112162.775548154 Recv: 112170.914673408 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 26   ServerImgID: 26   Rejected: No
[#CLIENT#] R[703]: Sent: 112162.942086363 Recv: 112162.993755529 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 100  Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[704]: Sent: 112163.095718780 Recv: 112171.177232575 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 75   ServerImgID: 75   Rejected: No
[#CLIENT#] R[705]: Sent: 112163.167710571 Recv: 112171.219212117 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 40   ServerImgID: 40   Rejected: No
[#CLIENT#] R[706]: Sent: 112163.168987113 Recv: 112171.520181242 Opcode: IMG_BLUR        OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No
[#CLIENT#] R[707]: Sent: 112163.188763321 Recv: 112171.771511409 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 75   ServerImgID: 75   Rejected: No
[#CLIENT#] R[708]: Sent: 112163.195218071 Recv: 112163.300736530 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 101  Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[709]: Sent: 112163.349735571 Recv: 112171.790986242 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 35   ServerImgID: 35   Rejected: No HASH: e91603ff2577620f87e773d162cbb1b8
[#CLIENT#] R[710]: Sent: 112163.386550280 Recv: 112163.420340780 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 102  Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[711]: Sent: 112163.582628071 Recv: 112172.029646284 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 54   ServerImgID: 54   Rejected: No
[#CLIENT#] R[712]: Sent: 112163.818450155 Recv: 112163.836399613 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 103  Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[713]: Sent: 112163.892895905 Recv: 112172.117315492 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[714]: Sent: 112164.185912030 Recv: 112164.220391197 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 104  Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[715]: Sent: 112164.307332572 Recv: 112172.204399576 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[716]: Sent: 112164.322210697 Recv: 112172.372496826 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 104  ServerImgID: 104  Rejected: No
[#CLIENT#] R[717]: Sent: 112164.353391238 Recv: 112172.693050867 Opcode: IMG_BLUR        OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[718]: Sent: 112164.478726989 Recv: 112173.195192076 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No
[#CLIENT#] R[719]: Sent: 112164.648456447 Recv: 112164.700320614 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 105  Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[720]: Sent: 112164.817297239 Recv: 112173.457360868 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 25   ServerImgID: 25   Rejected: No
[#CLIENT#] R[721]: Sent: 112164.892867864 Recv: 112173.563394659 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 73   ServerImgID: 73   Rejected: No HASH: a475f010c4c086a083fedd66f3725234
[#CLIENT#] R[722]: Sent: 112165.003987697 Recv: 112165.056525822 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 106  Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[723]: Sent: 112165.074171530 Recv: 112173.563407993 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 74   ServerImgID: 74   Rejected: No
[#CLIENT#] R[724]: Sent: 112165.155805947 Recv: 112173.600436493 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 60   ServerImgID: 60   Rejected: No HASH: b1b45b2076c3827d711962b82aa208f4
[#CLIENT#] R[725]: Sent: 112165.172848864 Recv: 112173.600468868 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No
[#CLIENT#] R[726]: Sent: 112165.386291447 Recv: 112173.641447618 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 91   ServerImgID: 91   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[727]: Sent: 112165.438753531 Recv: 112173.748416410 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 69   ServerImgID: 69   Rejected: No
[#CLIENT#] R[728]: Sent: 112165.511783447 Recv: 112173.999144118 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 80   ServerImgID: 80   Rejected: No
[#CLIENT#] R[729]: Sent: 112165.618748906 Recv: 112174.163465160 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 36   ServerImgID: 36   Rejected: No
[#CLIENT#] R[730]: Sent: 112165.702485072 Recv: 112174.250212660 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 47   ServerImgID: 47   Rejected: No
[#CLIENT#] R[731]: Sent: 112166.072307906 Recv: 112174.500933535 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 25   ServerImgID: 25   Rejected: No
[#CLIENT#] R[732]: Sent: 112166.090376489 Recv: 112174.584663660 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 72   ServerImgID: 72   Rejected: No
[#CLIENT#] R[733]: Sent: 112166.145643281 Recv: 112174.676738910 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 103  ServerImgID: 103  Rejected: No
[#CLIENT#] R[734]: Sent: 112166.228808323 Recv: 112174.942748243 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[735]: Sent: 112166.362561073 Recv: 112166.380077614 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 107  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[736]: Sent: 112166.441091948 Recv: 112174.983060035 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[737]: Sent: 112166.573771489 Recv: 112175.049821827 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[738]: Sent: 112166.712554156 Recv: 112175.084796077 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 34   ServerImgID: 34   Rejected: No HASH: 6af9501a868a53fa1aad440e6858e798
[#CLIENT#] R[739]: Sent: 112166.795971656 Recv: 112175.120924952 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 92   ServerImgID: 92   Rejected: No HASH: 2ed48485c391a80bfb05fe3b8525c2eb
[#CLIENT#] R[740]: Sent: 112166.879851448 Recv: 112175.613527327 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 27   ServerImgID: 27   Rejected: No
[#CLIENT#] R[741]: Sent: 112166.886494490 Recv: 112166.903920490 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 108  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[742]: Sent: 112167.098549365 Recv: 112175.613531410 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No
[#CLIENT#] R[743]: Sent: 112167.290325698 Recv: 112175.687447036 Opcode: IMG_BLUR        OW: 1 ClientImgID: 25   ServerImgID: 25   Rejected: No
[#CLIENT#] R[744]: Sent: 112167.356267240 Recv: 112175.771402702 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 89   ServerImgID: 89   Rejected: No
[#CLIENT#] R[745]: Sent: 112167.474124365 Recv: 112175.813408202 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No
[#CLIENT#] R[746]: Sent: 112167.480680657 Recv: 112175.853106119 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 84   ServerImgID: 84   Rejected: No
[#CLIENT#] R[747]: Sent: 112167.612718532 Recv: 112175.959860536 Opcode: IMG_BLUR        OW: 1 ClientImgID: 102  ServerImgID: 102  Rejected: No
[#CLIENT#] R[748]: Sent: 112167.961185407 Recv: 112176.013989202 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 93   ServerImgID: 93   Rejected: No
[#CLIENT#] R[749]: Sent: 112168.027948574 Recv: 112176.119453661 Opcode: IMG_BLUR        OW: 1 ClientImgID: 69   ServerImgID: 69   Rejected: No
[#CLIENT#] R[750]: Sent: 112168.038707574 Recv: 112176.175746036 Opcode: IMG_BLUR        OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No
[#CLIENT#] R[751]: Sent: 112168.108738865 Recv: 112176.259902869 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[752]: Sent: 112168.133913074 Recv: 112176.343707244 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 107  ServerImgID: 107  Rejected: No
[#CLIENT#] R[753]: Sent: 112168.436157032 Recv: 112176.427145911 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 82   ServerImgID: 82   Rejected: No
[#CLIENT#] R[754]: Sent: 112168.589507199 Recv: 112176.467944119 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 93   ServerImgID: 93   Rejected: No
[#CLIENT#] R[755]: Sent: 112168.632061532 Recv: 112176.553205328 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 72   ServerImgID: 72   Rejected: No
[#CLIENT#] R[756]: Sent: 112168.779421699 Recv: 112176.644984161 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No
[#CLIENT#] R[757]: Sent: 112169.060517032 Recv: 112176.681499786 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 69   ServerImgID: 69   Rejected: No HASH: 08d5145482ee2b793c663934d28ba736
[#CLIENT#] R[758]: Sent: 112169.090844699 Recv: 112176.730803453 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 89   ServerImgID: 89   Rejected: No
[#CLIENT#] R[759]: Sent: 112169.119946824 Recv: 112176.786352203 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 75   ServerImgID: 75   Rejected: No HASH: adc23dc6dc33b962db7266b6c30d2722
[#CLIENT#] R[760]: Sent: 112169.204311199 Recv: 112176.786410578 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No
[#CLIENT#] R[761]: Sent: 112169.355976741 Recv: 112169.373545949 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 109  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[762]: Sent: 112169.569972699 Recv: 112176.893410161 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 29   ServerImgID: 29   Rejected: No HASH: 9d278f693acd1c3d933d5bcbd5e97aef
[#CLIENT#] R[763]: Sent: 112169.993942033 Recv: 112177.251209536 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 40   ServerImgID: 40   Rejected: No
[#CLIENT#] R[764]: Sent: 112170.071998200 Recv: 112177.343911828 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[765]: Sent: 112170.086228241 Recv: 112177.596090203 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 23   ServerImgID: 23   Rejected: No
[#CLIENT#] R[766]: Sent: 112170.151844575 Recv: 112178.062625327 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 56   ServerImgID: 56   Rejected: No
[#CLIENT#] R[767]: Sent: 112170.156471658 Recv: 112178.368531161 Opcode: IMG_BLUR        OW: 1 ClientImgID: 94   ServerImgID: 94   Rejected: No
[#CLIENT#] R[768]: Sent: 112170.238223533 Recv: 112178.473235119 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 22   ServerImgID: 22   Rejected: No HASH: 8ad3ff104f1f02bc48625a0d3278d7ca
[#CLIENT#] R[769]: Sent: 112170.385853950 Recv: 112178.473242744 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 78   ServerImgID: 78   Rejected: No
[#CLIENT#] R[770]: Sent: 112170.414565158 Recv: 112178.473291494 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[771]: Sent: 112170.496535158 Recv: 112178.525613161 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 107  ServerImgID: 107  Rejected: No
[#CLIENT#] R[772]: Sent: 112170.641420366 Recv: 112178.617664911 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[773]: Sent: 112170.770172992 Recv: 112178.672078369 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 67   ServerImgID: 67   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[774]: Sent: 112170.804268617 Recv: 112178.690628828 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 59   ServerImgID: 59   Rejected: No HASH: ca8dabad272577686d07ecf7bb519b7f
[#CLIENT#] R[775]: Sent: 112171.087851658 Recv: 112178.706107369 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[776]: Sent: 112171.134814700 Recv: 112178.724246786 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 74   ServerImgID: 74   Rejected: No HASH: 3b3e20aa776ada5ed79da1b1242d54fd
[#CLIENT#] R[777]: Sent: 112171.240087492 Recv: 112178.779691078 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 16   ServerImgID: 16   Rejected: No HASH: 4b2c35b86d903c301597d0ec3e9cb745
[#CLIENT#] R[778]: Sent: 112171.310166783 Recv: 112178.797546453 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[779]: Sent: 112171.541402075 Recv: 112179.260554745 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 93   ServerImgID: 93   Rejected: No
[#CLIENT#] R[780]: Sent: 112171.581626992 Recv: 112179.725644536 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[781]: Sent: 112171.806070200 Recv: 112180.190368787 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[782]: Sent: 112171.816037325 Recv: 112180.279507078 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[783]: Sent: 112171.832742284 Recv: 112180.298406328 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 50   ServerImgID: 50   Rejected: No HASH: 718d34266062049362b6c40493e775e1
[#CLIENT#] R[784]: Sent: 112171.832820659 Recv: 112171.851036534 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 110  Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[785]: Sent: 112171.905397950 Recv: 112180.581478537 Opcode: IMG_BLUR        OW: 1 ClientImgID: 45   ServerImgID: 45   Rejected: No
[#CLIENT#] R[786]: Sent: 112172.046443117 Recv: 112180.636979079 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 97   ServerImgID: 97   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[787]: Sent: 112172.198216367 Recv: 112181.098641037 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No
[#CLIENT#] R[788]: Sent: 112172.255172867 Recv: 112181.582233204 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 101  ServerImgID: 101  Rejected: No
[#CLIENT#] R[789]: Sent: 112172.627958201 Recv: 112181.652911412 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 53   ServerImgID: 53   Rejected: No
[#CLIENT#] R[790]: Sent: 112172.735765159 Recv: 112181.706766996 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 43   ServerImgID: 43   Rejected: No HASH: 1832c766ca31fff55366ca0b5ebfe998
[#CLIENT#] R[791]: Sent: 112172.741372534 Recv: 112181.706783996 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 23   ServerImgID: 23   Rejected: No
[#CLIENT#] R[792]: Sent: 112173.021336076 Recv: 112181.988534204 Opcode: IMG_BLUR        OW: 1 ClientImgID: 27   ServerImgID: 27   Rejected: No
[#CLIENT#] R[793]: Sent: 112173.040769743 Recv: 112182.023694829 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No HASH: e0d35013596353b35647792dfb1d70fb
[#CLIENT#] R[794]: Sent: 112173.173678284 Recv: 112182.452082871 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 81   ServerImgID: 81   Rejected: No
[#CLIENT#] R[795]: Sent: 112173.191146993 Recv: 112182.506454121 Opcode: IMG_BLUR        OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[796]: Sent: 112173.277727326 Recv: 112182.591045871 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 39   ServerImgID: 39   Rejected: No
[#CLIENT#] R[797]: Sent: 112173.342520284 Recv: 112182.645173288 Opcode: IMG_BLUR        OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[798]: Sent: 112173.600480451 Recv: 112173.641474201 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 111  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[799]: Sent: 112173.672095868 Recv: 112182.729396246 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 35   ServerImgID: 35   Rejected: No
[#CLIENT#] R[800]: Sent: 112173.810027118 Recv: 112183.193711121 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[801]: Sent: 112173.832538993 Recv: 112183.657535247 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 98   ServerImgID: 98   Rejected: No
[#CLIENT#] R[802]: Sent: 112173.870328701 Recv: 112183.908359205 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 16   ServerImgID: 16   Rejected: No
[#CLIENT#] R[803]: Sent: 112174.061906826 Recv: 112184.001168830 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[804]: Sent: 112174.139730368 Recv: 112184.048521164 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 81   ServerImgID: 81   Rejected: No
[#CLIENT#] R[805]: Sent: 112174.249407535 Recv: 112184.133505580 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 74   ServerImgID: 74   Rejected: No
[#CLIENT#] R[806]: Sent: 112174.268126035 Recv: 112184.297987622 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[807]: Sent: 112174.324051952 Recv: 112184.316160455 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 72   ServerImgID: 72   Rejected: No HASH: 60ea7ced6c2564b47808ed9c0f294ac5
[#CLIENT#] R[808]: Sent: 112174.333508577 Recv: 112184.372481497 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 23   ServerImgID: 23   Rejected: No HASH: 5e5931dcd1b1bc70190585de0496669f
[#CLIENT#] R[809]: Sent: 112174.441204577 Recv: 112184.386046497 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 68   ServerImgID: 68   Rejected: No
[#CLIENT#] R[810]: Sent: 112174.445026660 Recv: 112184.558892539 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[811]: Sent: 112174.525539077 Recv: 112184.598280789 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 63   ServerImgID: 63   Rejected: No
[#CLIENT#] R[812]: Sent: 112174.536304702 Recv: 112185.084987247 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 93   ServerImgID: 93   Rejected: No
[#CLIENT#] R[813]: Sent: 112174.686578660 Recv: 112185.169865789 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 33   ServerImgID: 33   Rejected: No
[#CLIENT#] R[814]: Sent: 112174.818838535 Recv: 112185.223166164 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 42   ServerImgID: 42   Rejected: No HASH: be9bcb384b494d77de72bf72c984488a
[#CLIENT#] R[815]: Sent: 112175.169138619 Recv: 112175.278615577 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 112  Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[816]: Sent: 112175.515306327 Recv: 112175.613550744 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 113  Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[817]: Sent: 112175.648915160 Recv: 112185.635435789 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 81   ServerImgID: 81   Rejected: No
[#CLIENT#] R[818]: Sent: 112175.909142911 Recv: 112185.661019289 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 106  ServerImgID: 106  Rejected: No
[#CLIENT#] R[819]: Sent: 112175.934492327 Recv: 112185.679769539 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 79   ServerImgID: 79   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[820]: Sent: 112175.952786327 Recv: 112185.749199873 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No
[#CLIENT#] R[821]: Sent: 112176.006511411 Recv: 112186.214744165 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[822]: Sent: 112176.008843244 Recv: 112186.260382623 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[823]: Sent: 112176.270942786 Recv: 112186.302278040 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 22   ServerImgID: 22   Rejected: No
[#CLIENT#] R[824]: Sent: 112176.307469161 Recv: 112186.346619290 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 27   ServerImgID: 27   Rejected: No
[#CLIENT#] R[825]: Sent: 112176.530158203 Recv: 112186.836815207 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No
[#CLIENT#] R[826]: Sent: 112176.716901786 Recv: 112187.100435165 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 55   ServerImgID: 55   Rejected: No
[#CLIENT#] R[827]: Sent: 112176.893428578 Recv: 112187.408152790 Opcode: IMG_BLUR        OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[828]: Sent: 112176.900230911 Recv: 112187.657491207 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 97   ServerImgID: 97   Rejected: No
[#CLIENT#] R[829]: Sent: 112177.021999828 Recv: 112187.748881499 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No
[#CLIENT#] R[830]: Sent: 112177.027984661 Recv: 112188.234694832 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 76   ServerImgID: 76   Rejected: No
[#CLIENT#] R[831]: Sent: 112177.233567745 Recv: 112188.323167124 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[832]: Sent: 112177.276721786 Recv: 112188.365080582 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[833]: Sent: 112177.440021161 Recv: 112188.635062416 Opcode: IMG_BLUR        OW: 1 ClientImgID: 58   ServerImgID: 58   Rejected: No
[#CLIENT#] R[834]: Sent: 112177.449407661 Recv: 112177.466984995 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 114  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[835]: Sent: 112177.602898620 Recv: 112188.796768999 Opcode: IMG_BLUR        OW: 1 ClientImgID: 16   ServerImgID: 16   Rejected: No
[#CLIENT#] R[836]: Sent: 112177.659716036 Recv: 112188.883469957 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No
[#CLIENT#] R[837]: Sent: 112177.699690453 Recv: 112188.967741541 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 35   ServerImgID: 35   Rejected: No
[#CLIENT#] R[838]: Sent: 112177.895920827 Recv: 112189.140480041 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 49   ServerImgID: 49   Rejected: No
[#CLIENT#] R[839]: Sent: 112177.908051827 Recv: 112189.224764541 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 108  ServerImgID: 108  Rejected: No
[#CLIENT#] R[840]: Sent: 112178.046825619 Recv: 112189.527224249 Opcode: IMG_BLUR        OW: 1 ClientImgID: 93   ServerImgID: 93   Rejected: No
[#CLIENT#] R[841]: Sent: 112178.211286536 Recv: 112189.617435250 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[842]: Sent: 112178.473251328 Recv: 112189.780776916 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 36   ServerImgID: 36   Rejected: No
[#CLIENT#] R[843]: Sent: 112178.779709994 Recv: 112189.805309916 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[844]: Sent: 112179.001925578 Recv: 112190.269361041 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 84   ServerImgID: 84   Rejected: No
[#CLIENT#] R[845]: Sent: 112179.058188286 Recv: 112190.435312000 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 65   ServerImgID: 65   Rejected: No
[#CLIENT#] R[846]: Sent: 112179.132132870 Recv: 112190.600018667 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 36   ServerImgID: 36   Rejected: No
[#CLIENT#] R[847]: Sent: 112179.140019745 Recv: 112190.615532125 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 28   ServerImgID: 28   Rejected: No
[#CLIENT#] R[848]: Sent: 112179.189022370 Recv: 112190.718847125 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No HASH: 9cc30f3f41b6c1664957f515b67bb06b
[#CLIENT#] R[849]: Sent: 112179.237362911 Recv: 112190.718863208 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 50   ServerImgID: 50   Rejected: No
[#CLIENT#] R[850]: Sent: 112179.271192786 Recv: 112190.798138917 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 77   ServerImgID: 77   Rejected: No
[#CLIENT#] R[851]: Sent: 112179.302049078 Recv: 112190.882298208 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[852]: Sent: 112179.434061078 Recv: 112190.970713833 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 39   ServerImgID: 39   Rejected: No
[#CLIENT#] R[853]: Sent: 112179.558781370 Recv: 112191.074581834 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No HASH: 44c02a40a3054f600a746dd4283071ab
[#CLIENT#] R[854]: Sent: 112179.572892828 Recv: 112191.074613959 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 72   ServerImgID: 72   Rejected: No
[#CLIENT#] R[855]: Sent: 112179.607868870 Recv: 112191.237289459 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 28   ServerImgID: 28   Rejected: No
[#CLIENT#] R[856]: Sent: 112179.617924078 Recv: 112191.255628292 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 39   ServerImgID: 39   Rejected: No HASH: 7fba26df9b8d47e422afff7b6044e9c1
[#CLIENT#] R[857]: Sent: 112179.665423328 Recv: 112191.362055792 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 56   ServerImgID: 56   Rejected: No HASH: 09265369a030e219fcd2d80a99ded564
[#CLIENT#] R[858]: Sent: 112179.883307412 Recv: 112179.900948037 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 115  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[859]: Sent: 112180.017124620 Recv: 112191.726607626 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 63   ServerImgID: 63   Rejected: No
[#CLIENT#] R[860]: Sent: 112180.083095662 Recv: 112191.919343376 Opcode: IMG_BLUR        OW: 1 ClientImgID: 85   ServerImgID: 85   Rejected: No
[#CLIENT#] R[861]: Sent: 112180.123216078 Recv: 112192.053423084 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[862]: Sent: 112180.134013120 Recv: 112192.106592126 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 75   ServerImgID: 75   Rejected: No HASH: adc23dc6dc33b962db7266b6c30d2722
[#CLIENT#] R[863]: Sent: 112180.149993453 Recv: 112192.138106167 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 88   ServerImgID: 88   Rejected: No
[#CLIENT#] R[864]: Sent: 112180.181670162 Recv: 112192.301794834 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 60   ServerImgID: 60   Rejected: No
[#CLIENT#] R[865]: Sent: 112180.264235203 Recv: 112192.798043793 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[866]: Sent: 112180.408258995 Recv: 112192.881938876 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 108  ServerImgID: 108  Rejected: No
[#CLIENT#] R[867]: Sent: 112180.445127578 Recv: 112180.497961745 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 116  Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[868]: Sent: 112180.572388037 Recv: 112192.988588459 Opcode: IMG_BLUR        OW: 1 ClientImgID: 102  ServerImgID: 102  Rejected: No
[#CLIENT#] R[869]: Sent: 112180.636994079 Recv: 112193.450712335 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 45   ServerImgID: 45   Rejected: No
[#CLIENT#] R[870]: Sent: 112180.747678245 Recv: 112180.856434745 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 117  Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[871]: Sent: 112180.918042120 Recv: 112193.538099585 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[872]: Sent: 112180.978862870 Recv: 112194.001439960 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No
[#CLIENT#] R[873]: Sent: 112181.044906870 Recv: 112194.108621835 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 109  ServerImgID: 109  Rejected: No
[#CLIENT#] R[874]: Sent: 112181.112071745 Recv: 112181.146459037 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 118  Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[875]: Sent: 112181.191320412 Recv: 112194.108627543 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 49   ServerImgID: 49   Rejected: No
[#CLIENT#] R[876]: Sent: 112181.267200121 Recv: 112194.143052710 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 52   ServerImgID: 52   Rejected: No HASH: a8668745537ff91a7572d7046ad701bb
[#CLIENT#] R[877]: Sent: 112181.340619246 Recv: 112194.156556085 Opcode: IMG_BLUR        OW: 1 ClientImgID: 74   ServerImgID: 74   Rejected: No
[#CLIENT#] R[878]: Sent: 112181.392245746 Recv: 112194.196521127 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 27   ServerImgID: 27   Rejected: No
[#CLIENT#] R[879]: Sent: 112181.476109037 Recv: 112181.494302662 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 119  Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[880]: Sent: 112181.544732871 Recv: 112194.343189085 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 111  ServerImgID: 111  Rejected: No
[#CLIENT#] R[881]: Sent: 112181.564094037 Recv: 112181.582246037 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 120  Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[882]: Sent: 112181.600952412 Recv: 112194.343221210 Opcode: IMG_BLUR        OW: 1 ClientImgID: 74   ServerImgID: 74   Rejected: No
[#CLIENT#] R[883]: Sent: 112181.613120121 Recv: 112194.423487335 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 79   ServerImgID: 79   Rejected: No
[#CLIENT#] R[884]: Sent: 112181.739848246 Recv: 112194.891778252 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 94   ServerImgID: 94   Rejected: No
[#CLIENT#] R[885]: Sent: 112181.752114704 Recv: 112194.910688544 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 50   ServerImgID: 50   Rejected: No HASH: 9db28b1eaa63f07ad95591ec3ed72587
[#CLIENT#] R[886]: Sent: 112181.842922246 Recv: 112194.980781502 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No
[#CLIENT#] R[887]: Sent: 112181.873251496 Recv: 112181.925169246 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 121  Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[888]: Sent: 112182.991659955 Recv: 112195.066985460 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 50   ServerImgID: 50   Rejected: No
[#CLIENT#] R[889]: Sent: 112183.008754746 Recv: 112195.121661252 Opcode: IMG_BLUR        OW: 1 ClientImgID: 61   ServerImgID: 61   Rejected: No
[#CLIENT#] R[890]: Sent: 112183.332957038 Recv: 112195.130129960 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 26   ServerImgID: 26   Rejected: No
[#CLIENT#] R[891]: Sent: 112183.381174205 Recv: 112195.173027294 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 40   ServerImgID: 40   Rejected: No
[#CLIENT#] R[892]: Sent: 112183.519435330 Recv: 112195.637860294 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[893]: Sent: 112183.537481497 Recv: 112195.744596627 Opcode: IMG_BLUR        OW: 1 ClientImgID: 96   ServerImgID: 96   Rejected: No
[#CLIENT#] R[894]: Sent: 112183.686997580 Recv: 112195.762947086 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 35   ServerImgID: 35   Rejected: No HASH: f02548bdc1d694bf2aa0e1d35726601f
[#CLIENT#] R[895]: Sent: 112183.879376663 Recv: 112195.831359627 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[896]: Sent: 112184.203027872 Recv: 112195.995256503 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 34   ServerImgID: 34   Rejected: No
[#CLIENT#] R[897]: Sent: 112184.399177580 Recv: 112184.417241830 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 122  Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[898]: Sent: 112184.611882622 Recv: 112196.485723211 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[899]: Sent: 112184.677198164 Recv: 112184.785536081 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 123  Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[900]: Sent: 112185.581814706 Recv: 112196.577840503 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[901]: Sent: 112185.591119623 Recv: 112196.596587295 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 59   ServerImgID: 59   Rejected: No HASH: ca8dabad272577686d07ecf7bb519b7f
[#CLIENT#] R[902]: Sent: 112185.613874164 Recv: 112185.631510831 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 124  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[903]: Sent: 112185.791622164 Recv: 112196.880910128 Opcode: IMG_BLUR        OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No
[#CLIENT#] R[904]: Sent: 112185.835674706 Recv: 112197.131735836 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 55   ServerImgID: 55   Rejected: No
[#CLIENT#] R[905]: Sent: 112185.881101831 Recv: 112197.187075670 Opcode: IMG_BLUR        OW: 1 ClientImgID: 33   ServerImgID: 33   Rejected: No
[#CLIENT#] R[906]: Sent: 112185.901796998 Recv: 112197.290703337 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 58   ServerImgID: 58   Rejected: No HASH: 0e2dd886b2225341ca50f8f37103dbce
[#CLIENT#] R[907]: Sent: 112185.945328998 Recv: 112197.308659295 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 91   ServerImgID: 91   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[908]: Sent: 112185.993626998 Recv: 112197.356386170 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No
[#CLIENT#] R[909]: Sent: 112186.107429831 Recv: 112197.375359670 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 53   ServerImgID: 53   Rejected: No HASH: cb8a2ae1d35da5dc317ed9a391166950
[#CLIENT#] R[910]: Sent: 112186.273715581 Recv: 112197.608253837 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 42   ServerImgID: 42   Rejected: No
[#CLIENT#] R[911]: Sent: 112186.292588540 Recv: 112197.714840420 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 27   ServerImgID: 27   Rejected: No HASH: 113ea43c7c52e20533fd5c0a6c5bc11e
[#CLIENT#] R[912]: Sent: 112186.571185498 Recv: 112197.714849670 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[913]: Sent: 112186.604444831 Recv: 112197.714869170 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No
[#CLIENT#] R[914]: Sent: 112186.642480040 Recv: 112186.694841248 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 125  Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[915]: Sent: 112186.837430290 Recv: 112197.759434670 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[916]: Sent: 112186.967191748 Recv: 112198.022852295 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[917]: Sent: 112187.135037290 Recv: 112187.153381290 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 126  Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[918]: Sent: 112187.186307332 Recv: 112198.110351462 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No
[#CLIENT#] R[919]: Sent: 112187.281527415 Recv: 112198.213071337 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No HASH: a669a8b1c741bbd02a88795289a0e8ac
[#CLIENT#] R[920]: Sent: 112187.629221665 Recv: 112198.213085379 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 51   ServerImgID: 51   Rejected: No
[#CLIENT#] R[921]: Sent: 112187.666052290 Recv: 112198.229248004 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 71   ServerImgID: 71   Rejected: No
[#CLIENT#] R[922]: Sent: 112187.667156749 Recv: 112198.692514421 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 81   ServerImgID: 81   Rejected: No
[#CLIENT#] R[923]: Sent: 112187.842822374 Recv: 112198.779691879 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 126  ServerImgID: 126  Rejected: No
[#CLIENT#] R[924]: Sent: 112188.097846624 Recv: 112199.079599004 Opcode: IMG_BLUR        OW: 1 ClientImgID: 58   ServerImgID: 58   Rejected: No
[#CLIENT#] R[925]: Sent: 112188.105215165 Recv: 112199.134877504 Opcode: IMG_BLUR        OW: 1 ClientImgID: 77   ServerImgID: 77   Rejected: No
[#CLIENT#] R[926]: Sent: 112188.118637832 Recv: 112199.384162713 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 23   ServerImgID: 23   Rejected: No
[#CLIENT#] R[927]: Sent: 112188.123663207 Recv: 112199.848176671 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 101  ServerImgID: 101  Rejected: No
[#CLIENT#] R[928]: Sent: 112188.243864582 Recv: 112199.955448963 Opcode: IMG_BLUR        OW: 1 ClientImgID: 57   ServerImgID: 57   Rejected: No
[#CLIENT#] R[929]: Sent: 112188.516236874 Recv: 112200.059478546 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No HASH: 601af64569241055b07d9a99f0c670a1
[#CLIENT#] R[930]: Sent: 112188.542851707 Recv: 112200.225212546 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[931]: Sent: 112188.633294832 Recv: 112200.245616921 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[932]: Sent: 112188.644782624 Recv: 112200.708636005 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No
[#CLIENT#] R[933]: Sent: 112189.013190374 Recv: 112200.715918296 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[934]: Sent: 112189.533746583 Recv: 112200.768877546 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No HASH: 12c73cb1e8f64e1922959be2a9d982a0
[#CLIENT#] R[935]: Sent: 112189.607790750 Recv: 112200.768932713 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 51   ServerImgID: 51   Rejected: No
[#CLIENT#] R[936]: Sent: 112189.865447916 Recv: 112200.787466505 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No HASH: 9a2938e4f0d7513d21fe58144e3560d3
[#CLIENT#] R[937]: Sent: 112189.914147958 Recv: 112200.805487297 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 26   ServerImgID: 26   Rejected: No HASH: 2cc529524a171427ba242fcf8a09b6ff
[#CLIENT#] R[938]: Sent: 112189.944137083 Recv: 112200.840417838 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No HASH: 2767be6f95d5d7f6dee66214219c59a2
[#CLIENT#] R[939]: Sent: 112190.205455125 Recv: 112201.031543588 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 116  ServerImgID: 116  Rejected: No
[#CLIENT#] R[940]: Sent: 112190.212721500 Recv: 112201.115231755 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[941]: Sent: 112190.281154791 Recv: 112201.364806630 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 54   ServerImgID: 54   Rejected: No
[#CLIENT#] R[942]: Sent: 112190.328652958 Recv: 112190.363158000 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 127  Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[943]: Sent: 112190.469253375 Recv: 112201.456108005 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 53   ServerImgID: 53   Rejected: No
[#CLIENT#] R[944]: Sent: 112190.562377500 Recv: 112201.543519339 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 66   ServerImgID: 66   Rejected: No
[#CLIENT#] R[945]: Sent: 112190.718874792 Recv: 112201.794131964 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[946]: Sent: 112190.746970292 Recv: 112201.800949880 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 107  ServerImgID: 107  Rejected: No
[#CLIENT#] R[947]: Sent: 112190.801024000 Recv: 112201.963787005 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 118  ServerImgID: 118  Rejected: No
[#CLIENT#] R[948]: Sent: 112191.074629292 Recv: 112201.981858422 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 38   ServerImgID: 38   Rejected: No HASH: b8104132493de7040858ff7f6ba4b1e0
[#CLIENT#] R[949]: Sent: 112191.362069875 Recv: 112202.048127839 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 114  ServerImgID: 114  Rejected: No
[#CLIENT#] R[950]: Sent: 112191.377051375 Recv: 112202.134758255 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 122  ServerImgID: 122  Rejected: No
[#CLIENT#] R[951]: Sent: 112191.449313459 Recv: 112202.153536297 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 114  ServerImgID: 114  Rejected: No HASH: 392626c80f548779a200c8ec6e46c645
[#CLIENT#] R[952]: Sent: 112191.492680375 Recv: 112202.223690506 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 38   ServerImgID: 38   Rejected: No
[#CLIENT#] R[953]: Sent: 112191.601049625 Recv: 112202.230674256 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 88   ServerImgID: 88   Rejected: No
[#CLIENT#] R[954]: Sent: 112191.632731375 Recv: 112202.396041756 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 92   ServerImgID: 92   Rejected: No
[#CLIENT#] R[955]: Sent: 112191.643586000 Recv: 112202.480139339 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 82   ServerImgID: 82   Rejected: No
[#CLIENT#] R[956]: Sent: 112191.669161250 Recv: 112202.567406047 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[957]: Sent: 112191.814030001 Recv: 112191.919325417 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 128  Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[958]: Sent: 112192.106608667 Recv: 112202.829802756 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 67   ServerImgID: 67   Rejected: No
[#CLIENT#] R[959]: Sent: 112192.387122001 Recv: 112202.836796881 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 38   ServerImgID: 38   Rejected: No
[#CLIENT#] R[960]: Sent: 112192.410494668 Recv: 112202.998204923 Opcode: IMG_BLUR        OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[961]: Sent: 112192.575824501 Recv: 112203.085525589 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 47   ServerImgID: 47   Rejected: No
[#CLIENT#] R[962]: Sent: 112192.616821584 Recv: 112203.554602839 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[963]: Sent: 112192.844639043 Recv: 112203.637919673 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 91   ServerImgID: 91   Rejected: No
[#CLIENT#] R[964]: Sent: 112192.907955959 Recv: 112203.692876923 Opcode: IMG_BLUR        OW: 1 ClientImgID: 77   ServerImgID: 77   Rejected: No
[#CLIENT#] R[965]: Sent: 112192.912514626 Recv: 112203.706352548 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 49   ServerImgID: 49   Rejected: No
[#CLIENT#] R[966]: Sent: 112192.928197751 Recv: 112192.946277543 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 129  Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[967]: Sent: 112193.065552084 Recv: 112203.813621923 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 128  ServerImgID: 128  Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[968]: Sent: 112193.074350668 Recv: 112203.848712631 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 87   ServerImgID: 87   Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[969]: Sent: 112193.157505418 Recv: 112193.175800501 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 130  Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[970]: Sent: 112193.182560168 Recv: 112203.880223048 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No
[#CLIENT#] R[971]: Sent: 112193.289312001 Recv: 112204.041154215 Opcode: IMG_BLUR        OW: 1 ClientImgID: 43   ServerImgID: 43   Rejected: No
[#CLIENT#] R[972]: Sent: 112193.467036126 Recv: 112204.304054798 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 85   ServerImgID: 85   Rejected: No
[#CLIENT#] R[973]: Sent: 112193.810464585 Recv: 112204.322260923 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 86   ServerImgID: 86   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[974]: Sent: 112193.938068960 Recv: 112204.388410840 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[975]: Sent: 112194.056885252 Recv: 112194.108610293 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 131  Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[976]: Sent: 112194.166586377 Recv: 112204.472343257 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 33   ServerImgID: 33   Rejected: No
[#CLIENT#] R[977]: Sent: 112194.188988835 Recv: 112204.528786423 Opcode: IMG_BLUR        OW: 1 ClientImgID: 120  ServerImgID: 120  Rejected: No
[#CLIENT#] R[978]: Sent: 112194.238952210 Recv: 112194.343184793 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 4    ServerImgID: 132  Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[979]: Sent: 112194.572913002 Recv: 112204.546914090 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 88   ServerImgID: 88   Rejected: No HASH: 3b3e20aa776ada5ed79da1b1242d54fd
[#CLIENT#] R[980]: Sent: 112194.674384919 Recv: 112204.616061298 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[981]: Sent: 112194.810989627 Recv: 112204.699865465 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 72   ServerImgID: 72   Rejected: No
[#CLIENT#] R[982]: Sent: 112194.944318794 Recv: 112205.001860965 Opcode: IMG_BLUR        OW: 1 ClientImgID: 101  ServerImgID: 101  Rejected: No
[#CLIENT#] R[983]: Sent: 112195.273993294 Recv: 112195.307789544 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 2    ServerImgID: 133  Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[984]: Sent: 112195.316878252 Recv: 112205.019993632 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 79   ServerImgID: 79   Rejected: No HASH: ef8229e5c754a6f351669a8d377268c2
[#CLIENT#] R[985]: Sent: 112195.364578086 Recv: 112205.252051007 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 80   ServerImgID: 80   Rejected: No
[#CLIENT#] R[986]: Sent: 112195.648905294 Recv: 112205.516878507 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[987]: Sent: 112195.649022086 Recv: 112205.537601549 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 53   ServerImgID: 53   Rejected: No HASH: 1f1c8796819b3be90020a1649fbceb45
[#CLIENT#] R[988]: Sent: 112195.687758211 Recv: 112195.705355794 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 134  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[989]: Sent: 112195.816878211 Recv: 112205.818469007 Opcode: IMG_BLUR        OW: 1 ClientImgID: 63   ServerImgID: 63   Rejected: No
[#CLIENT#] R[990]: Sent: 112196.321308086 Recv: 112205.902922799 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 89   ServerImgID: 89   Rejected: No
[#CLIENT#] R[991]: Sent: 112196.389428878 Recv: 112205.959820591 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 90   ServerImgID: 90   Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[992]: Sent: 112196.782620128 Recv: 112196.834441170 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 3    ServerImgID: 135  Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[993]: Sent: 112196.990482128 Recv: 112206.203596966 Opcode: IMG_BLUR        OW: 1 ClientImgID: 84   ServerImgID: 84   Rejected: No
[#CLIENT#] R[994]: Sent: 112197.161768336 Recv: 112206.287410507 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 124  ServerImgID: 124  Rejected: No
[#CLIENT#] R[995]: Sent: 112197.308671462 Recv: 112206.305510466 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 72   ServerImgID: 72   Rejected: No HASH: 5ea1fa06c4cda67fa5c705c720733694
[#CLIENT#] R[996]: Sent: 112197.747701087 Recv: 112206.550270008 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 85   ServerImgID: 85   Rejected: No
[#CLIENT#] R[997]: Sent: 112197.785540712 Recv: 112206.849792133 Opcode: IMG_BLUR        OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[998]: Sent: 112197.809765462 Recv: 112206.887107258 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 102  ServerImgID: 102  Rejected: No HASH: 2789dd1ef70d8504357a520edd47d455
[#CLIENT#] R[999]: Sent: 112197.957392503 Recv: 112197.974693587 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 136  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31"""

# Input client report, and the imgop, plot the CDF of response times


def CDF(client_report):

    # Code below is for calculating individual response times (copied from hw5 bc.py)
    pattern = re.compile(r"Sent: (\d+\.\d+) Recv: (\d+\.\d+)")

    matches = pattern.findall(client_report)

    resp_times = [float(recv) - float(sent) for sent, recv in matches]

    # Compute CDF
    data_sorted = np.sort(resp_times)
    p = 1. * np.arange(1, len(resp_times)+1) / (len(resp_times))

    avg = np.mean(resp_times)
    percentile_99 = np.percentile(resp_times, 99)

    # Plot
    plt.figure(figsize=(10, 7))

    plt.plot(data_sorted, p, marker='.', linestyle='none')
    plt.axvline(x=avg, color='r', linestyle='--',
                label=f'Average: {avg:.2f}')
    plt.axvline(x=percentile_99, color='g', linestyle='--',
                label=f'99th Percentile: {percentile_99:.2f}')

    plt.xlabel('Response Time')
    plt.ylabel('CDF')
    plt.legend()
    plt.title(f'CDF of Response Times')
    plt.grid(True)
    plt.show()


CDF(run0)
