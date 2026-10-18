"""Reviewed selected-emission transcription; energies in MeV, yields per 100 decays.

Source PDFs/HTML are archived alongside the output. This produces a review manifest,
not source edits. Display precision is deliberately lower than reference precision.
"""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
D=ROOT/'reports/1.1/appendix-b-consistency'
# Each entry: selected charged-particle emissions or EC/IT branch; gamma photons;
# audit rationale. EC/IT have no emitted-particle energy in the particle column.
data={
'H-3':([['bm','0.0186','100']],[], 'Endpoint agrees at textbook precision; DDEP emission endpoint 18.564 keV.'),
'C-14':([['bm','0.1565','100']],[], '156.476 keV endpoint; beta mean energy is 49.16 keV, not half the endpoint.'),
'N-13':([['bp','1.198','99.8'],['EC','','0.197']],[], '1198.47 keV; 99.803% positrons and 0.197% EC. Annihilation photons remain outside the selected photon list.'),
'Na-22':([['bp','0.5464','90.3'],['EC','','9.64']],[['1.275','99.9']], 'DDEP 546.44 keV at 90.30%; 1274.537 keV photons at 99.94%. Selected positron branch excludes the 0.055% high-energy branch. EC combines 9.64% and 0.00098%; approved DDEP convention supersedes the interim NUBASE fractions.'),
'P-32':([['bm','1.711','100']],[], '1710.661 keV endpoint.'),
'S-35':([['bm','0.1673','100']],[], '167.33 keV endpoint.'),
'Cl-36':([['bm','0.7095','98.1'],['EC','','1.9']],[], 'DDEP distinguishes EC from the 0.00157% positron branch, below the principal-mode cutoff.'),
'K-40':([['bm','1.311','89.6'],['EC','','10.4']],[['1.461','10.3']], 'DDEP: 1310.91 keV beta endpoint at 89.56%; EC 10.34% to excited state plus 0.098% to ground state; 1460.822 keV gamma at 10.34%. Positrons 0.00103% omitted. Approved DDEP convention supersedes interim NUBASE fractions.'),
'K-43':([['bm','0.827','92.2']],[['0.3728','87.3'],['0.6175','80.5']], 'LNHB LARA scheme: 92.2% beta feeding to the 990.3 keV level; endpoint approximately 1817-990.3=826.7 keV. Gamma yields 87.3% and 80.5% are not both 87%.'),
'Ca-45':([['bm','0.2580','≈100']],[], '258.0 keV at 99.9980%; rare beta branch omitted.'),
'Cr-51':([['EC','','100']],[['0.3201','9.89']], '320.0835 keV photons at 9.89%.'),
'Mn-52':([['bp','0.576','30.9'],['EC','','≈69']],[['1.334','5.08'],['1.434','≈100']], 'Old 3.69 MeV is not an identified populated beta branch; replace with dominant 576.1(19) keV branch at 30.85%. EC total approximately 68.9%. Retain identifiable 1333.614 keV (5.079%) and 1434.060 keV (99.9866%) photons.'),
'Fe-52':([['bp','0.807','56.1'],['EC','','43.9']],[['0.1687','99.1'],['0.3777','1.64']], 'Correct dominant endpoint 807(6) keV, not 1.80 MeV. EC total 43.895%. DDEP photon yields 99.1% and 1.64%; 377.749 keV is from daughter Mn-52m IT.'),
'Fe-59':([['bm','0.2734','45.2'],['bm','0.4657','53.3']],[['1.099','56.5'],['1.292','43.2']], 'DDEP 45.19% and 53.30% beta branches; photons 56.51% and 43.23%. Selected branches do not sum to 100%.'),
'Co-60':([['bm','0.3173','99.9']],[['1.173','99.9'],['1.332','≈100']], '317.32 keV at 99.88%; photons 1173.228 keV at 99.85% and 1332.492 keV at 99.9826%.'),
'Zn-65':([['EC','','98.6'],['bp','0.3299','1.42']],[['1.116','50.2']], 'DDEP EC 50.23+48.35%; positrons 329.9 keV at 1.421%; principal positron branch was missing. Gamma 1115.539 keV at 50.22%.'),
'Ga-67':([['EC','','100']],[['0.09331','38.1'],['0.1846','21.0'],['0.3002','16.6']], 'Correct photon yields 38.1%, 20.96%, 16.60%; old 70%,35%,19% are not these photon yields.'),
'Se-75':([['EC','','100']],[['0.1211','16.9'],['0.1360','57.7'],['0.2647','58.8'],['0.2795','24.9']], 'DDEP photon yields 16.86%,57.7%,58.75%,24.89%.'),
'Rb-86':([['bm','0.698','8.71'],['bm','1.774','91.3']],[['1.077','8.71']], 'LNHB LARA: Q=1774.3 keV, level1076.78 keV => endpoint697.52 keV; beta feeding8.71%,91.29%; gamma1076.78keV at8.71%. EC0.0052% omitted.'),
'Sr-85':([['EC','','100']],[['0.5140','98.5']], '514.0048 keV photons at98.5%.'),
'Sr-90':([['bm','0.546','100']],[], '545.9(14) keV endpoint; daughter Y-90 listed separately.'),
'Y-90':([['bm','2.279','≈100']],[], '2278.7(16) keV endpoint at99.983%; very weak additional branches omitted.'),
'Tc-99m':([['IT','','≈100']],[['0.1405','88.5']], 'Old0.142MeV100% conflates isomer excitation with principal photon. Dominant gamma140.511keV at88.5%; distinct142.683keV photon only0.023%. Replace ambiguous entry with dominant line, as approved.'),
'In-113m':([['IT','','100']],[['0.3917','65.0']], 'LNHB LARA gamma391.698keV at64.97%, not100%.'),
'I-123':([['EC','','100']],[['0.1590','83.3']], '158.97keV photons at83.25%, not approximately100%.'),
'I-131':([['bm','0.2479','2.13'],['bm','0.6063','89.4']],[['0.3645','81.2']], 'Retain identifiable endpoints247.9keV and606.3keV, correct fractions2.130% and89.4%; old7% belongs near333.8keV branch. Photon364.489keV at81.2%.'),
'Cs-129':([['EC','','']],[['0.03958','2.97'],['0.3719','30.6'],['0.4115','22.3']], 'ICRP107 via MIRDspecs:39.578keV at2.968%,371.918keV at30.60%,411.490keV at22.31%. Old40keV35% is not the photon yield. EC fraction not newly inferred.'),
'Cs-137':([['bm','0.5140','94.6'],['bm','1.176','5.43']],[['0.6617','85.0']], 'DDEP beta endpoints513.97keV at94.57%,1175.63keV at5.43%; gamma661.655keV at85.01%, not95%; daughter Ba-137m transition.'),
'Ba-140':([['bm','0.467','24.9'],['bm','1.004','35.6'],['bm','1.018','25.6']],[['0.02996','14.4'],['0.1627','6.49'],['0.5373','24.6']], 'Replace unidentifiable1.035MeV≈100% with three dominant beta endpoints; replace unidentified44keV65% photon with evaluated162.6591keV6.49%. Keep29.9641keV14.4%,537.261keV24.6%.'),
'Au-198':([['bm','0.9610','99.0']],[['0.4118','95.6']], 'Replace incorrect1.161MeV with dominant961.0keV endpoint98.99%;411.80205keV gamma95.62%.'),
'Hg-197':([['EC','','100']],[['0.07735','18.8']], 'LNHB LARA principal77.352keV gamma at18.8%; old73.3keV100% not identifiable.'),
'Po-210':([['a','5.304','≈100']],[], 'Alpha particle5304.33keV at99.99876%; old5.41MeV is close to total transition energy including recoil.'),
'Ra-226':([['a','4.601','5.95'],['a','4.784','94.0']],[['0.1862','3.56']], 'Use emitted alpha energies4601keV and4784.34keV rather than transition energies4684.41/4870.62keV. Gamma186.211keV yield3.555%, not100%.'),
'U-235':([['a','4.215','5.95'],['a','4.366','18.8'],['a','4.398','57.2']],[['0.1438','10.9'],['0.1634','5.08'],['0.1857','57.0']], 'Replace4.68MeV≈100% with three dominant alpha lines4214.7,4366.1,4397.8keV. Replace numerous/<0.400% with three strong photons143.767,163.356,185.720keV.'),
'U-238':([['a','4.151','22.3'],['a','4.198','77.5']],[['0.04955','0.0697']], 'Alpha particle4151(5),4198(3)keV, not transition energies4.22/4.27MeV. Gamma49.55keV at0.0697%, not23%.'),
'Np-237':([['a','4.767','9.5'],['a','4.771','23.0'],['a','4.788','47.6']],[['0.02937','14.3'],['0.08648','12.3']], 'Replace vague numerous/max4.96MeV and gamma<0.250% with dominant alpha4766.5,4771.4,4788.0keV and photons29.374,86.477keV.'),
'Pu-239':([['a','5.106','11.9'],['a','5.144','17.1'],['a','5.157','70.8']],[['0.0000765','≈0.00000001'],['0.01298','0.0341'],['0.05162','0.0269']], 'Correct emitted alpha energies5105.81,5143.82,5156.59keV; yields11.87,17.14,70.79%. Retain identifiable gamma0.0765,12.975,51.624keV, but yields approximately1e-8,0.0341,0.02694 per100 decays, not73%,15%,10%.'),
'Am-243':([['a','5.233','11.5'],['a','5.275','86.7'],['a','5.349','0.240']],[['0.07466','67.2']], 'Use particle5233.3,5275.3,5349.4keV (last is maximum) instead of total transition energies5.32,5.37,5.44MeV. Gamma74.66keV67.2%.'),
}
lara={'K-43','Rb-86','In-113m','Hg-197'}
out=[]
for isotope,(charged,gamma,note) in data.items():
    source=('https://www.lnhb.fr/Laraweb/' if isotope in lara else 'https://mirdsoft.org/products/MIRDspecs/MIRDspecs_HTMLs/Cs-129.htm' if isotope=='Cs-129' else f'https://www.lnhb.fr/nuclides/{isotope}_tables.pdf')
    out.append(dict(isotope=isotope,charged=charged,gamma=gamma,audit_note=note,source=source))
assert len(out)==38
(D/'selected-emissions.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Wrote 38-isotope selected-emission manifest.')
