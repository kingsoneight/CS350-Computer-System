import re


run1 = """
[#CLIENT#] R[0]: Sent: 86084.361916112 Recv: 86084.379329112 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[1]: Sent: 86084.470921403 Recv: 86084.555421195 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[2]: Sent: 86084.547525820 Recv: 86084.673072237 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[3]: Sent: 86084.558590737 Recv: 86084.733935445 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[4]: Sent: 86084.574899445 Recv: 86084.751576695 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No HASH: cd2fe665a682aae0a997597a0e89b352
[#CLIENT#] R[5]: Sent: 86084.624506903 Recv: 86084.644864028 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 1    Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[6]: Sent: 86084.796759112 Recv: 86084.851315904 Opcode: IMG_BLUR        OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[7]: Sent: 86084.860088154 Recv: 86084.877799570 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 2    Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[8]: Sent: 86084.878629279 Recv: 86084.934994279 Opcode: IMG_BLUR        OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[9]: Sent: 86084.960190404 Recv: 86084.977583445 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[10]: Sent: 86084.977617279 Recv: 86085.061793237 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[11]: Sent: 86084.989965154 Recv: 86085.148640279 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[12]: Sent: 86085.037402320 Recv: 86085.165447654 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[13]: Sent: 86085.074591904 Recv: 86085.209732862 Opcode: IMG_BLUR        OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[14]: Sent: 86085.091923945 Recv: 86085.296280404 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[15]: Sent: 86085.165414112 Recv: 86085.387550446 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[16]: Sent: 86085.182110529 Recv: 86085.441983862 Opcode: IMG_BLUR        OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[17]: Sent: 86085.307842112 Recv: 86085.525994321 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[18]: Sent: 86085.345215445 Recv: 86085.532765529 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[19]: Sent: 86085.399660029 Recv: 86085.617134654 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[20]: Sent: 86085.403036237 Recv: 86085.671287904 Opcode: IMG_BLUR        OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[21]: Sent: 86085.406319404 Recv: 86085.758721321 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[22]: Sent: 86085.522586071 Recv: 86085.842678362 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[23]: Sent: 86085.561420321 Recv: 86085.578994987 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 3    Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[24]: Sent: 86085.614946529 Recv: 86085.896717654 Opcode: IMG_BLUR        OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[25]: Sent: 86085.617032779 Recv: 86085.952939779 Opcode: IMG_BLUR        OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[26]: Sent: 86085.750612612 Recv: 86086.009254154 Opcode: IMG_BLUR        OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[27]: Sent: 86085.817769779 Recv: 86086.098521821 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[28]: Sent: 86085.876049987 Recv: 86086.181529404 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[29]: Sent: 86085.982131654 Recv: 86086.239475113 Opcode: IMG_BLUR        OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[30]: Sent: 86085.995171362 Recv: 86086.326079821 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[31]: Sent: 86086.053227529 Recv: 86086.071512488 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 4    Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[32]: Sent: 86086.125064321 Recv: 86086.410689279 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[33]: Sent: 86086.253946571 Recv: 86086.272224946 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 5    Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[34]: Sent: 86086.329893821 Recv: 86086.502180113 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[35]: Sent: 86086.342119279 Recv: 86086.590693571 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[36]: Sent: 86086.350147238 Recv: 86086.679450654 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[37]: Sent: 86086.378476571 Recv: 86086.687435863 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[38]: Sent: 86086.455647029 Recv: 86086.705116904 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No HASH: c9e9acb37a12747a13739fb3fe21a308
[#CLIENT#] R[39]: Sent: 86086.468545238 Recv: 86086.723447404 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No HASH: 1978a21da2d4933f3be508d60938f8e3
[#CLIENT#] R[40]: Sent: 86086.509222571 Recv: 86086.771914446 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[41]: Sent: 86086.627934571 Recv: 86086.855998321 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[42]: Sent: 86086.662194363 Recv: 86086.946638113 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[43]: Sent: 86086.798907113 Recv: 86087.030553280 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[44]: Sent: 86086.868231530 Recv: 86087.114434321 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[45]: Sent: 86086.881490905 Recv: 86086.898848030 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 6    Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[46]: Sent: 86086.906956488 Recv: 86087.202397821 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[47]: Sent: 86086.985874863 Recv: 86087.305443030 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[48]: Sent: 86086.989778946 Recv: 86087.386015738 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[49]: Sent: 86087.026656738 Recv: 86087.474438155 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[50]: Sent: 86087.106612113 Recv: 86087.565365363 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[51]: Sent: 86087.277830155 Recv: 86087.652266363 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[52]: Sent: 86087.282765446 Recv: 86087.671714072 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No HASH: 73c811d543c159b93167a1179dbfef06
[#CLIENT#] R[53]: Sent: 86087.286855655 Recv: 86087.305436530 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 7    Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[54]: Sent: 86087.336358780 Recv: 86087.708727947 Opcode: IMG_BLUR        OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[55]: Sent: 86087.406841780 Recv: 86087.796754155 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[56]: Sent: 86088.004636113 Recv: 86088.091773697 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[57]: Sent: 86088.011390780 Recv: 86088.180388947 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[58]: Sent: 86088.113642030 Recv: 86088.132168530 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 8    Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[59]: Sent: 86088.260419239 Recv: 86088.268429197 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[60]: Sent: 86088.269367280 Recv: 86088.326774822 Opcode: IMG_BLUR        OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[61]: Sent: 86088.355050614 Recv: 86088.373790072 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No HASH: 73c811d543c159b93167a1179dbfef06
[#CLIENT#] R[62]: Sent: 86088.398398364 Recv: 86088.485327614 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[63]: Sent: 86088.403674864 Recv: 86088.541523905 Opcode: IMG_BLUR        OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[64]: Sent: 86088.421832697 Recv: 86088.548590780 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[65]: Sent: 86088.526880697 Recv: 86088.632331114 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[66]: Sent: 86088.528742697 Recv: 86088.715839155 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[67]: Sent: 86088.658561197 Recv: 86088.734724489 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No HASH: ebfa87f9ffc7ccdd1988ce37c2f1c508
[#CLIENT#] R[68]: Sent: 86088.852816239 Recv: 86088.871071822 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No HASH: 6b42d28be14d6b3561ecde7d488bd7a1
[#CLIENT#] R[69]: Sent: 86089.058379614 Recv: 86089.115052697 Opcode: IMG_BLUR        OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[70]: Sent: 86089.067371406 Recv: 86089.085009864 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 9    Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[71]: Sent: 86089.089018156 Recv: 86089.201862197 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[72]: Sent: 86089.138713572 Recv: 86089.156952489 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 10   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[73]: Sent: 86089.175959531 Recv: 86089.208610614 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[74]: Sent: 86089.179891447 Recv: 86089.297231531 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[75]: Sent: 86089.232559864 Recv: 86089.316652656 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No HASH: 6b42d28be14d6b3561ecde7d488bd7a1
[#CLIENT#] R[76]: Sent: 86089.249032906 Recv: 86089.339027572 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[77]: Sent: 86089.255063239 Recv: 86089.391174156 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[78]: Sent: 86089.399496281 Recv: 86089.483286614 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[79]: Sent: 86089.493621739 Recv: 86089.512197114 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No HASH: 5270006985a5f40de12fea9382d69f27
[#CLIENT#] R[80]: Sent: 86089.514807822 Recv: 86089.521559156 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[81]: Sent: 86089.528161614 Recv: 86089.612350781 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[82]: Sent: 86089.561065906 Recv: 86089.699691489 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[83]: Sent: 86089.571162448 Recv: 86089.783630489 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[84]: Sent: 86089.597934156 Recv: 86089.824032448 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[85]: Sent: 86089.648714781 Recv: 86089.666210531 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 11   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[86]: Sent: 86089.713184864 Recv: 86089.846325823 Opcode: IMG_BLUR        OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[87]: Sent: 86089.733115656 Recv: 86089.932634573 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[88]: Sent: 86089.860012114 Recv: 86089.989562239 Opcode: IMG_BLUR        OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[89]: Sent: 86089.874904448 Recv: 86090.043745073 Opcode: IMG_BLUR        OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[90]: Sent: 86089.890018448 Recv: 86090.097866656 Opcode: IMG_BLUR        OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[91]: Sent: 86089.894961031 Recv: 86090.104572573 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[92]: Sent: 86089.937994073 Recv: 86090.192746906 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[93]: Sent: 86089.955101448 Recv: 86090.247019615 Opcode: IMG_BLUR        OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[94]: Sent: 86089.975119448 Recv: 86090.333713990 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[95]: Sent: 86089.975312031 Recv: 86090.389809906 Opcode: IMG_BLUR        OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[96]: Sent: 86089.985753406 Recv: 86090.476672948 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[97]: Sent: 86090.111397656 Recv: 86090.495496031 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No HASH: 70cf2014ae70367eb9f0b3a744d9fc82
[#CLIENT#] R[98]: Sent: 86090.117879948 Recv: 86090.563797490 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[99]: Sent: 86090.192322739 Recv: 86090.654329740 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[100]: Sent: 86090.291402865 Recv: 86090.741296156 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[101]: Sent: 86090.331141865 Recv: 86090.796055781 Opcode: IMG_BLUR        OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[102]: Sent: 86090.451363990 Recv: 86090.879772656 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[103]: Sent: 86090.495507031 Recv: 86090.513846531 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 12   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[104]: Sent: 86090.613826615 Recv: 86090.920026573 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[105]: Sent: 86090.708377115 Recv: 86090.970629490 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[106]: Sent: 86090.718361781 Recv: 86090.977671782 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[107]: Sent: 86090.725878115 Recv: 86091.064191823 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[108]: Sent: 86090.816957240 Recv: 86091.151201407 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[109]: Sent: 86090.829535615 Recv: 86091.169607907 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No HASH: 3289f9eebf73d9017eaff4e0959053d7
[#CLIENT#] R[110]: Sent: 86090.837020531 Recv: 86091.205511323 Opcode: IMG_BLUR        OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[111]: Sent: 86090.971389365 Recv: 86091.293874782 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[112]: Sent: 86091.062090115 Recv: 86091.301901657 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[113]: Sent: 86091.082512032 Recv: 86091.100169282 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 13   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[114]: Sent: 86091.147109823 Recv: 86091.357833032 Opcode: IMG_BLUR        OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[115]: Sent: 86091.150899490 Recv: 86091.413925198 Opcode: IMG_BLUR        OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[116]: Sent: 86091.173519323 Recv: 86091.500766073 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[117]: Sent: 86091.178353657 Recv: 86091.589103282 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[118]: Sent: 86091.222176365 Recv: 86091.643309490 Opcode: IMG_BLUR        OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[119]: Sent: 86091.293920823 Recv: 86091.699276365 Opcode: IMG_BLUR        OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[120]: Sent: 86091.401264032 Recv: 86091.755656865 Opcode: IMG_BLUR        OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[121]: Sent: 86091.412991782 Recv: 86091.839562532 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[122]: Sent: 86091.501612573 Recv: 86091.926364532 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[123]: Sent: 86091.521370032 Recv: 86091.945307990 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No HASH: e2efeefd1cbbc9e3b60573ef66bbfb73
[#CLIENT#] R[124]: Sent: 86091.730879324 Recv: 86091.982834115 Opcode: IMG_BLUR        OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[125]: Sent: 86091.738250699 Recv: 86091.990792157 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[126]: Sent: 86091.814746824 Recv: 86092.047693990 Opcode: IMG_BLUR        OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[127]: Sent: 86091.820876949 Recv: 86092.136132240 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[128]: Sent: 86091.823411282 Recv: 86092.224837990 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[129]: Sent: 86091.884963407 Recv: 86092.309561699 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[130]: Sent: 86091.985187990 Recv: 86092.393626741 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[131]: Sent: 86092.009357074 Recv: 86092.412231699 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No HASH: fbc784159e6b8d4e474219599d0ddef4
[#CLIENT#] R[132]: Sent: 86092.092194490 Recv: 86092.485013866 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[133]: Sent: 86092.094970865 Recv: 86092.112994282 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 14   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[134]: Sent: 86092.171814282 Recv: 86092.494341282 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[135]: Sent: 86092.216435907 Recv: 86092.494344741 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[136]: Sent: 86092.261673407 Recv: 86092.584076199 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[137]: Sent: 86092.371495324 Recv: 86092.590799157 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[138]: Sent: 86092.418576782 Recv: 86092.679740282 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[139]: Sent: 86092.463954699 Recv: 86092.481316574 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 15   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[140]: Sent: 86092.484951241 Recv: 86092.764287324 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[141]: Sent: 86092.494319116 Recv: 86092.848236866 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[142]: Sent: 86092.582014074 Recv: 86092.866879449 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No HASH: faab646f0cde255316ec04bec6f22d07
[#CLIENT#] R[143]: Sent: 86092.687373449 Recv: 86092.937133199 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[144]: Sent: 86092.741259199 Recv: 86093.023852116 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[145]: Sent: 86092.816637991 Recv: 86093.114723741 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[146]: Sent: 86092.835093449 Recv: 86093.169063158 Opcode: IMG_BLUR        OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[147]: Sent: 86092.882509782 Recv: 86093.188452658 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No HASH: c0eff8764c6853ed6f602c42746bdd59
[#CLIENT#] R[148]: Sent: 86092.958764824 Recv: 86093.188465908 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[149]: Sent: 86092.984438699 Recv: 86093.264621199 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[150]: Sent: 86092.997599616 Recv: 86093.348843449 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[151]: Sent: 86093.006025699 Recv: 86093.364995158 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[152]: Sent: 86093.029971157 Recv: 86093.447900949 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[153]: Sent: 86093.096853241 Recv: 86093.539800658 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[154]: Sent: 86093.137061491 Recv: 86093.610562283 Opcode: IMG_BLUR        OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[155]: Sent: 86093.220093491 Recv: 86093.702813491 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[156]: Sent: 86093.272060074 Recv: 86093.743373158 Opcode: IMG_BLUR        OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[157]: Sent: 86093.364967199 Recv: 86093.799362491 Opcode: IMG_BLUR        OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[158]: Sent: 86093.401547074 Recv: 86093.891346866 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[159]: Sent: 86093.465022491 Recv: 86093.979437908 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[160]: Sent: 86093.473380783 Recv: 86094.066761033 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[161]: Sent: 86093.531333491 Recv: 86094.153280575 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[162]: Sent: 86093.591624324 Recv: 86094.209327950 Opcode: IMG_BLUR        OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[163]: Sent: 86093.591938949 Recv: 86093.610551366 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 16   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[164]: Sent: 86093.663806324 Recv: 86094.292899825 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[165]: Sent: 86093.684722866 Recv: 86093.702820866 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 17   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[166]: Sent: 86093.755777533 Recv: 86094.384072325 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[167]: Sent: 86093.766114200 Recv: 86094.470641783 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[168]: Sent: 86093.854425616 Recv: 86094.557424908 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[169]: Sent: 86093.865058200 Recv: 86094.577083742 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No HASH: 73945748f7244a6b8465a2e91b7e99ea
[#CLIENT#] R[170]: Sent: 86093.966688491 Recv: 86094.646277617 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[171]: Sent: 86094.101499700 Recv: 86094.730030950 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[172]: Sent: 86094.141628575 Recv: 86094.813763783 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[173]: Sent: 86094.181862741 Recv: 86094.820791158 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[174]: Sent: 86094.266035491 Recv: 86094.840474992 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No HASH: 87db525c3ec4071155dc5f70dd388a0f
[#CLIENT#] R[175]: Sent: 86094.534091658 Recv: 86094.552128908 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 18   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[176]: Sent: 86094.655733283 Recv: 86094.904809992 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[177]: Sent: 86094.726980742 Recv: 86094.985258658 Opcode: IMG_BLUR        OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[178]: Sent: 86094.742258450 Recv: 86095.016091408 Opcode: IMG_BLUR        OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[179]: Sent: 86094.751429492 Recv: 86095.023077825 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[180]: Sent: 86094.854640408 Recv: 86095.042433783 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No HASH: 18743a90a1c8b73697150fda5f9497ce
[#CLIENT#] R[181]: Sent: 86094.902012700 Recv: 86095.061335450 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No HASH: 638d7ca114bb6a1a36751eb706d5b10c
[#CLIENT#] R[182]: Sent: 86094.940714283 Recv: 86095.110179908 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[183]: Sent: 86094.942412783 Recv: 86094.959884825 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 19   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[184]: Sent: 86095.061348367 Recv: 86095.198372700 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[185]: Sent: 86095.095033950 Recv: 86095.217159200 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No HASH: e2e2b925039144f36533fe19c5abed0a
[#CLIENT#] R[186]: Sent: 86095.179247367 Recv: 86095.235953742 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No HASH: 18743a90a1c8b73697150fda5f9497ce
[#CLIENT#] R[187]: Sent: 86095.235961825 Recv: 86095.360098325 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[188]: Sent: 86095.250176492 Recv: 86095.423069367 Opcode: IMG_BLUR        OW: 1 ClientImgID: 17   ServerImgID: 17   Rejected: No
[#CLIENT#] R[189]: Sent: 86095.313418784 Recv: 86095.331506242 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 20   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[190]: Sent: 86095.375204909 Recv: 86095.392789492 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 21   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[191]: Sent: 86095.659390367 Recv: 86095.743552700 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[192]: Sent: 86095.710608200 Recv: 86095.830386992 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[193]: Sent: 86095.723049034 Recv: 86095.913960159 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[194]: Sent: 86095.790035617 Recv: 86095.932790201 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[195]: Sent: 86095.885137159 Recv: 86095.951611826 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 17   ServerImgID: 17   Rejected: No HASH: 1d58d784c91555c8541eca0755b4bb5a
[#CLIENT#] R[196]: Sent: 86095.999851951 Recv: 86096.017492617 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 22   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[197]: Sent: 86096.055931492 Recv: 86096.074923159 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No HASH: cbea9a5b7219df360b4b3688c3a874ba
[#CLIENT#] R[198]: Sent: 86096.205603034 Recv: 86096.298961201 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[199]: Sent: 86096.376661201 Recv: 86096.394643951 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 23   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[200]: Sent: 86096.470395784 Recv: 86096.555073451 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[201]: Sent: 86096.485323117 Recv: 86096.575056326 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 17   ServerImgID: 17   Rejected: No HASH: 1d58d784c91555c8541eca0755b4bb5a
[#CLIENT#] R[202]: Sent: 86096.505503034 Recv: 86096.642270951 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[203]: Sent: 86096.545944326 Recv: 86096.661390076 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No HASH: ef8229e5c754a6f351669a8d377268c2
[#CLIENT#] R[204]: Sent: 86096.578474534 Recv: 86096.679790493 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No HASH: 2db87292a19f21c5dffa0df6872eeb8f
[#CLIENT#] R[205]: Sent: 86096.702669909 Recv: 86096.709719118 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 17   ServerImgID: 17   Rejected: No
[#CLIENT#] R[206]: Sent: 86096.802996868 Recv: 86096.822134909 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No HASH: cbea9a5b7219df360b4b3688c3a874ba
[#CLIENT#] R[207]: Sent: 86096.822142284 Recv: 86096.840306451 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No HASH: 9501a7ff4534a1193b3fc6fa69efaad3
[#CLIENT#] R[208]: Sent: 86096.878618659 Recv: 86096.962926659 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[209]: Sent: 86096.919800534 Recv: 86096.937510493 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 24   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[210]: Sent: 86096.938474493 Recv: 86097.017212076 Opcode: IMG_BLUR        OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[211]: Sent: 86097.067186701 Recv: 86097.124568576 Opcode: IMG_BLUR        OW: 1 ClientImgID: 16   ServerImgID: 16   Rejected: No
[#CLIENT#] R[212]: Sent: 86097.176327493 Recv: 86097.265246701 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[213]: Sent: 86097.206066284 Recv: 86097.349137326 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[214]: Sent: 86097.257037576 Recv: 86097.435710410 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 21   ServerImgID: 21   Rejected: No
[#CLIENT#] R[215]: Sent: 86097.274398785 Recv: 86097.526356826 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[216]: Sent: 86097.389270535 Recv: 86097.533349160 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[217]: Sent: 86097.405243826 Recv: 86097.617434660 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[218]: Sent: 86097.505663701 Recv: 86097.625357743 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[219]: Sent: 86097.634907660 Recv: 86097.723334118 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[220]: Sent: 86097.644082660 Recv: 86097.765170118 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[221]: Sent: 86097.653799410 Recv: 86097.765177118 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No
[#CLIENT#] R[222]: Sent: 86097.800625868 Recv: 86097.855017576 Opcode: IMG_BLUR        OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[223]: Sent: 86097.807044993 Recv: 86097.946644118 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[224]: Sent: 86097.930466326 Recv: 86097.965561660 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No HASH: 35a883f5d3035c55d6dce2432d42b949
[#CLIENT#] R[225]: Sent: 86097.934159368 Recv: 86097.983573243 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No HASH: d9b5ed73a1a400cba967dee2d74aacfe
[#CLIENT#] R[226]: Sent: 86097.983580452 Recv: 86097.991601327 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No
[#CLIENT#] R[227]: Sent: 86098.105364618 Recv: 86098.192265285 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 22   ServerImgID: 22   Rejected: No
[#CLIENT#] R[228]: Sent: 86098.107188993 Recv: 86098.199639410 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[229]: Sent: 86098.177241910 Recv: 86098.209197952 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[230]: Sent: 86098.179099952 Recv: 86098.297749577 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[231]: Sent: 86098.233345118 Recv: 86098.338469993 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[232]: Sent: 86098.343447493 Recv: 86098.434412827 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[233]: Sent: 86098.346049035 Recv: 86098.528945077 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[234]: Sent: 86098.406060285 Recv: 86098.605443993 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[235]: Sent: 86098.424851993 Recv: 86098.624636160 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 21   ServerImgID: 21   Rejected: No HASH: 54ef7553d21733e88e2e512be41c798f
[#CLIENT#] R[236]: Sent: 86098.507762035 Recv: 86098.624641743 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 16   ServerImgID: 16   Rejected: No
[#CLIENT#] R[237]: Sent: 86098.510557493 Recv: 86098.528938452 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 25   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[238]: Sent: 86098.542919743 Recv: 86098.625160410 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[239]: Sent: 86098.545940660 Recv: 86098.704464452 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[240]: Sent: 86098.548838118 Recv: 86098.793031369 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[241]: Sent: 86098.563706285 Recv: 86098.581239118 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 26   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[242]: Sent: 86098.625110535 Recv: 86098.847056119 Opcode: IMG_BLUR        OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[243]: Sent: 86098.755399285 Recv: 86098.935473869 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[244]: Sent: 86098.820795327 Recv: 86098.977023452 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 22   ServerImgID: 22   Rejected: No
[#CLIENT#] R[245]: Sent: 86098.871026410 Recv: 86099.030283785 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[246]: Sent: 86099.005119744 Recv: 86099.117078619 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[247]: Sent: 86099.042123827 Recv: 86099.060399785 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 27   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[248]: Sent: 86099.117356619 Recv: 86099.205661285 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No
[#CLIENT#] R[249]: Sent: 86099.133060535 Recv: 86099.263176994 Opcode: IMG_BLUR        OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[250]: Sent: 86099.145153660 Recv: 86099.346535536 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[251]: Sent: 86099.202710244 Recv: 86099.432592952 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 22   ServerImgID: 22   Rejected: No
[#CLIENT#] R[252]: Sent: 86099.298409994 Recv: 86099.520783744 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No
[#CLIENT#] R[253]: Sent: 86099.353566661 Recv: 86099.604644786 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[254]: Sent: 86099.367991119 Recv: 86099.623688827 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No HASH: 35a883f5d3035c55d6dce2432d42b949
[#CLIENT#] R[255]: Sent: 86099.404146244 Recv: 86099.696174452 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[256]: Sent: 86099.442074952 Recv: 86099.799748286 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[257]: Sent: 86099.508855952 Recv: 86099.818446161 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No HASH: 98b9ed3ea6eae02e2969162cccbd71f7
[#CLIENT#] R[258]: Sent: 86099.511136286 Recv: 86099.875675911 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 22   ServerImgID: 22   Rejected: No
[#CLIENT#] R[259]: Sent: 86099.544561244 Recv: 86099.930035869 Opcode: IMG_BLUR        OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[260]: Sent: 86099.630401661 Recv: 86099.960363786 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[261]: Sent: 86099.634521161 Recv: 86100.029403160 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 16   ServerImgID: 16   Rejected: No
[#CLIENT#] R[262]: Sent: 86099.763016286 Recv: 86100.113345660 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[263]: Sent: 86099.777096869 Recv: 86100.185065369 Opcode: IMG_BLUR        OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[264]: Sent: 86099.782015786 Recv: 86099.799736786 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 28   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[265]: Sent: 86099.818457411 Recv: 86100.222139660 Opcode: IMG_BLUR        OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[266]: Sent: 86099.893628786 Recv: 86100.279679202 Opcode: IMG_BLUR        OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[267]: Sent: 86099.960335411 Recv: 86100.299094452 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No HASH: 3ad8c8d9c6b419108c52c240bbd998ed
[#CLIENT#] R[268]: Sent: 86099.965444327 Recv: 86100.366835244 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[269]: Sent: 86099.970839702 Recv: 86100.422850660 Opcode: IMG_BLUR        OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[270]: Sent: 86100.053830869 Recv: 86100.519527244 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No
[#CLIENT#] R[271]: Sent: 86100.070088827 Recv: 86100.562854119 Opcode: IMG_BLUR        OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[272]: Sent: 86100.141644244 Recv: 86100.159798785 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 29   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[273]: Sent: 86100.253108827 Recv: 86100.569695994 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[274]: Sent: 86100.299103869 Recv: 86100.316592577 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 30   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[275]: Sent: 86100.336129702 Recv: 86100.677096202 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[276]: Sent: 86100.340418160 Recv: 86100.710888327 Opcode: IMG_BLUR        OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[277]: Sent: 86100.394358535 Recv: 86100.721429994 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 29   ServerImgID: 29   Rejected: No
[#CLIENT#] R[278]: Sent: 86100.438043994 Recv: 86100.808289536 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 29   ServerImgID: 29   Rejected: No
[#CLIENT#] R[279]: Sent: 86100.475707410 Recv: 86100.494018202 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 31   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[280]: Sent: 86100.567149535 Recv: 86100.903516994 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[281]: Sent: 86100.603383660 Recv: 86100.983627327 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[282]: Sent: 86100.633559035 Recv: 86100.651707327 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 32   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[283]: Sent: 86100.680152494 Recv: 86101.037888452 Opcode: IMG_BLUR        OW: 1 ClientImgID: 26   ServerImgID: 26   Rejected: No
[#CLIENT#] R[284]: Sent: 86100.686934702 Recv: 86101.126456077 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[285]: Sent: 86100.762730536 Recv: 86101.212775244 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 22   ServerImgID: 22   Rejected: No
[#CLIENT#] R[286]: Sent: 86100.883296827 Recv: 86101.299571161 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[287]: Sent: 86100.885752952 Recv: 86100.903507036 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 33   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[288]: Sent: 86101.034943952 Recv: 86101.319474536 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 25   ServerImgID: 25   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[289]: Sent: 86101.080329036 Recv: 86101.319483952 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 33   ServerImgID: 33   Rejected: No
[#CLIENT#] R[290]: Sent: 86101.119121661 Recv: 86101.395292578 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[291]: Sent: 86101.162238119 Recv: 86101.449452744 Opcode: IMG_BLUR        OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[292]: Sent: 86101.240118827 Recv: 86101.469041411 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 33   ServerImgID: 33   Rejected: No HASH: a46fa185b469892706544a2d486bf142
[#CLIENT#] R[293]: Sent: 86101.245282369 Recv: 86101.262798036 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 34   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[294]: Sent: 86101.331471577 Recv: 86101.537761619 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No
[#CLIENT#] R[295]: Sent: 86101.420541578 Recv: 86101.578032661 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 21   ServerImgID: 21   Rejected: No
[#CLIENT#] R[296]: Sent: 86101.469051119 Recv: 86101.628979036 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[297]: Sent: 86101.512321119 Recv: 86101.649099661 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 17   ServerImgID: 17   Rejected: No HASH: 87504e6eb7330f31ab17020c33a18aa9
[#CLIENT#] R[298]: Sent: 86101.582871869 Recv: 86101.668357786 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[299]: Sent: 86101.590669744 Recv: 86101.718808994 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[300]: Sent: 86101.683676078 Recv: 86101.774595953 Opcode: IMG_BLUR        OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No
[#CLIENT#] R[301]: Sent: 86101.738650244 Recv: 86101.858558619 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[302]: Sent: 86101.848343994 Recv: 86101.945103994 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No
[#CLIENT#] R[303]: Sent: 86101.864125828 Recv: 86101.953146411 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[304]: Sent: 86101.917748619 Recv: 86101.960838953 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 28   ServerImgID: 28   Rejected: No
[#CLIENT#] R[305]: Sent: 86101.953125744 Recv: 86102.030876953 Opcode: IMG_BLUR        OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[306]: Sent: 86101.960818828 Recv: 86102.096408786 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[307]: Sent: 86102.012572078 Recv: 86102.030886994 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 35   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[308]: Sent: 86102.086929495 Recv: 86102.188663453 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[309]: Sent: 86102.170791661 Recv: 86102.188631495 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 36   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[310]: Sent: 86102.233251078 Recv: 86102.250933286 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 37   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[311]: Sent: 86102.325374703 Recv: 86102.380478953 Opcode: IMG_BLUR        OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[312]: Sent: 86102.431441078 Recv: 86102.520032620 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[313]: Sent: 86102.453767328 Recv: 86102.576377703 Opcode: IMG_BLUR        OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[314]: Sent: 86102.505938536 Recv: 86102.632768745 Opcode: IMG_BLUR        OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[315]: Sent: 86102.607773036 Recv: 86102.730343120 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[316]: Sent: 86102.689749953 Recv: 86102.806396578 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 29   ServerImgID: 29   Rejected: No
[#CLIENT#] R[317]: Sent: 86102.712629578 Recv: 86102.730335036 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 38   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[318]: Sent: 86102.776044287 Recv: 86102.813452287 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[319]: Sent: 86102.804390703 Recv: 86102.870034537 Opcode: IMG_BLUR        OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[320]: Sent: 86102.835287620 Recv: 86102.953860037 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[321]: Sent: 86102.848033745 Recv: 86103.042283953 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No
[#CLIENT#] R[322]: Sent: 86102.865966787 Recv: 86103.128873412 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 35   ServerImgID: 35   Rejected: No
[#CLIENT#] R[323]: Sent: 86102.898708370 Recv: 86103.213072745 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[324]: Sent: 86102.996658037 Recv: 86103.221027912 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 28   ServerImgID: 28   Rejected: No
[#CLIENT#] R[325]: Sent: 86103.006927912 Recv: 86103.309121828 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 38   ServerImgID: 38   Rejected: No
[#CLIENT#] R[326]: Sent: 86103.024015578 Recv: 86103.360080912 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[327]: Sent: 86103.082217662 Recv: 86103.407771370 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 23   ServerImgID: 23   Rejected: No
[#CLIENT#] R[328]: Sent: 86103.242846412 Recv: 86103.416747412 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[329]: Sent: 86103.341639787 Recv: 86103.360091412 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 39   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[330]: Sent: 86103.398496412 Recv: 86103.503192829 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[331]: Sent: 86103.486722537 Recv: 86103.510128079 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No
[#CLIENT#] R[332]: Sent: 86103.512757370 Recv: 86103.532460412 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No HASH: 6ad28213dba0817acd3db0b6f74eb670
[#CLIENT#] R[333]: Sent: 86103.532469204 Recv: 86103.616942620 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[334]: Sent: 86103.553825204 Recv: 86103.571340870 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 40   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[335]: Sent: 86103.622480495 Recv: 86103.630591704 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 17   ServerImgID: 17   Rejected: No
[#CLIENT#] R[336]: Sent: 86103.661461620 Recv: 86103.668500704 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 27   ServerImgID: 27   Rejected: No
[#CLIENT#] R[337]: Sent: 86103.672125704 Recv: 86103.690749162 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No HASH: cb4a82a72e81817c8d6e7fc99f03d7eb
[#CLIENT#] R[338]: Sent: 86103.690755620 Recv: 86103.745401329 Opcode: IMG_BLUR        OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[339]: Sent: 86103.712277579 Recv: 86103.834501412 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 26   ServerImgID: 26   Rejected: No
[#CLIENT#] R[340]: Sent: 86103.733348662 Recv: 86103.916312620 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 16   ServerImgID: 16   Rejected: No
[#CLIENT#] R[341]: Sent: 86103.816248662 Recv: 86103.834495829 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 41   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[342]: Sent: 86103.871310912 Recv: 86103.889561704 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 42   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[343]: Sent: 86103.911750495 Recv: 86104.000642995 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[344]: Sent: 86103.969259495 Recv: 86103.986897745 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 43   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[345]: Sent: 86103.994452912 Recv: 86104.088609120 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[346]: Sent: 86104.040358204 Recv: 86104.159815370 Opcode: IMG_BLUR        OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[347]: Sent: 86104.142067662 Recv: 86104.159829329 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 44   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[348]: Sent: 86104.178586704 Recv: 86104.265933954 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 22   ServerImgID: 22   Rejected: No
[#CLIENT#] R[349]: Sent: 86104.216616037 Recv: 86104.284952704 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No HASH: 43ca8e4190f0418a76cd3ad359706a20
[#CLIENT#] R[350]: Sent: 86104.376059621 Recv: 86104.432663704 Opcode: IMG_BLUR        OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[351]: Sent: 86104.378819204 Recv: 86104.396314204 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 45   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[352]: Sent: 86104.398350704 Recv: 86104.484942829 Opcode: IMG_BLUR        OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[353]: Sent: 86104.410814996 Recv: 86104.428791746 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 46   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[354]: Sent: 86104.432620621 Recv: 86104.576485912 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No
[#CLIENT#] R[355]: Sent: 86104.463475121 Recv: 86104.667851162 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[356]: Sent: 86104.504934287 Recv: 86104.721872204 Opcode: IMG_BLUR        OW: 1 ClientImgID: 34   ServerImgID: 34   Rejected: No
[#CLIENT#] R[357]: Sent: 86104.560786454 Recv: 86104.815168912 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[358]: Sent: 86104.593054371 Recv: 86104.610615079 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 47   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[359]: Sent: 86104.744202454 Recv: 86104.901896204 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 25   ServerImgID: 25   Rejected: No
[#CLIENT#] R[360]: Sent: 86104.859815704 Recv: 86104.920838413 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No HASH: 17f53b44873a51687c7b7eb59caa78d4
[#CLIENT#] R[361]: Sent: 86104.987025788 Recv: 86105.073553288 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No
[#CLIENT#] R[362]: Sent: 86105.073064329 Recv: 86105.092395621 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No HASH: e86ac01aa209232d9ecce0271f9ce47b
[#CLIENT#] R[363]: Sent: 86105.073352413 Recv: 86105.111485954 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No HASH: 1fb565223d78c2f2e9e5dc6d48609731
[#CLIENT#] R[364]: Sent: 86105.122764288 Recv: 86105.178729413 Opcode: IMG_BLUR        OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No
[#CLIENT#] R[365]: Sent: 86105.124666079 Recv: 86105.234572871 Opcode: IMG_BLUR        OW: 1 ClientImgID: 21   ServerImgID: 21   Rejected: No
[#CLIENT#] R[366]: Sent: 86105.227496746 Recv: 86105.252828079 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No HASH: e86ac01aa209232d9ecce0271f9ce47b
[#CLIENT#] R[367]: Sent: 86105.283763038 Recv: 86105.300921371 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 48   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[368]: Sent: 86105.351691079 Recv: 86105.358752121 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[369]: Sent: 86105.628323288 Recv: 86105.645984996 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 49   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[370]: Sent: 86105.651221538 Recv: 86105.738954121 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No
[#CLIENT#] R[371]: Sent: 86105.668468913 Recv: 86105.745974746 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 23   ServerImgID: 23   Rejected: No
[#CLIENT#] R[372]: Sent: 86105.692449371 Recv: 86105.764921580 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No HASH: d523eac10654580a8082902b4be07d62
[#CLIENT#] R[373]: Sent: 86105.802626288 Recv: 86105.889248996 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 42   ServerImgID: 42   Rejected: No
[#CLIENT#] R[374]: Sent: 86105.812381080 Recv: 86105.978307121 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[375]: Sent: 86105.942180788 Recv: 86106.067240621 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[376]: Sent: 86105.958354705 Recv: 86106.086151455 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 26   ServerImgID: 26   Rejected: No HASH: 9d73e97ac536ed43ec67b869dac562a7
[#CLIENT#] R[377]: Sent: 86106.046584038 Recv: 86106.159433371 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 33   ServerImgID: 33   Rejected: No
[#CLIENT#] R[378]: Sent: 86106.086160288 Recv: 86106.240328371 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[379]: Sent: 86106.117121038 Recv: 86106.134935746 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 50   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[380]: Sent: 86106.159377955 Recv: 86106.296517663 Opcode: IMG_BLUR        OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No
[#CLIENT#] R[381]: Sent: 86106.169837455 Recv: 86106.303231372 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[382]: Sent: 86106.294555497 Recv: 86106.322664122 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No HASH: 2ec8a864904a738fd306d50b3cd3cf7e
[#CLIENT#] R[383]: Sent: 86106.342378247 Recv: 86106.359462330 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 51   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[384]: Sent: 86106.394312580 Recv: 86106.402289538 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 17   ServerImgID: 17   Rejected: No
[#CLIENT#] R[385]: Sent: 86106.446848038 Recv: 86106.465411955 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 33   ServerImgID: 33   Rejected: No HASH: 0ca2b17283ae8bada714cf75628b9380
[#CLIENT#] R[386]: Sent: 86106.483581538 Recv: 86106.537793038 Opcode: IMG_BLUR        OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[387]: Sent: 86106.539858330 Recv: 86106.623674663 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[388]: Sent: 86106.617502913 Recv: 86106.637944288 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 33   ServerImgID: 33   Rejected: No
[#CLIENT#] R[389]: Sent: 86106.637897788 Recv: 86106.730255747 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[390]: Sent: 86106.651907663 Recv: 86106.750328163 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No HASH: 661fe052697a9a56d76b60d5cc8e9cc3
[#CLIENT#] R[391]: Sent: 86106.678982163 Recv: 86106.842091747 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[392]: Sent: 86106.754224622 Recv: 86106.903008622 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[393]: Sent: 86106.762080038 Recv: 86106.957021247 Opcode: IMG_BLUR        OW: 1 ClientImgID: 43   ServerImgID: 43   Rejected: No
[#CLIENT#] R[394]: Sent: 86106.799188913 Recv: 86106.816635705 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 52   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[395]: Sent: 86106.855657497 Recv: 86107.040548872 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[396]: Sent: 86106.869106580 Recv: 86107.095019455 Opcode: IMG_BLUR        OW: 1 ClientImgID: 34   ServerImgID: 34   Rejected: No
[#CLIENT#] R[397]: Sent: 86106.901518413 Recv: 86107.178794872 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 40   ServerImgID: 40   Rejected: No
[#CLIENT#] R[398]: Sent: 86107.043268164 Recv: 86107.262818580 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 40   ServerImgID: 40   Rejected: No
[#CLIENT#] R[399]: Sent: 86107.058789789 Recv: 86107.318809914 Opcode: IMG_BLUR        OW: 1 ClientImgID: 22   ServerImgID: 22   Rejected: No
[#CLIENT#] R[400]: Sent: 86107.088559830 Recv: 86107.372951205 Opcode: IMG_BLUR        OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[401]: Sent: 86107.132742080 Recv: 86107.150876497 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 53   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[402]: Sent: 86107.329337455 Recv: 86107.392443247 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No HASH: 63462aae85d7bb2238584f421e5321b0
[#CLIENT#] R[403]: Sent: 86107.539292705 Recv: 86107.625753664 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 51   ServerImgID: 51   Rejected: No
[#CLIENT#] R[404]: Sent: 86107.575571664 Recv: 86107.593245122 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 54   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[405]: Sent: 86107.660551289 Recv: 86107.748623539 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 49   ServerImgID: 49   Rejected: No
[#CLIENT#] R[406]: Sent: 86107.704471206 Recv: 86107.804868997 Opcode: IMG_BLUR        OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[407]: Sent: 86107.724056956 Recv: 86107.888780414 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 38   ServerImgID: 38   Rejected: No
[#CLIENT#] R[408]: Sent: 86107.801458622 Recv: 86107.895635164 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[409]: Sent: 86107.829359206 Recv: 86107.982203372 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 49   ServerImgID: 49   Rejected: No
[#CLIENT#] R[410]: Sent: 86107.890478581 Recv: 86108.068762914 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 39   ServerImgID: 39   Rejected: No
[#CLIENT#] R[411]: Sent: 86107.890935164 Recv: 86108.075985831 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No
[#CLIENT#] R[412]: Sent: 86107.927969747 Recv: 86108.095407331 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 40   ServerImgID: 40   Rejected: No HASH: ca244572358dc4837fabdc3637bd44b9
[#CLIENT#] R[413]: Sent: 86107.937154081 Recv: 86108.160188706 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 26   ServerImgID: 26   Rejected: No
[#CLIENT#] R[414]: Sent: 86107.977870747 Recv: 86108.246705414 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No
[#CLIENT#] R[415]: Sent: 86107.988651289 Recv: 86108.265773081 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No HASH: 0b00d2004cd908e0aef14f5b9b7574cd
[#CLIENT#] R[416]: Sent: 86108.053645997 Recv: 86108.338844706 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 42   ServerImgID: 42   Rejected: No
[#CLIENT#] R[417]: Sent: 86108.110361831 Recv: 86108.425185373 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 29   ServerImgID: 29   Rejected: No
[#CLIENT#] R[418]: Sent: 86108.174326622 Recv: 86108.192439039 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 55   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[419]: Sent: 86108.244316497 Recv: 86108.459332414 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[420]: Sent: 86108.321099081 Recv: 86108.338836331 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 56   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[421]: Sent: 86108.362839331 Recv: 86108.500034873 Opcode: IMG_BLUR        OW: 1 ClientImgID: 23   ServerImgID: 23   Rejected: No
[#CLIENT#] R[422]: Sent: 86108.459303581 Recv: 86108.544829456 Opcode: IMG_BLUR        OW: 1 ClientImgID: 35   ServerImgID: 35   Rejected: No
[#CLIENT#] R[423]: Sent: 86108.658722248 Recv: 86108.745844706 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[424]: Sent: 86108.777504164 Recv: 86108.794576914 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 57   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[425]: Sent: 86108.803009998 Recv: 86108.820883498 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 58   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[426]: Sent: 86108.836422831 Recv: 86108.924967081 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 52   ServerImgID: 52   Rejected: No
[#CLIENT#] R[427]: Sent: 86108.869065664 Recv: 86108.979290581 Opcode: IMG_BLUR        OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[428]: Sent: 86108.884628623 Recv: 86108.986064289 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 52   ServerImgID: 52   Rejected: No
[#CLIENT#] R[429]: Sent: 86108.927215914 Recv: 86109.070107206 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[430]: Sent: 86108.981673414 Recv: 86109.153902165 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 43   ServerImgID: 43   Rejected: No
[#CLIENT#] R[431]: Sent: 86109.194945165 Recv: 86109.287372748 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[432]: Sent: 86109.201822206 Recv: 86109.306808415 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 36   ServerImgID: 36   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[433]: Sent: 86109.204958290 Recv: 86109.371794873 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[434]: Sent: 86109.278263123 Recv: 86109.390527831 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 36   ServerImgID: 36   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[435]: Sent: 86109.351591915 Recv: 86109.409068373 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No HASH: 8521ee02b69e716c6bf3c7431c777740
[#CLIENT#] R[436]: Sent: 86109.432300540 Recv: 86109.449383873 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 59   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[437]: Sent: 86109.479125248 Recv: 86109.496648331 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 60   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[438]: Sent: 86109.498462331 Recv: 86109.553290248 Opcode: IMG_BLUR        OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No
[#CLIENT#] R[439]: Sent: 86109.519996123 Recv: 86109.594520415 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[440]: Sent: 86109.605147081 Recv: 86109.693674540 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[441]: Sent: 86109.613028873 Recv: 86109.777475790 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[442]: Sent: 86109.633842748 Recv: 86109.796105790 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 33   ServerImgID: 33   Rejected: No HASH: 8424c5f06ec75b6d7be01c9662dba8cc
[#CLIENT#] R[443]: Sent: 86109.763588540 Recv: 86109.865715832 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[444]: Sent: 86109.767121040 Recv: 86109.954140457 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[445]: Sent: 86109.796115707 Recv: 86110.042120123 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 22   ServerImgID: 22   Rejected: No
[#CLIENT#] R[446]: Sent: 86109.905768707 Recv: 86110.049242082 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 25   ServerImgID: 25   Rejected: No
[#CLIENT#] R[447]: Sent: 86109.939233415 Recv: 86110.136325665 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No
[#CLIENT#] R[448]: Sent: 86110.019778540 Recv: 86110.223091957 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No
[#CLIENT#] R[449]: Sent: 86110.059452790 Recv: 86110.243180707 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No HASH: 99904a9a04062db3ec5b5af7eda23f71
[#CLIENT#] R[450]: Sent: 86110.082982790 Recv: 86110.307761248 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 56   ServerImgID: 56   Rejected: No
[#CLIENT#] R[451]: Sent: 86110.086495873 Recv: 86110.104211457 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 61   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[452]: Sent: 86110.104539582 Recv: 86110.364125373 Opcode: IMG_BLUR        OW: 1 ClientImgID: 21   ServerImgID: 21   Rejected: No
[#CLIENT#] R[453]: Sent: 86110.106966623 Recv: 86110.450747165 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No
[#CLIENT#] R[454]: Sent: 86110.116254623 Recv: 86110.457749373 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[455]: Sent: 86110.132795290 Recv: 86110.544506499 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No
[#CLIENT#] R[456]: Sent: 86110.171429623 Recv: 86110.631112415 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 23   ServerImgID: 23   Rejected: No
[#CLIENT#] R[457]: Sent: 86110.182998165 Recv: 86110.719740790 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[458]: Sent: 86110.255432373 Recv: 86110.739565582 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 29   ServerImgID: 29   Rejected: No HASH: d8390c28690c913753725bac84c2eed9
[#CLIENT#] R[459]: Sent: 86110.288273957 Recv: 86110.775105457 Opcode: IMG_BLUR        OW: 1 ClientImgID: 50   ServerImgID: 50   Rejected: No
[#CLIENT#] R[460]: Sent: 86110.419859498 Recv: 86110.861380624 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 55   ServerImgID: 55   Rejected: No
[#CLIENT#] R[461]: Sent: 86110.493116082 Recv: 86110.868069332 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 57   ServerImgID: 57   Rejected: No
[#CLIENT#] R[462]: Sent: 86110.739575374 Recv: 86110.887344332 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No HASH: ec311d772fe3879aa7d51e283c0b90b4
[#CLIENT#] R[463]: Sent: 86110.802871665 Recv: 86110.958373707 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 42   ServerImgID: 42   Rejected: No
[#CLIENT#] R[464]: Sent: 86110.803679624 Recv: 86110.821059499 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 62   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[465]: Sent: 86110.887355124 Recv: 86110.962345957 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 54   ServerImgID: 54   Rejected: No
[#CLIENT#] R[466]: Sent: 86110.911894624 Recv: 86111.018502707 Opcode: IMG_BLUR        OW: 1 ClientImgID: 44   ServerImgID: 44   Rejected: No
[#CLIENT#] R[467]: Sent: 86110.913662124 Recv: 86111.025217207 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 59   ServerImgID: 59   Rejected: No
[#CLIENT#] R[468]: Sent: 86110.915542957 Recv: 86110.933766082 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 63   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[469]: Sent: 86110.961843957 Recv: 86111.082348374 Opcode: IMG_BLUR        OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[470]: Sent: 86111.003286457 Recv: 86111.138709415 Opcode: IMG_BLUR        OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No
[#CLIENT#] R[471]: Sent: 86111.018022290 Recv: 86111.158298707 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 39   ServerImgID: 39   Rejected: No HASH: 78a7633528e7dc2fc020b73ae9ed6596
[#CLIENT#] R[472]: Sent: 86111.070569874 Recv: 86111.230189791 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 44   ServerImgID: 44   Rejected: No
[#CLIENT#] R[473]: Sent: 86111.075285290 Recv: 86111.317193124 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[474]: Sent: 86111.109748915 Recv: 86111.127832832 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 64   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[475]: Sent: 86111.271153541 Recv: 86111.289342082 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 65   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[476]: Sent: 86111.358470124 Recv: 86111.442076957 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 38   ServerImgID: 38   Rejected: No
[#CLIENT#] R[477]: Sent: 86111.440151041 Recv: 86111.533222749 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[478]: Sent: 86111.485616874 Recv: 86111.552045999 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 30   ServerImgID: 30   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[479]: Sent: 86111.616038749 Recv: 86111.633347416 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 66   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[480]: Sent: 86111.654076249 Recv: 86111.660913791 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[481]: Sent: 86111.666109832 Recv: 86111.720582999 Opcode: IMG_BLUR        OW: 1 ClientImgID: 40   ServerImgID: 40   Rejected: No
[#CLIENT#] R[482]: Sent: 86111.713640291 Recv: 86111.807753416 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[483]: Sent: 86111.753181541 Recv: 86111.898767124 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 39   ServerImgID: 39   Rejected: No
[#CLIENT#] R[484]: Sent: 86111.756259082 Recv: 86111.954832291 Opcode: IMG_BLUR        OW: 1 ClientImgID: 65   ServerImgID: 65   Rejected: No
[#CLIENT#] R[485]: Sent: 86111.775638166 Recv: 86111.974936916 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No HASH: dd9a1adf0b75a1a305c8435c9141612e
[#CLIENT#] R[486]: Sent: 86111.823162166 Recv: 86111.974942166 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 49   ServerImgID: 49   Rejected: No
[#CLIENT#] R[487]: Sent: 86111.855302291 Recv: 86112.050720541 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 52   ServerImgID: 52   Rejected: No
[#CLIENT#] R[488]: Sent: 86111.861097624 Recv: 86112.105069666 Opcode: IMG_BLUR        OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[489]: Sent: 86111.877816999 Recv: 86112.193129916 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No
[#CLIENT#] R[490]: Sent: 86111.910489458 Recv: 86112.200100333 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 42   ServerImgID: 42   Rejected: No
[#CLIENT#] R[491]: Sent: 86111.974949416 Recv: 86112.287368374 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 60   ServerImgID: 60   Rejected: No
[#CLIENT#] R[492]: Sent: 86112.008210333 Recv: 86112.373711791 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 21   ServerImgID: 21   Rejected: No
[#CLIENT#] R[493]: Sent: 86112.011043083 Recv: 86112.380845916 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 21   ServerImgID: 21   Rejected: No
[#CLIENT#] R[494]: Sent: 86112.013527999 Recv: 86112.399662333 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No HASH: 4bcea4ed61c74a8bd7fe5cfe3de16077
[#CLIENT#] R[495]: Sent: 86112.046276624 Recv: 86112.469897708 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[496]: Sent: 86112.405503541 Recv: 86112.422909833 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 67   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[497]: Sent: 86112.666595958 Recv: 86112.675160916 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 65   ServerImgID: 65   Rejected: No
[#CLIENT#] R[498]: Sent: 86112.700676833 Recv: 86112.717701708 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 68   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[499]: Sent: 86112.756559708 Recv: 86112.773442333 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 69   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[500]: Sent: 86112.814689916 Recv: 86112.832333666 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 70   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[501]: Sent: 86112.838638125 Recv: 86112.893453958 Opcode: IMG_BLUR        OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[502]: Sent: 86112.870491041 Recv: 86112.930603625 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[503]: Sent: 86112.885876041 Recv: 86112.984619166 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 50   ServerImgID: 50   Rejected: No
[#CLIENT#] R[504]: Sent: 86112.930569333 Recv: 86113.071430625 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[505]: Sent: 86113.077311875 Recv: 86113.097171583 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No HASH: 14128b7071d3593098601c12f695916d
[#CLIENT#] R[506]: Sent: 86113.097178208 Recv: 86113.104979958 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 57   ServerImgID: 57   Rejected: No
[#CLIENT#] R[507]: Sent: 86113.117073000 Recv: 86113.134773875 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 71   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[508]: Sent: 86113.253278166 Recv: 86113.345831875 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 27   ServerImgID: 27   Rejected: No
[#CLIENT#] R[509]: Sent: 86113.300297500 Recv: 86113.352820417 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 36   ServerImgID: 36   Rejected: No
[#CLIENT#] R[510]: Sent: 86113.322812458 Recv: 86113.439412375 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 65   ServerImgID: 65   Rejected: No
[#CLIENT#] R[511]: Sent: 86113.358044125 Recv: 86113.523085750 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 45   ServerImgID: 45   Rejected: No
[#CLIENT#] R[512]: Sent: 86113.372602458 Recv: 86113.529917125 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[513]: Sent: 86113.384725917 Recv: 86113.559688958 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 16   ServerImgID: 16   Rejected: No
[#CLIENT#] R[514]: Sent: 86113.526121500 Recv: 86113.623660250 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 17   ServerImgID: 17   Rejected: No
[#CLIENT#] R[515]: Sent: 86113.559666833 Recv: 86113.707535958 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 28   ServerImgID: 28   Rejected: No
[#CLIENT#] R[516]: Sent: 86113.569555833 Recv: 86113.791492292 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[517]: Sent: 86113.618715792 Recv: 86113.811203417 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No HASH: ec9d0684bccc9509c34c96a563d0333d
[#CLIENT#] R[518]: Sent: 86113.636740875 Recv: 86113.846280417 Opcode: IMG_BLUR        OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[519]: Sent: 86113.655901250 Recv: 86113.930048000 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[520]: Sent: 86113.812806458 Recv: 86113.936631667 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[521]: Sent: 86113.872670333 Recv: 86113.955655500 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No HASH: cd10514ae06344d4dc27c6909446c42f
[#CLIENT#] R[522]: Sent: 86113.881716208 Recv: 86113.955660708 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 69   ServerImgID: 69   Rejected: No
[#CLIENT#] R[523]: Sent: 86113.974602959 Recv: 86113.981368917 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 30   ServerImgID: 30   Rejected: No
[#CLIENT#] R[524]: Sent: 86114.052345667 Recv: 86114.070942917 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 51   ServerImgID: 51   Rejected: No HASH: 392626c80f548779a200c8ec6e46c645
[#CLIENT#] R[525]: Sent: 86114.070953375 Recv: 86114.077926625 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 21   ServerImgID: 21   Rejected: No
[#CLIENT#] R[526]: Sent: 86114.076187834 Recv: 86114.084853000 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No
[#CLIENT#] R[527]: Sent: 86114.220211459 Recv: 86114.237431375 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 72   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[528]: Sent: 86114.280119834 Recv: 86114.369768084 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[529]: Sent: 86114.313205750 Recv: 86114.453593792 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 51   ServerImgID: 51   Rejected: No
[#CLIENT#] R[530]: Sent: 86114.325174292 Recv: 86114.472931459 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 47   ServerImgID: 47   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[531]: Sent: 86114.344637000 Recv: 86114.542532125 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 66   ServerImgID: 66   Rejected: No
[#CLIENT#] R[532]: Sent: 86114.478604167 Recv: 86114.630259834 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 29   ServerImgID: 29   Rejected: No
[#CLIENT#] R[533]: Sent: 86114.514453584 Recv: 86114.716658042 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 53   ServerImgID: 53   Rejected: No
[#CLIENT#] R[534]: Sent: 86114.534248042 Recv: 86114.724661001 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[535]: Sent: 86114.706172126 Recv: 86114.808768209 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 51   ServerImgID: 51   Rejected: No
[#CLIENT#] R[536]: Sent: 86114.730258709 Recv: 86114.892971334 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 72   ServerImgID: 72   Rejected: No
[#CLIENT#] R[537]: Sent: 86114.823349501 Recv: 86114.911867542 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No HASH: 814e704706b0f25a007d0e918fb6e39f
[#CLIENT#] R[538]: Sent: 86114.880954542 Recv: 86114.929967084 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 51   ServerImgID: 51   Rejected: No HASH: 6bd3e9be835105140ff16e2c8860dd70
[#CLIENT#] R[539]: Sent: 86114.963061876 Recv: 86115.077872834 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 58   ServerImgID: 58   Rejected: No
[#CLIENT#] R[540]: Sent: 86115.049152751 Recv: 86115.145439667 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 43   ServerImgID: 43   Rejected: No
[#CLIENT#] R[541]: Sent: 86115.053920376 Recv: 86115.071478126 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 73   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[542]: Sent: 86115.077841709 Recv: 86115.229455334 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[543]: Sent: 86115.086607376 Recv: 86115.104068417 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 74   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[544]: Sent: 86115.131917167 Recv: 86115.236192959 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 66   ServerImgID: 66   Rejected: No
[#CLIENT#] R[545]: Sent: 86115.231307251 Recv: 86115.324449417 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 40   ServerImgID: 40   Rejected: No
[#CLIENT#] R[546]: Sent: 86115.385553293 Recv: 86115.472192209 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No
[#CLIENT#] R[547]: Sent: 86115.491861043 Recv: 86115.576009793 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 43   ServerImgID: 43   Rejected: No
[#CLIENT#] R[548]: Sent: 86115.507470918 Recv: 86115.667398876 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 55   ServerImgID: 55   Rejected: No
[#CLIENT#] R[549]: Sent: 86115.534530251 Recv: 86115.751851584 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[550]: Sent: 86115.586791834 Recv: 86115.770019168 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No HASH: 2534f3b4744ebd76878f4b516855f50e
[#CLIENT#] R[551]: Sent: 86115.710850959 Recv: 86115.728769543 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 75   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[552]: Sent: 86115.854739459 Recv: 86115.861762418 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 73   ServerImgID: 73   Rejected: No
[#CLIENT#] R[553]: Sent: 86115.941330793 Recv: 86115.948048959 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 72   ServerImgID: 72   Rejected: No
[#CLIENT#] R[554]: Sent: 86115.973147043 Recv: 86116.095090793 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 47   ServerImgID: 47   Rejected: No
[#CLIENT#] R[555]: Sent: 86116.025731834 Recv: 86116.147714543 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 63   ServerImgID: 63   Rejected: No
[#CLIENT#] R[556]: Sent: 86116.052155376 Recv: 86116.070481085 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 76   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[557]: Sent: 86116.164670168 Recv: 86116.183509460 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No HASH: 3381183e364a1cb420b6d168cb53a234
[#CLIENT#] R[558]: Sent: 86116.284067043 Recv: 86116.370700001 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[559]: Sent: 86116.293103835 Recv: 86116.427403043 Opcode: IMG_BLUR        OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No
[#CLIENT#] R[560]: Sent: 86116.298468876 Recv: 86116.512042835 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 43   ServerImgID: 43   Rejected: No
[#CLIENT#] R[561]: Sent: 86116.432184168 Recv: 86116.595816168 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 34   ServerImgID: 34   Rejected: No
[#CLIENT#] R[562]: Sent: 86116.617450668 Recv: 86116.701237376 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 34   ServerImgID: 34   Rejected: No
[#CLIENT#] R[563]: Sent: 86116.626576376 Recv: 86116.813078043 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[564]: Sent: 86116.627300918 Recv: 86116.841793418 Opcode: IMG_BLUR        OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No
[#CLIENT#] R[565]: Sent: 86116.720908835 Recv: 86116.848747377 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 44   ServerImgID: 44   Rejected: No
[#CLIENT#] R[566]: Sent: 86116.770712960 Recv: 86116.788464835 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 77   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[567]: Sent: 86116.857501877 Recv: 86116.941767043 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 57   ServerImgID: 57   Rejected: No
[#CLIENT#] R[568]: Sent: 86116.859832168 Recv: 86116.961590002 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No HASH: 983c7662a9de41557a81193721437286
[#CLIENT#] R[569]: Sent: 86116.871234377 Recv: 86116.998391710 Opcode: IMG_BLUR        OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[570]: Sent: 86116.872812043 Recv: 86117.017462960 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No HASH: 6e06616a7fe9cf88e02360cc2080e794
[#CLIENT#] R[571]: Sent: 86116.894163502 Recv: 86117.053120043 Opcode: IMG_BLUR        OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[572]: Sent: 86116.908165793 Recv: 86117.139823002 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 60   ServerImgID: 60   Rejected: No
[#CLIENT#] R[573]: Sent: 86117.999807252 Recv: 86118.006537502 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 43   ServerImgID: 43   Rejected: No
[#CLIENT#] R[574]: Sent: 86118.017401877 Recv: 86118.106793169 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[575]: Sent: 86118.019365252 Recv: 86118.037705294 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 78   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[576]: Sent: 86118.171142002 Recv: 86118.179152377 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[577]: Sent: 86118.302529627 Recv: 86118.320304211 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 79   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[578]: Sent: 86118.440525794 Recv: 86118.457742086 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 80   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[579]: Sent: 86118.465528836 Recv: 86118.484931877 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 71   ServerImgID: 71   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[580]: Sent: 86118.484938752 Recv: 86118.493789461 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 52   ServerImgID: 52   Rejected: No
[#CLIENT#] R[581]: Sent: 86118.500804002 Recv: 86118.508759086 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[582]: Sent: 86118.566050127 Recv: 86118.584276377 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 26   ServerImgID: 26   Rejected: No HASH: 55348f8ec458faee8aef206c3daa6f14
[#CLIENT#] R[583]: Sent: 86118.586842336 Recv: 86118.675734794 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[584]: Sent: 86118.718172669 Recv: 86118.736981586 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No HASH: b52bf2575572cfd08cd9725b1ec1a230
[#CLIENT#] R[585]: Sent: 86118.882563586 Recv: 86118.974321961 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[586]: Sent: 86118.887606419 Recv: 86118.981848294 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No
[#CLIENT#] R[587]: Sent: 86118.954083003 Recv: 86119.068603294 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 64   ServerImgID: 64   Rejected: No
[#CLIENT#] R[588]: Sent: 86119.019753544 Recv: 86119.155153211 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 55   ServerImgID: 55   Rejected: No
[#CLIENT#] R[589]: Sent: 86119.250878961 Recv: 86119.335090128 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 54   ServerImgID: 54   Rejected: No
[#CLIENT#] R[590]: Sent: 86119.307532044 Recv: 86119.418864086 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 66   ServerImgID: 66   Rejected: No
[#CLIENT#] R[591]: Sent: 86119.420276294 Recv: 86119.427242544 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[592]: Sent: 86119.462892753 Recv: 86119.482577419 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 79   ServerImgID: 79   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[593]: Sent: 86119.521051503 Recv: 86119.538015128 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 81   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[594]: Sent: 86119.563857045 Recv: 86119.651507503 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No
[#CLIENT#] R[595]: Sent: 86119.630438378 Recv: 86119.747312086 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 51   ServerImgID: 51   Rejected: No
[#CLIENT#] R[596]: Sent: 86119.668216711 Recv: 86119.819260128 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 77   ServerImgID: 77   Rejected: No
[#CLIENT#] R[597]: Sent: 86119.695198586 Recv: 86119.907332253 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 61   ServerImgID: 61   Rejected: No
[#CLIENT#] R[598]: Sent: 86119.703018336 Recv: 86119.721203961 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 82   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[599]: Sent: 86119.792198586 Recv: 86119.927091836 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 75   ServerImgID: 75   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[600]: Sent: 86119.823198711 Recv: 86119.965714170 Opcode: IMG_BLUR        OW: 1 ClientImgID: 76   ServerImgID: 76   Rejected: No
[#CLIENT#] R[601]: Sent: 86119.840031503 Recv: 86120.054379961 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No
[#CLIENT#] R[602]: Sent: 86119.883020086 Recv: 86120.073777670 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 74   ServerImgID: 74   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[603]: Sent: 86119.927103336 Recv: 86120.138539836 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 28   ServerImgID: 28   Rejected: No
[#CLIENT#] R[604]: Sent: 86119.934273086 Recv: 86120.184026795 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 51   ServerImgID: 51   Rejected: No
[#CLIENT#] R[605]: Sent: 86119.972432420 Recv: 86120.184030295 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[606]: Sent: 86120.073788545 Recv: 86120.184039920 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 63   ServerImgID: 63   Rejected: No
[#CLIENT#] R[607]: Sent: 86120.199484211 Recv: 86120.304490753 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[608]: Sent: 86120.271332628 Recv: 86120.289531628 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 83   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[609]: Sent: 86120.304449420 Recv: 86120.322955462 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No HASH: b52bf2575572cfd08cd9725b1ec1a230
[#CLIENT#] R[610]: Sent: 86120.344480003 Recv: 86120.428504503 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 34   ServerImgID: 34   Rejected: No
[#CLIENT#] R[611]: Sent: 86120.402839628 Recv: 86120.447062087 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 70   ServerImgID: 70   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[612]: Sent: 86120.546687295 Recv: 86120.564948962 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No HASH: 8c796a5f4a2648665d69fa146854ae67
[#CLIENT#] R[613]: Sent: 86120.564955795 Recv: 86120.582530337 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 84   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[614]: Sent: 86120.602594253 Recv: 86120.610774128 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 66   ServerImgID: 66   Rejected: No
[#CLIENT#] R[615]: Sent: 86120.668011628 Recv: 86120.756729295 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[616]: Sent: 86120.679469753 Recv: 86120.844051920 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 75   ServerImgID: 75   Rejected: No
[#CLIENT#] R[617]: Sent: 86120.774242462 Recv: 86120.924912712 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 45   ServerImgID: 45   Rejected: No
[#CLIENT#] R[618]: Sent: 86120.799924962 Recv: 86120.817561795 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 85   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[619]: Sent: 86120.862152545 Recv: 86120.932089878 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[620]: Sent: 86120.888226295 Recv: 86121.020976004 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[621]: Sent: 86120.925651378 Recv: 86121.028912462 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 43   ServerImgID: 43   Rejected: No
[#CLIENT#] R[622]: Sent: 86121.019719504 Recv: 86121.083430795 Opcode: IMG_BLUR        OW: 1 ClientImgID: 81   ServerImgID: 81   Rejected: No
[#CLIENT#] R[623]: Sent: 86121.161530379 Recv: 86121.248473295 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 84   ServerImgID: 84   Rejected: No
[#CLIENT#] R[624]: Sent: 86121.195763920 Recv: 86121.332226545 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 68   ServerImgID: 68   Rejected: No
[#CLIENT#] R[625]: Sent: 86121.318082754 Recv: 86121.421056045 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No
[#CLIENT#] R[626]: Sent: 86121.451708712 Recv: 86121.459902462 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[627]: Sent: 86121.455798754 Recv: 86121.556492170 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 52   ServerImgID: 52   Rejected: No
[#CLIENT#] R[628]: Sent: 86121.529582462 Recv: 86121.547961295 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 86   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[629]: Sent: 86121.556434379 Recv: 86121.612816254 Opcode: IMG_BLUR        OW: 1 ClientImgID: 55   ServerImgID: 55   Rejected: No
[#CLIENT#] R[630]: Sent: 86121.779130129 Recv: 86121.797419629 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 68   ServerImgID: 68   Rejected: No HASH: d4f94469bfe2b5ed7246046002f99653
[#CLIENT#] R[631]: Sent: 86121.845036046 Recv: 86121.931794462 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No
[#CLIENT#] R[632]: Sent: 86121.900816129 Recv: 86121.988055754 Opcode: IMG_BLUR        OW: 1 ClientImgID: 64   ServerImgID: 64   Rejected: No
[#CLIENT#] R[633]: Sent: 86121.925110837 Recv: 86122.079219754 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 83   ServerImgID: 83   Rejected: No
[#CLIENT#] R[634]: Sent: 86121.954930837 Recv: 86122.097590379 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No HASH: a23a719827efff3d96392acc4f93cb9d
[#CLIENT#] R[635]: Sent: 86122.269381254 Recv: 86122.360830046 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No
[#CLIENT#] R[636]: Sent: 86122.311164671 Recv: 86122.368775129 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No
[#CLIENT#] R[637]: Sent: 86122.488318088 Recv: 86122.496244296 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[638]: Sent: 86122.495455296 Recv: 86122.583009046 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 49   ServerImgID: 49   Rejected: No
[#CLIENT#] R[639]: Sent: 86122.579108671 Recv: 86122.667078463 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 13   ServerImgID: 13   Rejected: No
[#CLIENT#] R[640]: Sent: 86122.594758338 Recv: 86122.686979213 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No HASH: 91a35f676711c245714ac7c99eac2772
[#CLIENT#] R[641]: Sent: 86122.597422629 Recv: 86122.755930171 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 70   ServerImgID: 70   Rejected: No
[#CLIENT#] R[642]: Sent: 86122.692253171 Recv: 86122.862084254 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 21   ServerImgID: 21   Rejected: No
[#CLIENT#] R[643]: Sent: 86122.739039504 Recv: 86122.938025963 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 84   ServerImgID: 84   Rejected: No
[#CLIENT#] R[644]: Sent: 86122.762042838 Recv: 86123.025039838 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[645]: Sent: 86122.793199463 Recv: 86123.032037713 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 23   ServerImgID: 23   Rejected: No
[#CLIENT#] R[646]: Sent: 86122.841827379 Recv: 86122.859603254 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 87   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[647]: Sent: 86122.862051921 Recv: 86123.115966921 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 40   ServerImgID: 40   Rejected: No
[#CLIENT#] R[648]: Sent: 86122.906766588 Recv: 86122.924057129 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 88   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[649]: Sent: 86122.976914129 Recv: 86122.995118671 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 89   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[650]: Sent: 86123.081673380 Recv: 86123.202376880 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[651]: Sent: 86123.117178546 Recv: 86123.288277963 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 76   ServerImgID: 76   Rejected: No
[#CLIENT#] R[652]: Sent: 86123.130545130 Recv: 86123.372039796 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 74   ServerImgID: 74   Rejected: No
[#CLIENT#] R[653]: Sent: 86123.225066380 Recv: 86123.428142046 Opcode: IMG_BLUR        OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[654]: Sent: 86123.242514296 Recv: 86123.446865255 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 26   ServerImgID: 26   Rejected: No HASH: 55348f8ec458faee8aef206c3daa6f14
[#CLIENT#] R[655]: Sent: 86123.245883880 Recv: 86123.512394171 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No
[#CLIENT#] R[656]: Sent: 86123.249755630 Recv: 86123.267901671 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 90   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[657]: Sent: 86123.282510421 Recv: 86123.627825255 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 47   ServerImgID: 47   Rejected: No
[#CLIENT#] R[658]: Sent: 86123.339552421 Recv: 86123.357204546 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 91   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[659]: Sent: 86123.363924546 Recv: 86123.655535505 Opcode: IMG_BLUR        OW: 1 ClientImgID: 43   ServerImgID: 43   Rejected: No
[#CLIENT#] R[660]: Sent: 86123.446877213 Recv: 86123.746296922 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No
[#CLIENT#] R[661]: Sent: 86123.484532171 Recv: 86123.753075255 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No
[#CLIENT#] R[662]: Sent: 86123.496091088 Recv: 86123.773102880 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 79   ServerImgID: 79   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[663]: Sent: 86123.526016255 Recv: 86123.837044088 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[664]: Sent: 86123.577890505 Recv: 86123.596301338 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 92   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[665]: Sent: 86123.610089630 Recv: 86123.627829755 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 93   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[666]: Sent: 86123.641205046 Recv: 86123.921452422 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[667]: Sent: 86123.651977213 Recv: 86123.978753255 Opcode: IMG_BLUR        OW: 1 ClientImgID: 92   ServerImgID: 92   Rejected: No
[#CLIENT#] R[668]: Sent: 86123.656505380 Recv: 86124.019028255 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 92   ServerImgID: 92   Rejected: No
[#CLIENT#] R[669]: Sent: 86123.658941630 Recv: 86124.071209005 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[670]: Sent: 86123.773111672 Recv: 86124.157926713 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 42   ServerImgID: 42   Rejected: No
[#CLIENT#] R[671]: Sent: 86123.877964630 Recv: 86124.249771130 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[672]: Sent: 86123.881408213 Recv: 86124.305920755 Opcode: IMG_BLUR        OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[673]: Sent: 86123.899567380 Recv: 86124.325962380 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 78   ServerImgID: 78   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[674]: Sent: 86123.910710547 Recv: 86124.344740838 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 50   ServerImgID: 50   Rejected: No HASH: 9d73e97ac536ed43ec67b869dac562a7
[#CLIENT#] R[675]: Sent: 86123.917125505 Recv: 86124.398873922 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[676]: Sent: 86123.954794755 Recv: 86123.972339838 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 94   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[677]: Sent: 86123.974824047 Recv: 86124.489859172 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No
[#CLIENT#] R[678]: Sent: 86124.039645713 Recv: 86124.544232339 Opcode: IMG_BLUR        OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[679]: Sent: 86124.047949672 Recv: 86124.632784797 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 70   ServerImgID: 70   Rejected: No
[#CLIENT#] R[680]: Sent: 86124.244373422 Recv: 86124.651548964 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 51   ServerImgID: 51   Rejected: No HASH: 185510b52e413cb63ecddc84b37f1ea9
[#CLIENT#] R[681]: Sent: 86124.246054880 Recv: 86124.651554255 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 75   ServerImgID: 75   Rejected: No
[#CLIENT#] R[682]: Sent: 86124.344753588 Recv: 86124.362865005 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 95   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[683]: Sent: 86124.404567422 Recv: 86124.723867505 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 72   ServerImgID: 72   Rejected: No
[#CLIENT#] R[684]: Sent: 86124.411572172 Recv: 86124.743622380 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 16   ServerImgID: 16   Rejected: No HASH: dbadfc20b3c75e0856a235f9764943c6
[#CLIENT#] R[685]: Sent: 86124.492925047 Recv: 86124.804493380 Opcode: IMG_BLUR        OW: 1 ClientImgID: 94   ServerImgID: 94   Rejected: No
[#CLIENT#] R[686]: Sent: 86124.545471089 Recv: 86124.866353964 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 77   ServerImgID: 77   Rejected: No
[#CLIENT#] R[687]: Sent: 86124.613675255 Recv: 86124.631531839 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 96   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[688]: Sent: 86124.652237005 Recv: 86124.953197422 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[689]: Sent: 86124.658352255 Recv: 86124.961144714 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 9    ServerImgID: 9    Rejected: No
[#CLIENT#] R[690]: Sent: 86124.669347130 Recv: 86125.047912089 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 89   ServerImgID: 89   Rejected: No
[#CLIENT#] R[691]: Sent: 86124.689591339 Recv: 86125.118114047 Opcode: IMG_BLUR        OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[692]: Sent: 86124.692165589 Recv: 86125.193760506 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 84   ServerImgID: 84   Rejected: No
[#CLIENT#] R[693]: Sent: 86124.743630047 Recv: 86125.213809714 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 84   ServerImgID: 84   Rejected: No HASH: 2326e8a964742d53375a7edba55f44a4
[#CLIENT#] R[694]: Sent: 86124.761349797 Recv: 86124.778948547 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 97   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[695]: Sent: 86124.907675297 Recv: 86125.250308297 Opcode: IMG_BLUR        OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[696]: Sent: 86124.963775047 Recv: 86125.337162589 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 76   ServerImgID: 76   Rejected: No
[#CLIENT#] R[697]: Sent: 86125.040292214 Recv: 86125.393488172 Opcode: IMG_BLUR        OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[698]: Sent: 86125.069712005 Recv: 86125.087309839 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 98   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[699]: Sent: 86125.155260881 Recv: 86125.172793756 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 99   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[700]: Sent: 86125.237643964 Recv: 86125.480516631 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 39   ServerImgID: 39   Rejected: No
[#CLIENT#] R[701]: Sent: 86125.254307797 Recv: 86125.564319047 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 75   ServerImgID: 75   Rejected: No
[#CLIENT#] R[702]: Sent: 86125.271392839 Recv: 86125.571064256 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 26   ServerImgID: 26   Rejected: No
[#CLIENT#] R[703]: Sent: 86125.354659381 Recv: 86125.372211672 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 100  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[704]: Sent: 86125.380487047 Recv: 86125.659734047 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 75   ServerImgID: 75   Rejected: No
[#CLIENT#] R[705]: Sent: 86125.416526006 Recv: 86125.701028839 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 40   ServerImgID: 40   Rejected: No
[#CLIENT#] R[706]: Sent: 86125.417180339 Recv: 86125.752103214 Opcode: IMG_BLUR        OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No
[#CLIENT#] R[707]: Sent: 86125.427070839 Recv: 86125.807152089 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 75   ServerImgID: 75   Rejected: No
[#CLIENT#] R[708]: Sent: 86125.430298589 Recv: 86125.447821006 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 101  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[709]: Sent: 86125.472317547 Recv: 86125.826778297 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 35   ServerImgID: 35   Rejected: No HASH: 63462aae85d7bb2238584f421e5321b0
[#CLIENT#] R[710]: Sent: 86125.490743047 Recv: 86125.508424589 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 102  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[711]: Sent: 86125.589565006 Recv: 86125.891338506 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 54   ServerImgID: 54   Rejected: No
[#CLIENT#] R[712]: Sent: 86125.707478131 Recv: 86125.726120922 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 103  Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[713]: Sent: 86125.754351714 Recv: 86125.975965631 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[714]: Sent: 86125.900823756 Recv: 86125.919124714 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 104  Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[715]: Sent: 86125.962612214 Recv: 86126.059860006 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[716]: Sent: 86125.970061048 Recv: 86126.150735464 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 104  ServerImgID: 104  Rejected: No
[#CLIENT#] R[717]: Sent: 86125.985651131 Recv: 86126.201219714 Opcode: IMG_BLUR        OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[718]: Sent: 86126.048301631 Recv: 86126.292095131 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No
[#CLIENT#] R[719]: Sent: 86126.133158298 Recv: 86126.150729798 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 105  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[720]: Sent: 86126.209247589 Recv: 86126.378413006 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 25   ServerImgID: 25   Rejected: No
[#CLIENT#] R[721]: Sent: 86126.247024714 Recv: 86126.397485256 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 73   ServerImgID: 73   Rejected: No HASH: a46fa185b469892706544a2d486bf142
[#CLIENT#] R[722]: Sent: 86126.302580714 Recv: 86126.320789964 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 106  Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[723]: Sent: 86126.329591631 Recv: 86126.397499423 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 74   ServerImgID: 74   Rejected: No
[#CLIENT#] R[724]: Sent: 86126.370410464 Recv: 86126.416876131 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 60   ServerImgID: 60   Rejected: No HASH: cb8a2ae1d35da5dc317ed9a391166950
[#CLIENT#] R[725]: Sent: 86126.397504381 Recv: 86126.488551631 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No
[#CLIENT#] R[726]: Sent: 86126.504228089 Recv: 86126.523170339 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 91   ServerImgID: 91   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[727]: Sent: 86126.530445214 Recv: 86126.618820881 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 69   ServerImgID: 69   Rejected: No
[#CLIENT#] R[728]: Sent: 86126.566950381 Recv: 86126.702584465 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 80   ServerImgID: 80   Rejected: No
[#CLIENT#] R[729]: Sent: 86126.620400006 Recv: 86126.789332673 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 36   ServerImgID: 36   Rejected: No
[#CLIENT#] R[730]: Sent: 86126.662253298 Recv: 86126.872992423 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 47   ServerImgID: 47   Rejected: No
[#CLIENT#] R[731]: Sent: 86126.847165840 Recv: 86126.959367840 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 25   ServerImgID: 25   Rejected: No
[#CLIENT#] R[732]: Sent: 86126.856215506 Recv: 86127.043428090 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 72   ServerImgID: 72   Rejected: No
[#CLIENT#] R[733]: Sent: 86126.883826673 Recv: 86127.134614798 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 103  ServerImgID: 103  Rejected: No
[#CLIENT#] R[734]: Sent: 86126.925366840 Recv: 86127.226161006 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[735]: Sent: 86126.992226631 Recv: 86127.010523673 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 107  Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[736]: Sent: 86127.041028840 Recv: 86127.233138590 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[737]: Sent: 86127.107402673 Recv: 86127.324820757 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[738]: Sent: 86127.176758965 Recv: 86127.344131007 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 34   ServerImgID: 34   Rejected: No HASH: eac0a1248f802d95bd7859a30061c076
[#CLIENT#] R[739]: Sent: 86127.218434465 Recv: 86127.363443882 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 92   ServerImgID: 92   Rejected: No HASH: 87504e6eb7330f31ab17020c33a18aa9
[#CLIENT#] R[740]: Sent: 86127.260347590 Recv: 86127.412246757 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 27   ServerImgID: 27   Rejected: No
[#CLIENT#] R[741]: Sent: 86127.263674048 Recv: 86127.281991173 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 108  Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[742]: Sent: 86127.379298840 Recv: 86127.420193548 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No
[#CLIENT#] R[743]: Sent: 86127.475165507 Recv: 86127.531730548 Opcode: IMG_BLUR        OW: 1 ClientImgID: 25   ServerImgID: 25   Rejected: No
[#CLIENT#] R[744]: Sent: 86127.508111382 Recv: 86127.618396548 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 89   ServerImgID: 89   Rejected: No
[#CLIENT#] R[745]: Sent: 86127.567024090 Recv: 86127.636328215 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No
[#CLIENT#] R[746]: Sent: 86127.570304090 Recv: 86127.636331715 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 84   ServerImgID: 84   Rejected: No
[#CLIENT#] R[747]: Sent: 86127.636311007 Recv: 86127.690569632 Opcode: IMG_BLUR        OW: 1 ClientImgID: 102  ServerImgID: 102  Rejected: No
[#CLIENT#] R[748]: Sent: 86127.810541132 Recv: 86127.817723298 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 93   ServerImgID: 93   Rejected: No
[#CLIENT#] R[749]: Sent: 86127.843909132 Recv: 86127.898180715 Opcode: IMG_BLUR        OW: 1 ClientImgID: 69   ServerImgID: 69   Rejected: No
[#CLIENT#] R[750]: Sent: 86127.849288882 Recv: 86127.954340924 Opcode: IMG_BLUR        OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No
[#CLIENT#] R[751]: Sent: 86127.884301090 Recv: 86128.038342965 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[752]: Sent: 86127.896894298 Recv: 86128.124987090 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 107  ServerImgID: 107  Rejected: No
[#CLIENT#] R[753]: Sent: 86128.028902007 Recv: 86128.211380507 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 82   ServerImgID: 82   Rejected: No
[#CLIENT#] R[754]: Sent: 86128.105559465 Recv: 86128.252032340 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 93   ServerImgID: 93   Rejected: No
[#CLIENT#] R[755]: Sent: 86128.126814632 Recv: 86128.301594507 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 72   ServerImgID: 72   Rejected: No
[#CLIENT#] R[756]: Sent: 86128.200473257 Recv: 86128.387742382 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No
[#CLIENT#] R[757]: Sent: 86128.340999174 Recv: 86128.407543049 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 69   ServerImgID: 69   Rejected: No HASH: 73dd4cb71b2b004ba550beb16f37f768
[#CLIENT#] R[758]: Sent: 86128.356162132 Recv: 86128.474910132 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 89   ServerImgID: 89   Rejected: No
[#CLIENT#] R[759]: Sent: 86128.370703757 Recv: 86128.493733340 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 75   ServerImgID: 75   Rejected: No HASH: b81d6db32f3a769c3e48f3673f2a40ae
[#CLIENT#] R[760]: Sent: 86128.412884340 Recv: 86128.493738924 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No
[#CLIENT#] R[761]: Sent: 86128.493745299 Recv: 86128.511282590 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 109  Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[762]: Sent: 86128.609491090 Recv: 86128.628783007 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 29   ServerImgID: 29   Rejected: No HASH: 980a8402e6523177fe0562036332e0bd
[#CLIENT#] R[763]: Sent: 86128.788421507 Recv: 86128.873671632 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 40   ServerImgID: 40   Rejected: No
[#CLIENT#] R[764]: Sent: 86128.827447091 Recv: 86128.962149757 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[765]: Sent: 86128.834546341 Recv: 86129.048616424 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 23   ServerImgID: 23   Rejected: No
[#CLIENT#] R[766]: Sent: 86128.867356924 Recv: 86129.132427424 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 56   ServerImgID: 56   Rejected: No
[#CLIENT#] R[767]: Sent: 86128.869679174 Recv: 86129.186665382 Opcode: IMG_BLUR        OW: 1 ClientImgID: 94   ServerImgID: 94   Rejected: No
[#CLIENT#] R[768]: Sent: 86128.910570007 Recv: 86129.207073757 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 22   ServerImgID: 22   Rejected: No HASH: fc6f8555846f74d78dec631af3f63e49
[#CLIENT#] R[769]: Sent: 86128.984387507 Recv: 86129.207087341 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 78   ServerImgID: 78   Rejected: No
[#CLIENT#] R[770]: Sent: 86128.998746841 Recv: 86129.207126257 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[771]: Sent: 86129.039740424 Recv: 86129.289279424 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 107  ServerImgID: 107  Rejected: No
[#CLIENT#] R[772]: Sent: 86129.112193632 Recv: 86129.377565591 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[773]: Sent: 86129.176565049 Recv: 86129.396345341 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 67   ServerImgID: 67   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[774]: Sent: 86129.207095132 Recv: 86129.415104466 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 59   ServerImgID: 59   Rejected: No HASH: a46fa185b469892706544a2d486bf142
[#CLIENT#] R[775]: Sent: 86129.348896341 Recv: 86129.464526133 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[776]: Sent: 86129.372379091 Recv: 86129.483171716 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 74   ServerImgID: 74   Rejected: No HASH: 3b3e20aa776ada5ed79da1b1242d54fd
[#CLIENT#] R[777]: Sent: 86129.425017466 Recv: 86129.502651383 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 16   ServerImgID: 16   Rejected: No HASH: dbadfc20b3c75e0856a235f9764943c6
[#CLIENT#] R[778]: Sent: 86129.460040299 Recv: 86129.555954133 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[779]: Sent: 86129.575647008 Recv: 86129.662225924 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 93   ServerImgID: 93   Rejected: No
[#CLIENT#] R[780]: Sent: 86129.595751133 Recv: 86129.749268924 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 7    ServerImgID: 7    Rejected: No
[#CLIENT#] R[781]: Sent: 86129.707945674 Recv: 86129.835818091 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[782]: Sent: 86129.712917924 Recv: 86129.924828924 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[783]: Sent: 86129.721279508 Recv: 86129.944377133 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 50   ServerImgID: 50   Rejected: No HASH: 9d73e97ac536ed43ec67b869dac562a7
[#CLIENT#] R[784]: Sent: 86129.721328258 Recv: 86129.739263966 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 110  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[785]: Sent: 86129.766390966 Recv: 86129.979722341 Opcode: IMG_BLUR        OW: 1 ClientImgID: 45   ServerImgID: 45   Rejected: No
[#CLIENT#] R[786]: Sent: 86129.836896383 Recv: 86129.998955716 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 97   ServerImgID: 97   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[787]: Sent: 86129.912772424 Recv: 86130.071179299 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No
[#CLIENT#] R[788]: Sent: 86129.944384341 Recv: 86130.154963632 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 101  ServerImgID: 101  Rejected: No
[#CLIENT#] R[789]: Sent: 86130.130772799 Recv: 86130.241495382 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 53   ServerImgID: 53   Rejected: No
[#CLIENT#] R[790]: Sent: 86130.184666007 Recv: 86130.260458966 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 43   ServerImgID: 43   Rejected: No HASH: efcb94c606c54a9c1900acc4f61d60d2
[#CLIENT#] R[791]: Sent: 86130.187452132 Recv: 86130.260465049 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 23   ServerImgID: 23   Rejected: No
[#CLIENT#] R[792]: Sent: 86130.327424174 Recv: 86130.383682924 Opcode: IMG_BLUR        OW: 1 ClientImgID: 27   ServerImgID: 27   Rejected: No
[#CLIENT#] R[793]: Sent: 86130.337110507 Recv: 86130.402476716 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No HASH: ce0554cad54a8bdac1186811c81ebf37
[#CLIENT#] R[794]: Sent: 86130.403500716 Recv: 86130.487568882 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 81   ServerImgID: 81   Rejected: No
[#CLIENT#] R[795]: Sent: 86130.412190716 Recv: 86130.542050216 Opcode: IMG_BLUR        OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[796]: Sent: 86130.455444382 Recv: 86130.628478466 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 39   ServerImgID: 39   Rejected: No
[#CLIENT#] R[797]: Sent: 86130.487811966 Recv: 86130.682323841 Opcode: IMG_BLUR        OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[798]: Sent: 86130.601025424 Recv: 86130.618746549 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 111  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[799]: Sent: 86130.643935007 Recv: 86130.769531383 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 35   ServerImgID: 35   Rejected: No
[#CLIENT#] R[800]: Sent: 86130.712873674 Recv: 86130.856500508 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[801]: Sent: 86130.724301799 Recv: 86130.940201966 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 98   ServerImgID: 98   Rejected: No
[#CLIENT#] R[802]: Sent: 86130.743188258 Recv: 86131.026999424 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 16   ServerImgID: 16   Rejected: No
[#CLIENT#] R[803]: Sent: 86130.838947466 Recv: 86131.116030633 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 6    ServerImgID: 6    Rejected: No
[#CLIENT#] R[804]: Sent: 86130.877844758 Recv: 86131.151270258 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 81   ServerImgID: 81   Rejected: No
[#CLIENT#] R[805]: Sent: 86130.932679674 Recv: 86131.206748049 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 74   ServerImgID: 74   Rejected: No
[#CLIENT#] R[806]: Sent: 86130.942043758 Recv: 86131.293759758 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[807]: Sent: 86130.969998799 Recv: 86131.313374924 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 72   ServerImgID: 72   Rejected: No HASH: 60ea7ced6c2564b47808ed9c0f294ac5
[#CLIENT#] R[808]: Sent: 86130.974742341 Recv: 86131.332833674 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 23   ServerImgID: 23   Rejected: No HASH: 86df0a1d09855216236b9e223f5fb0a0
[#CLIENT#] R[809]: Sent: 86131.028570633 Recv: 86131.378326633 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 68   ServerImgID: 68   Rejected: No
[#CLIENT#] R[810]: Sent: 86131.030459633 Recv: 86131.470095091 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 2    ServerImgID: 2    Rejected: No
[#CLIENT#] R[811]: Sent: 86131.070716883 Recv: 86131.477186508 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 63   ServerImgID: 63   Rejected: No
[#CLIENT#] R[812]: Sent: 86131.076100799 Recv: 86131.568183258 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 93   ServerImgID: 93   Rejected: No
[#CLIENT#] R[813]: Sent: 86131.151248883 Recv: 86131.652174800 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 33   ServerImgID: 33   Rejected: No
[#CLIENT#] R[814]: Sent: 86131.217365841 Recv: 86131.672218466 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 42   ServerImgID: 42   Rejected: No HASH: 5051735868d16f5af5b401a0ebe4d0d8
[#CLIENT#] R[815]: Sent: 86131.392475050 Recv: 86131.410518591 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 112  Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[816]: Sent: 86131.528840883 Recv: 86131.547008508 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 113  Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[817]: Sent: 86131.564659716 Recv: 86131.736714633 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 81   ServerImgID: 81   Rejected: No
[#CLIENT#] R[818]: Sent: 86131.694750675 Recv: 86131.743702800 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 106  ServerImgID: 106  Rejected: No
[#CLIENT#] R[819]: Sent: 86131.707426591 Recv: 86131.763233425 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 79   ServerImgID: 79   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[820]: Sent: 86131.716565758 Recv: 86131.827875133 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No
[#CLIENT#] R[821]: Sent: 86131.743404216 Recv: 86131.915053508 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[822]: Sent: 86131.763240300 Recv: 86131.921662758 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[823]: Sent: 86131.894313425 Recv: 86131.929682883 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 22   ServerImgID: 22   Rejected: No
[#CLIENT#] R[824]: Sent: 86131.912582425 Recv: 86131.936669341 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 27   ServerImgID: 27   Rejected: No
[#CLIENT#] R[825]: Sent: 86132.023937425 Recv: 86132.115403258 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No
[#CLIENT#] R[826]: Sent: 86132.117298258 Recv: 86132.208298092 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 55   ServerImgID: 55   Rejected: No
[#CLIENT#] R[827]: Sent: 86132.185491217 Recv: 86132.264504133 Opcode: IMG_BLUR        OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[828]: Sent: 86132.188887508 Recv: 86132.349018717 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 97   ServerImgID: 97   Rejected: No
[#CLIENT#] R[829]: Sent: 86132.249784800 Recv: 86132.440507300 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No
[#CLIENT#] R[830]: Sent: 86132.252747175 Recv: 86132.531413758 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 76   ServerImgID: 76   Rejected: No
[#CLIENT#] R[831]: Sent: 86132.355497467 Recv: 86132.619389675 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[832]: Sent: 86132.377052758 Recv: 86132.661026592 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[833]: Sent: 86132.458694008 Recv: 86132.683514342 Opcode: IMG_BLUR        OW: 1 ClientImgID: 58   ServerImgID: 58   Rejected: No
[#CLIENT#] R[834]: Sent: 86132.463377092 Recv: 86132.481429758 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 114  Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[835]: Sent: 86132.549394633 Recv: 86132.739537758 Opcode: IMG_BLUR        OW: 1 ClientImgID: 16   ServerImgID: 16   Rejected: No
[#CLIENT#] R[836]: Sent: 86132.577821592 Recv: 86132.826283092 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No
[#CLIENT#] R[837]: Sent: 86132.597812883 Recv: 86132.913029300 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 35   ServerImgID: 35   Rejected: No
[#CLIENT#] R[838]: Sent: 86132.695908425 Recv: 86133.003818467 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 49   ServerImgID: 49   Rejected: No
[#CLIENT#] R[839]: Sent: 86132.701951758 Recv: 86133.091121217 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 108  ServerImgID: 108  Rejected: No
[#CLIENT#] R[840]: Sent: 86132.771329258 Recv: 86133.147175092 Opcode: IMG_BLUR        OW: 1 ClientImgID: 93   ServerImgID: 93   Rejected: No
[#CLIENT#] R[841]: Sent: 86132.853534925 Recv: 86133.236119717 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 19   ServerImgID: 19   Rejected: No
[#CLIENT#] R[842]: Sent: 86132.943765759 Recv: 86133.322461467 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 36   ServerImgID: 36   Rejected: No
[#CLIENT#] R[843]: Sent: 86133.082711634 Recv: 86133.330617592 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[844]: Sent: 86133.193802634 Recv: 86133.417428509 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 84   ServerImgID: 84   Rejected: No
[#CLIENT#] R[845]: Sent: 86133.221913300 Recv: 86133.504261634 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 65   ServerImgID: 65   Rejected: No
[#CLIENT#] R[846]: Sent: 86133.258874800 Recv: 86133.590678676 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 36   ServerImgID: 36   Rejected: No
[#CLIENT#] R[847]: Sent: 86133.262827634 Recv: 86133.599634926 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 28   ServerImgID: 28   Rejected: No
[#CLIENT#] R[848]: Sent: 86133.287317259 Recv: 86133.618669926 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No HASH: 5ea20db3d31a80938c95b21f08e1d40b
[#CLIENT#] R[849]: Sent: 86133.311471717 Recv: 86133.683724717 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 50   ServerImgID: 50   Rejected: No
[#CLIENT#] R[850]: Sent: 86133.328384717 Recv: 86133.772910384 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 77   ServerImgID: 77   Rejected: No
[#CLIENT#] R[851]: Sent: 86133.343796342 Recv: 86133.857015426 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 1    ServerImgID: 1    Rejected: No
[#CLIENT#] R[852]: Sent: 86133.409783550 Recv: 86133.949362134 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 39   ServerImgID: 39   Rejected: No
[#CLIENT#] R[853]: Sent: 86133.472109967 Recv: 86133.968503509 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No HASH: 1edeef86f82e9d5dbdf7360914f1aa0a
[#CLIENT#] R[854]: Sent: 86133.479178426 Recv: 86134.038215801 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 72   ServerImgID: 72   Rejected: No
[#CLIENT#] R[855]: Sent: 86133.496673426 Recv: 86134.127077634 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 28   ServerImgID: 28   Rejected: No
[#CLIENT#] R[856]: Sent: 86133.501700634 Recv: 86134.146413801 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 39   ServerImgID: 39   Rejected: No HASH: c4b894947203484cc55370f4244fe3cd
[#CLIENT#] R[857]: Sent: 86133.525485009 Recv: 86134.164925467 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 56   ServerImgID: 56   Rejected: No HASH: 69f5b8f4c5543d57ea4584e5e2950152
[#CLIENT#] R[858]: Sent: 86133.634418801 Recv: 86133.652843509 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 115  Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[859]: Sent: 86133.710931051 Recv: 86134.219175426 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 63   ServerImgID: 63   Rejected: No
[#CLIENT#] R[860]: Sent: 86133.743903884 Recv: 86134.273932634 Opcode: IMG_BLUR        OW: 1 ClientImgID: 85   ServerImgID: 85   Rejected: No
[#CLIENT#] R[861]: Sent: 86133.763982134 Recv: 86134.360911551 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 12   ServerImgID: 12   Rejected: No
[#CLIENT#] R[862]: Sent: 86133.769426426 Recv: 86134.379609134 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 75   ServerImgID: 75   Rejected: No HASH: b81d6db32f3a769c3e48f3673f2a40ae
[#CLIENT#] R[863]: Sent: 86133.777440967 Recv: 86134.464147926 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 88   ServerImgID: 88   Rejected: No
[#CLIENT#] R[864]: Sent: 86133.793288759 Recv: 86134.532007426 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 60   ServerImgID: 60   Rejected: No
[#CLIENT#] R[865]: Sent: 86133.834575717 Recv: 86134.623845384 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[866]: Sent: 86133.906593801 Recv: 86134.710998218 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 108  ServerImgID: 108  Rejected: No
[#CLIENT#] R[867]: Sent: 86133.925007051 Recv: 86133.942706926 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 116  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[868]: Sent: 86133.979906342 Recv: 86134.765110301 Opcode: IMG_BLUR        OW: 1 ClientImgID: 102  ServerImgID: 102  Rejected: No
[#CLIENT#] R[869]: Sent: 86133.995969759 Recv: 86134.848694343 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 45   ServerImgID: 45   Rejected: No
[#CLIENT#] R[870]: Sent: 86134.051293092 Recv: 86134.069488301 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 117  Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[871]: Sent: 86134.100275801 Recv: 86134.932971843 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[872]: Sent: 86134.164933051 Recv: 86135.020264926 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No
[#CLIENT#] R[873]: Sent: 86134.197940218 Recv: 86135.107118385 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 109  ServerImgID: 109  Rejected: No
[#CLIENT#] R[874]: Sent: 86134.231497718 Recv: 86134.249266093 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 118  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[875]: Sent: 86134.271675759 Recv: 86135.114221135 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 49   ServerImgID: 49   Rejected: No
[#CLIENT#] R[876]: Sent: 86134.309596884 Recv: 86135.133769718 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 52   ServerImgID: 52   Rejected: No HASH: 1ffca4140001fa3f6f50080787eb82af
[#CLIENT#] R[877]: Sent: 86134.346312884 Recv: 86135.168841801 Opcode: IMG_BLUR        OW: 1 ClientImgID: 74   ServerImgID: 74   Rejected: No
[#CLIENT#] R[878]: Sent: 86134.379619968 Recv: 86135.209029885 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 27   ServerImgID: 27   Rejected: No
[#CLIENT#] R[879]: Sent: 86134.421540093 Recv: 86134.438963926 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 119  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[880]: Sent: 86134.464173093 Recv: 86135.259764468 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 111  ServerImgID: 111  Rejected: No
[#CLIENT#] R[881]: Sent: 86134.473855259 Recv: 86134.491289301 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 120  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[882]: Sent: 86134.500678634 Recv: 86135.314097176 Opcode: IMG_BLUR        OW: 1 ClientImgID: 74   ServerImgID: 74   Rejected: No
[#CLIENT#] R[883]: Sent: 86134.506801384 Recv: 86135.411574135 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 79   ServerImgID: 79   Rejected: No
[#CLIENT#] R[884]: Sent: 86134.570168301 Recv: 86135.488981051 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 94   ServerImgID: 94   Rejected: No
[#CLIENT#] R[885]: Sent: 86134.576245718 Recv: 86135.508361301 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 50   ServerImgID: 50   Rejected: No HASH: 55348f8ec458faee8aef206c3daa6f14
[#CLIENT#] R[886]: Sent: 86134.621664634 Recv: 86135.588557760 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 41   ServerImgID: 41   Rejected: No
[#CLIENT#] R[887]: Sent: 86134.636808968 Recv: 86134.654429759 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 121  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[888]: Sent: 86134.687642426 Recv: 86135.660316802 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 50   ServerImgID: 50   Rejected: No
[#CLIENT#] R[889]: Sent: 86134.696202968 Recv: 86135.714697968 Opcode: IMG_BLUR        OW: 1 ClientImgID: 61   ServerImgID: 61   Rejected: No
[#CLIENT#] R[890]: Sent: 86134.858265968 Recv: 86135.722872468 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 26   ServerImgID: 26   Rejected: No
[#CLIENT#] R[891]: Sent: 86134.882333635 Recv: 86135.731233052 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 40   ServerImgID: 40   Rejected: No
[#CLIENT#] R[892]: Sent: 86134.951459843 Recv: 86135.816172802 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 3    ServerImgID: 3    Rejected: No
[#CLIENT#] R[893]: Sent: 86134.960469051 Recv: 86135.870519802 Opcode: IMG_BLUR        OW: 1 ClientImgID: 96   ServerImgID: 96   Rejected: No
[#CLIENT#] R[894]: Sent: 86135.035229926 Recv: 86135.890043635 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 35   ServerImgID: 35   Rejected: No HASH: 9d06f87e49e80fbf587457d81dd0aaf8
[#CLIENT#] R[895]: Sent: 86135.133779426 Recv: 86135.954886177 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[896]: Sent: 86135.295607593 Recv: 86136.038791802 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 34   ServerImgID: 34   Rejected: No
[#CLIENT#] R[897]: Sent: 86135.393700010 Recv: 86135.411566260 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 122  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[898]: Sent: 86135.508824010 Recv: 86136.131631802 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[899]: Sent: 86135.541481510 Recv: 86135.558937760 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 123  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[900]: Sent: 86135.957075552 Recv: 86136.220370927 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[901]: Sent: 86135.961701677 Recv: 86136.239337385 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 59   ServerImgID: 59   Rejected: No HASH: a46fa185b469892706544a2d486bf142
[#CLIENT#] R[902]: Sent: 86135.973080260 Recv: 86135.990734427 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 124  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[903]: Sent: 86136.070800135 Recv: 86136.276990802 Opcode: IMG_BLUR        OW: 1 ClientImgID: 46   ServerImgID: 46   Rejected: No
[#CLIENT#] R[904]: Sent: 86136.092830302 Recv: 86136.363850594 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 55   ServerImgID: 55   Rejected: No
[#CLIENT#] R[905]: Sent: 86136.115539677 Recv: 86136.418316719 Opcode: IMG_BLUR        OW: 1 ClientImgID: 33   ServerImgID: 33   Rejected: No
[#CLIENT#] R[906]: Sent: 86136.125889302 Recv: 86136.438418260 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 58   ServerImgID: 58   Rejected: No HASH: 5c96632b13472f279fafe1aed5158180
[#CLIENT#] R[907]: Sent: 86136.147645802 Recv: 86136.457046760 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 91   ServerImgID: 91   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[908]: Sent: 86136.171775468 Recv: 86136.503425094 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No
[#CLIENT#] R[909]: Sent: 86136.239346968 Recv: 86136.522726802 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 53   ServerImgID: 53   Rejected: No HASH: cb8a2ae1d35da5dc317ed9a391166950
[#CLIENT#] R[910]: Sent: 86136.322490802 Recv: 86136.590389010 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 42   ServerImgID: 42   Rejected: No
[#CLIENT#] R[911]: Sent: 86136.331918219 Recv: 86136.609890635 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 27   ServerImgID: 27   Rejected: No HASH: c1dbf5a37071cc55e3eebc58e1fc016d
[#CLIENT#] R[912]: Sent: 86136.471170177 Recv: 86136.609901969 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 11   ServerImgID: 11   Rejected: No
[#CLIENT#] R[913]: Sent: 86136.487748177 Recv: 86136.681642344 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 18   ServerImgID: 18   Rejected: No
[#CLIENT#] R[914]: Sent: 86136.522732969 Recv: 86136.540257927 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 125  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[915]: Sent: 86136.611552469 Recv: 86136.722034844 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 20   ServerImgID: 20   Rejected: No
[#CLIENT#] R[916]: Sent: 86136.676417510 Recv: 86136.794434885 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[917]: Sent: 86136.760325760 Recv: 86136.777897427 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 126  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[918]: Sent: 86136.794354677 Recv: 86136.881054135 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No
[#CLIENT#] R[919]: Sent: 86136.841995510 Recv: 86136.900535135 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No HASH: 0e55cc785d26615d4ba224db90aa2ec5
[#CLIENT#] R[920]: Sent: 86137.015842344 Recv: 86137.023911886 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 51   ServerImgID: 51   Rejected: No
[#CLIENT#] R[921]: Sent: 86137.034253219 Recv: 86137.125445844 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 71   ServerImgID: 71   Rejected: No
[#CLIENT#] R[922]: Sent: 86137.034813302 Recv: 86137.209172636 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 81   ServerImgID: 81   Rejected: No
[#CLIENT#] R[923]: Sent: 86137.122636136 Recv: 86137.292935219 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 126  ServerImgID: 126  Rejected: No
[#CLIENT#] R[924]: Sent: 86137.250096302 Recv: 86137.349288552 Opcode: IMG_BLUR        OW: 1 ClientImgID: 58   ServerImgID: 58   Rejected: No
[#CLIENT#] R[925]: Sent: 86137.253745969 Recv: 86137.403437594 Opcode: IMG_BLUR        OW: 1 ClientImgID: 77   ServerImgID: 77   Rejected: No
[#CLIENT#] R[926]: Sent: 86137.260458344 Recv: 86137.490231136 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 23   ServerImgID: 23   Rejected: No
[#CLIENT#] R[927]: Sent: 86137.263018677 Recv: 86137.574209802 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 101  ServerImgID: 101  Rejected: No
[#CLIENT#] R[928]: Sent: 86137.323123719 Recv: 86137.628121886 Opcode: IMG_BLUR        OW: 1 ClientImgID: 57   ServerImgID: 57   Rejected: No
[#CLIENT#] R[929]: Sent: 86137.459293136 Recv: 86137.648414927 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 31   ServerImgID: 31   Rejected: No HASH: 3fea5a34426ab24ebd51da923b420aef
[#CLIENT#] R[930]: Sent: 86137.472582552 Recv: 86137.720261511 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[931]: Sent: 86137.517773719 Recv: 86137.727128136 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No
[#CLIENT#] R[932]: Sent: 86137.523494802 Recv: 86137.813940094 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 32   ServerImgID: 32   Rejected: No
[#CLIENT#] R[933]: Sent: 86137.707693636 Recv: 86137.821384928 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[934]: Sent: 86137.967975386 Recv: 86137.986920803 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 15   ServerImgID: 15   Rejected: No HASH: 1d476bca63f5fe2f3ff9c9b20f6826dd
[#CLIENT#] R[935]: Sent: 86138.004979428 Recv: 86138.011908803 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 51   ServerImgID: 51   Rejected: No
[#CLIENT#] R[936]: Sent: 86138.133809886 Recv: 86138.153370678 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 37   ServerImgID: 37   Rejected: No HASH: 9a2938e4f0d7513d21fe58144e3560d3
[#CLIENT#] R[937]: Sent: 86138.158156219 Recv: 86138.176404511 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 26   ServerImgID: 26   Rejected: No HASH: 2cc529524a171427ba242fcf8a09b6ff
[#CLIENT#] R[938]: Sent: 86138.176410428 Recv: 86138.194688178 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No HASH: 8f1dcaeb48bf816050821f18e2b297a4
[#CLIENT#] R[939]: Sent: 86138.307025136 Recv: 86138.416791261 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 116  ServerImgID: 116  Rejected: No
[#CLIENT#] R[940]: Sent: 86138.310627053 Recv: 86138.482606386 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 5    ServerImgID: 5    Rejected: No
[#CLIENT#] R[941]: Sent: 86138.344839136 Recv: 86138.566560095 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 54   ServerImgID: 54   Rejected: No
[#CLIENT#] R[942]: Sent: 86138.368568345 Recv: 86138.386748553 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 127  Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[943]: Sent: 86138.439790178 Recv: 86138.657472303 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 53   ServerImgID: 53   Rejected: No
[#CLIENT#] R[944]: Sent: 86138.486344761 Recv: 86138.741415095 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 66   ServerImgID: 66   Rejected: No
[#CLIENT#] R[945]: Sent: 86138.526218970 Recv: 86138.829766178 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[946]: Sent: 86138.540255178 Recv: 86138.836744886 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 107  ServerImgID: 107  Rejected: No
[#CLIENT#] R[947]: Sent: 86138.567292511 Recv: 86138.920824636 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 118  ServerImgID: 118  Rejected: No
[#CLIENT#] R[948]: Sent: 86138.673976803 Recv: 86138.940317636 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 38   ServerImgID: 38   Rejected: No HASH: b8104132493de7040858ff7f6ba4b1e0
[#CLIENT#] R[949]: Sent: 86138.798679011 Recv: 86139.008285011 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 114  ServerImgID: 114  Rejected: No
[#CLIENT#] R[950]: Sent: 86138.806176886 Recv: 86139.092323720 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 122  ServerImgID: 122  Rejected: No
[#CLIENT#] R[951]: Sent: 86138.842289803 Recv: 86139.112132637 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 114  ServerImgID: 114  Rejected: No HASH: 54ef7553d21733e88e2e512be41c798f
[#CLIENT#] R[952]: Sent: 86138.863983095 Recv: 86139.180918220 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 38   ServerImgID: 38   Rejected: No
[#CLIENT#] R[953]: Sent: 86138.918166970 Recv: 86139.222028637 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 88   ServerImgID: 88   Rejected: No
[#CLIENT#] R[954]: Sent: 86138.940327886 Recv: 86139.274728803 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 92   ServerImgID: 92   Rejected: No
[#CLIENT#] R[955]: Sent: 86138.945783636 Recv: 86139.361579720 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 82   ServerImgID: 82   Rejected: No
[#CLIENT#] R[956]: Sent: 86138.958569220 Recv: 86139.448275428 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 8    ServerImgID: 8    Rejected: No
[#CLIENT#] R[957]: Sent: 86139.030979636 Recv: 86139.048744803 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 128  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[958]: Sent: 86139.122207512 Recv: 86139.550700637 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 67   ServerImgID: 67   Rejected: No
[#CLIENT#] R[959]: Sent: 86139.262459803 Recv: 86139.550706595 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 38   ServerImgID: 38   Rejected: No
[#CLIENT#] R[960]: Sent: 86139.274153720 Recv: 86139.600787262 Opcode: IMG_BLUR        OW: 1 ClientImgID: 10   ServerImgID: 10   Rejected: No
[#CLIENT#] R[961]: Sent: 86139.356834345 Recv: 86139.684479053 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 47   ServerImgID: 47   Rejected: No
[#CLIENT#] R[962]: Sent: 86139.377312928 Recv: 86139.768338137 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 24   ServerImgID: 24   Rejected: No
[#CLIENT#] R[963]: Sent: 86139.491200262 Recv: 86139.852295679 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 91   ServerImgID: 91   Rejected: No
[#CLIENT#] R[964]: Sent: 86139.522836262 Recv: 86139.906484470 Opcode: IMG_BLUR        OW: 1 ClientImgID: 77   ServerImgID: 77   Rejected: No
[#CLIENT#] R[965]: Sent: 86139.525092970 Recv: 86139.913606762 Opcode: IMG_ROT90CLKW   OW: 1 ClientImgID: 49   ServerImgID: 49   Rejected: No
[#CLIENT#] R[966]: Sent: 86139.532939512 Recv: 86139.550695637 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 129  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[967]: Sent: 86139.610299553 Recv: 86139.932979220 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 128  ServerImgID: 128  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[968]: Sent: 86139.614716095 Recv: 86139.951617720 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 87   ServerImgID: 87   Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[969]: Sent: 86139.656293095 Recv: 86139.673831637 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 130  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[970]: Sent: 86139.677219595 Recv: 86139.998544179 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 62   ServerImgID: 62   Rejected: No
[#CLIENT#] R[971]: Sent: 86139.730624928 Recv: 86140.052891762 Opcode: IMG_BLUR        OW: 1 ClientImgID: 43   ServerImgID: 43   Rejected: No
[#CLIENT#] R[972]: Sent: 86139.819481679 Recv: 86140.140967345 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 85   ServerImgID: 85   Rejected: No
[#CLIENT#] R[973]: Sent: 86139.991190179 Recv: 86140.160765179 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 86   ServerImgID: 86   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[974]: Sent: 86140.054980595 Recv: 86140.242480012 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 48   ServerImgID: 48   Rejected: No
[#CLIENT#] R[975]: Sent: 86140.114384470 Recv: 86140.132605304 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 131  Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[976]: Sent: 86140.161615054 Recv: 86140.308903179 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 33   ServerImgID: 33   Rejected: No
[#CLIENT#] R[977]: Sent: 86140.172828387 Recv: 86140.363121929 Opcode: IMG_BLUR        OW: 1 ClientImgID: 120  ServerImgID: 120  Rejected: No
[#CLIENT#] R[978]: Sent: 86140.197805554 Recv: 86140.214884179 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 132  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[979]: Sent: 86140.329745095 Recv: 86140.382215554 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 88   ServerImgID: 88   Rejected: No HASH: 3b3e20aa776ada5ed79da1b1242d54fd
[#CLIENT#] R[980]: Sent: 86140.382222137 Recv: 86140.466314679 Opcode: IMG_HORIZEDGES  OW: 1 ClientImgID: 0    ServerImgID: 0    Rejected: No
[#CLIENT#] R[981]: Sent: 86140.450515470 Recv: 86140.550435554 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 72   ServerImgID: 72   Rejected: No
[#CLIENT#] R[982]: Sent: 86140.517149096 Recv: 86140.604287804 Opcode: IMG_BLUR        OW: 1 ClientImgID: 101  ServerImgID: 101  Rejected: No
[#CLIENT#] R[983]: Sent: 86140.681969512 Recv: 86140.699777679 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 133  Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[984]: Sent: 86140.704317679 Recv: 86140.723340721 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 79   ServerImgID: 79   Rejected: No HASH: 1978a21da2d4933f3be508d60938f8e3
[#CLIENT#] R[985]: Sent: 86140.728157179 Recv: 86140.812678054 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 80   ServerImgID: 80   Rejected: No
[#CLIENT#] R[986]: Sent: 86140.870327554 Recv: 86140.959495762 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 14   ServerImgID: 14   Rejected: No
[#CLIENT#] R[987]: Sent: 86140.870389512 Recv: 86140.978709429 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 53   ServerImgID: 53   Rejected: No HASH: 1f1c8796819b3be90020a1649fbceb45
[#CLIENT#] R[988]: Sent: 86140.889760387 Recv: 86140.907373846 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 134  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[989]: Sent: 86140.978719554 Recv: 86141.034629262 Opcode: IMG_BLUR        OW: 1 ClientImgID: 63   ServerImgID: 63   Rejected: No
[#CLIENT#] R[990]: Sent: 86141.230921929 Recv: 86141.317844304 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 89   ServerImgID: 89   Rejected: No
[#CLIENT#] R[991]: Sent: 86141.264975721 Recv: 86141.337298721 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 90   ServerImgID: 90   Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[992]: Sent: 86141.461562221 Recv: 86141.478677679 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 135  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[993]: Sent: 86141.556679721 Recv: 86141.614336179 Opcode: IMG_BLUR        OW: 1 ClientImgID: 84   ServerImgID: 84   Rejected: No
[#CLIENT#] R[994]: Sent: 86141.642295596 Recv: 86141.726282388 Opcode: IMG_VERTEDGES   OW: 1 ClientImgID: 124  ServerImgID: 124  Rejected: No
[#CLIENT#] R[995]: Sent: 86141.680889888 Recv: 86141.745388054 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 72   ServerImgID: 72   Rejected: No HASH: 5ea1fa06c4cda67fa5c705c720733694
[#CLIENT#] R[996]: Sent: 86141.900401180 Recv: 86141.989136096 Opcode: IMG_SHARPEN     OW: 1 ClientImgID: 85   ServerImgID: 85   Rejected: No
[#CLIENT#] R[997]: Sent: 86141.919312555 Recv: 86142.045319680 Opcode: IMG_BLUR        OW: 1 ClientImgID: 4    ServerImgID: 4    Rejected: No
[#CLIENT#] R[998]: Sent: 86141.931399096 Recv: 86142.064238180 Opcode: IMG_RETRIEVE    OW: 1 ClientImgID: 102  ServerImgID: 102  Rejected: No HASH: b160da825890007a3f9202bc65b7ddb3
[#CLIENT#] R[999]: Sent: 86142.005199471 Recv: 86142.022899096 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 0    ServerImgID: 136  Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
"""

run2 = """[#CLIENT#] R[0]: Sent: 86390.208108543 Recv: 86390.226206209 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 1    ServerImgID: 0    Rejected: No HASH: b6770726558da9722136ce84f12bfac8
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


# Input client report, retutrn the dictionary with key as IMGOPT, values as request report associated with it
def group_output_by_imgop(client_report):

    outputs_by_imgop = {}
    client_lines = client_report.strip().split('\n')

    for line in client_lines:

        opt = line.split("Opcode: ")[1].split(' ')[0]

        if opt != "IMG_RETRIEVE":

            if opt not in outputs_by_imgop.keys():
                outputs_by_imgop[opt] = [line]
            else:
                outputs_by_imgop[opt] += [line]

    return outputs_by_imgop


# Code below is for calculating individual response times
pattern = re.compile(r"Sent: (\d+\.\d+) Recv: (\d+\.\d+)")

matches_SJN = pattern.findall(
    "\n".join(group_output_by_imgop(run1)['IMG_HORIZEDGES']))

resp_times_SJN = [float(recv) - float(sent) for sent, recv in matches_SJN]

# matches_FIFO = pattern.findall(FIFO_40)

# resp_times_FIFO = [float(recv) - float(sent) for sent, recv in matches_FIFO]

print(resp_times_SJN)
