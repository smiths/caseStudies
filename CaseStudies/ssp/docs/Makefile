# Makefile
.PHONY:	SRS

all:	SRS MG MIS PS SVnVP UVnVP VnVR

SRS:
	cd SRS && make && cd ..

MG:
	cd Design/MG && make && cd ../..

MIS:
	cd Design/MIS && make && cd ../..

PS:
	cd ProblemStatement && make && cd ..

SVnVP:
	cd VnVPlan/SystVnVPlan && make && cd ../..

UVnVP:
	cd VnVPlan/UnitVnVPlan && make && cd ../..

VnVR:
	cd VnVReport && make && cd ..


clean:	cleanSRS cleanMG cleanMIS cleanPS cleanSVnVP cleanUVnVP cleanVnVR

cleanPS:
	cd ProblemStatement && make clean && cd ..

cleanSRS:
	cd SRS && make clean && cd ..

cleanMG:
	cd Design/MG && make clean && cd ..

cleanMIS:
	cd Design/MIS && make clean && cd ..

cleanSVnVP:
	cd VnVPlan/SystVnVPlan && make clean && cd ..

cleanUVnVP:
	cd VnVPlan/UnitVnVPlan && make clean && cd ..

cleanSVnVR:
	cd VnVReport && make clean && cd ..
