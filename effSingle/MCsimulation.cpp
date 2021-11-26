#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <stdio.h>
#include <stdlib.h>

#include <string>
#include <vector>
#include <TAxis.h>
#include <TCanvas.h>
#include <TF1.h>
#include <TFitResult.h>
#include <TH1D.h>
#include <TLatex.h>
#include <TMatrixDSym.h>
#include <TRandom3.h>
#include <TStyle.h>

using namespace std;


double mu_distribution(double x) {

return pow(cos(x), 3)*sin(x);

}

//Try & Catch method
double rand_TAC(double xMin, double xMax, double yMin,double yMax,
Random3* rand) {

double x = 0. , y = 0.;

do {
x = rand->Uniform(xMin,xMax);
y = rand->Uniform(yMin,yMax);
} while( y > mu_distribution(x) );

return x;

}

double GetY_xfixed(double x0, double y0, double x, double theta, double
phi) {

return y0 + (x - x0) * tan(phi);

}

double GetZ_xfixed(double x0, double z0, double x, double theta, double
phi) {

return z0 + (x - x0) / (tan(theta) * cos(phi));


}

double GetX_yfixed(double x0, double y0, double y, double theta, double
phi) {

return x0 + (y - y0) / tan(phi);

}

double GetZ_yfixed(double y0, double z0, double y, double theta, double
phi) {

return z0 + (y - y0) / (tan(theta) * sin(phi));

}

double GetX_zfixed(double x0, double z0, double z, double theta, double
phi) {

return x0 + (z - z0) * tan(theta) * cos(phi);

}

double GetY_zfixed(double y0, double z0, double z, double theta, double
phi) {

return y0 + (z - z0) * tan(theta) * sin(phi);

}

//MC estimation of geometrical efficiency
double MC(double L, double l, double h1, double h2, double h3, double
d1, double d2, int N_MC, int M, int NBin, int Layout, string dir,
string suffix) {

double ymin_A, ymax_A;
double ymin_B, ymax_B;

double theta; //zenith
double phi; //azimutal

double x1, y1, z1;

double x2_up, y2_up;
double z2_up = h3 + d2 + h2;

double x2_down, y2_down;
double z2_down = h3 + d2;


double x3_up, y3_up;
double z3_up = h3;

double x3_down ,y3_down;
double z3_down = 0.;

double x3_right_yfixed, x3_left_yfixed, z3_right_yfixed,
z3_left_yfixed;
double y3_xfixed, z3_xfixed;

bool sc2_A_up, sc2_A_down;
bool sc2_B_up, sc2_B_down;
bool sc3;
bool sc3_up, sc3_down;
bool sc3_xfixed, sc3_right_yfixed, sc3_left_xfixed;

int Nd_true, Nd_wa, Nd_false;

double eff_geom; //geometrical efficiency
double eff_geom_min = 1.;
double eff_geom_max = 0.;

switch (Layout) {

case 1:

ymin_A = 0.;
ymax_A = l;
ymin_B = l;
ymax_B = L;
break;

case 2:

ymin_A = l;
ymax_A = 2*l;
ymin_B = 0;
ymax_B = l;
break;

case 3:

ymin_A = 2*l;
ymax_A = L;
ymin_B = 0;
ymax_B = 2*l;
break;


default:

cout << "Unknown layout. MC simulation will be interrupted"
<< endl;
return -1;
}

TRandom3 * R = new TRandom3(time(NULL));

TCanvas* canva = new TCanvas();
TH1D * histo = new TH1D("Statistical box", "", NBin, 0., 0.);
TF1 * gauss_distrib;

for (int j = 0; j < N_MC; j++) {

//print status
if (j == N_MC/10)
cout << "MC generation status: 10%" << endl;
if (j == N_MC*2/10)
cout << "MC generation status: 20%" << endl;
if (j == N_MC*3/10)
cout << "MC generation status: 30%" << endl;
if (j == N_MC*4/10)
cout << "MC generation status: 40%" << endl;
if (j == N_MC*5/10)
cout << "MC generation status: 50%" << endl;
if (j == N_MC*6/10)
cout << "MC generation status: 60%" << endl;
if (j == N_MC*7/10)
cout << "MC generation status: 70%" << endl;
if (j == N_MC*8/10)
cout << "MC generation status: 80%" << endl;
if (j == N_MC*9/10)
cout << "MC generation status: 90%" << endl;
if (j == N_MC-1)
cout << "MC generation status: 100%" << endl << endl;

Nd_true = 0;
Nd_wa = 0;
Nd_false = 0;

for (int i = 0; i < M; i++) {

//Generate an incoming muon on the upper scintillator
x1 = R -> Uniform(0., L);
y1 = R -> Uniform(ymin_A, ymin_A+l);
z1 = R -> Uniform(h3 + d2 + h2 + d1, h3 + d2 + h2 + d1 + h1);

theta = rand_TAC(0., M_PI/2, 0., 1., R);
phi = R -> Uniform(0., 2 * M_PI);

//middle scintillator coords
x2_up = GetX_zfixed(x1, z1, z2_up, theta, phi);
y2_up = GetY_zfixed(y1, z1, z2_up, theta, phi);
x2_down = GetX_zfixed(x1, z1, z2_down, theta, phi);
y2_down = GetY_zfixed(y1, z1, z2_down, theta, phi);

//lower scintillator coords
x3_up = GetX_zfixed(x1, z1, z3_up, theta, phi);
y3_up = GetY_zfixed(y1, z1, z3_up, theta, phi);
x3_down = GetX_zfixed(x1, z1, z3_down, theta, phi);
y3_down = GetY_zfixed(y1, z1, z3_down, theta, phi);
x3_right_yfixed = GetX_yfixed(x1, y1, L, theta, phi);
z3_right_yfixed = GetZ_yfixed(y1, z1, L, theta, phi);
x3_left_yfixed = GetX_yfixed(x1, y1, 0., theta, phi);
z3_left_yfixed = GetZ_yfixed(y1, z1, 0., theta, phi);
y3_xfixed = GetY_xfixed(x1, y1, l, theta, phi);
z3_xfixed = GetZ_xfixed(x1, z1, l, theta, phi);

sc2_A_up = (x2_up >= 0.) && (x2_up <= l) && (y2_up >= ymin_A)
&& (y2_up <= ymax_A);
sc2_A_down = (x2_down >= 0.) && (x2_down <= l) && (y2_down >=
ymin_A) && (y2_down <= ymax_A);
sc2_B_up = (x2_up >= 0.) && (x2_up <= l) && (y2_up > ymin_B)
&& (y2_up <= ymax_B);
sc2_B_down = (x2_down >= 0.) && (x2_down <= l) && (y2_down >
ymin_B) && (y2_down <= ymax_B);
if (Layout == 2) {
sc2_B_up = sc2_B_up || ( (x2_up >= 0.) && (x2_up <= l) &&
(y2_up > 2*l) && (y2_up <= L) );
sc2_B_down = sc2_B_down || ( (x2_down >= 0.) && (x2_down
<= l) && (y2_down > 2*l) && (y2_down <= L) );
}
sc3_up = (x3_up >= 0.) && (x3_up <= l) && (y3_up >= 0.) &&
(y3_up <= L);
221 sc3_down = (x3_down >= 0.) && (x3_down <= l) && (y3_down >=
0.) && (y3_down <= L);
222 sc3_xfixed = (y3_xfixed >= 0.) && (y3_xfixed <= L) &&
(z3_xfixed >= z3_down) && (z3_xfixed <= z3_up);
223 sc3_right_yfixed = (x3_right_yfixed >= 0.) &&
(x3_right_yfixed <= l) && (z3_right_yfixed >= z3_down) &&
(z3_right_yfixed <= z3_up);
224 sc3_left_xfixed = (x3_left_yfixed >= 0.) && (x3_left_yfixed
<= l) && (z3_left_yfixed >= z3_down) && (z3_left_yfixed
<= z3_up);

sc3 = sc3_up || sc3_down || sc3_xfixed || sc3_right_yfixed ||
sc3_left_xfixed;

if ((sc2_A_up || sc2_A_down) && sc3)
Nd_true += 1;

else if ( (sc2_B_up || sc2_B_down) && sc3)
Nd_wa += 1;

else if ((!(sc2_A_up || sc2_A_down || sc2_B_up ||
sc2_B_down)) && sc3)
Nd_false += 1;

}

eff_geom = ((double)(Nd_true + Nd_wa)) / (Nd_true + Nd_wa +
Nd_false);

if (eff_geom < eff_geom_min)
eff_geom_min = eff_geom;
if (eff_geom > eff_geom_max)
eff_geom_max = eff_geom;

histo -> Fill(eff_geom);

}

histo -> GetXaxis() -> SetTitle("#varepsilon_{geom}");
histo -> GetYaxis() -> SetTitle("Counts");
histo -> GetXaxis() -> SetTitleSize(0.042);

gauss_distrib = new TF1 ("gauss_distrib", "gaus", eff_geom_min,
eff_geom_max);
gauss_distrib -> SetParameter(1, 0.93);

gStyle -> SetOptStat(11);
gStyle -> SetOptFit(1112);

canva -> cd();

histo -> Draw();

TFitResultPtr fit_result = histo -> Fit("gauss_distrib", "RS",
"sames");
TMatrixDSym covariance_matrix = fit_result -> GetCovarianceMatrix();

eff_geom = gauss_distrib -> GetParameter(1);


canva -> Modified();
canva -> Update();
canva -> SaveAs(("./"+dir+"/eff_geom"+suffix+".root").c_str());

delete histo;

return eff_geom;

}
