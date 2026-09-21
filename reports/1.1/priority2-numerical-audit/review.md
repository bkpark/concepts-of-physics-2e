# Priority 2 numerical audit

Original priority 2 only: radiation/medical numerical tables and directly connected claims; not a book-wide numerical audit.

Source-linked inventory and recommended directions, not final patches. No textbook edits applied.

## P2-01 — Acute-effects table

Closer review: table structure and source interpretation

- The table uses Sv/rem for acute tissue injury; revise to absorbed dose in Gy/rad and state the applicable exposure conditions.
- CDC gives LD50/60 as about 2.5–5 Gy; this does not support the textbook’s exact 4.5 Sv LD50/32 entry.
- CDC places the full gastrointestinal syndrome above about 10 Gy and the full cardiovascular/CNS syndrome above about 50 Gy, with some symptoms at lower doses. The textbook’s >20 Sv → fatal within hours is too categorical.
- The fertility row mixes sex-specific organ effects into a whole-body table. ICRP’s published table does not support 0.35 for women as a general temporary-sterility threshold.

**Recommendation:** Rebuild a short table around clear absorbed-dose bands and major acute effects. Prefer a consistent CDC whole-body framework; treat fertility separately or remove that row from this table. Do not merely change Sv to Gy while retaining every old row.

**Review:** Review how much clinical detail belongs in the conceptual textbook. The most important source distinction is threshold/symptom onset versus a usual full syndrome, and LD50/60 versus LD50/32.

**Source limits:** CDC numbers apply to specified radiation/exposure conditions and are approximate. Survival depends on treatment and the exposed population. The ICRP fertility source is older and is not a warrant for copying its entire table; a final modern fertility row would need a dedicated check if retained.

- [CDC: Acute Radiation Syndrome for clinicians](https://www.cdc.gov/radiation-emergencies/hcp/clinical-guidance/ars.html) — The three classic syndromes; Table 1; dose footnotes
- [ICRP: Radiation and your patient](https://www.icrp.org/docs/Rad_for_GP_for_web.pdf) — Printed page 11, Table 1; organ-specific sterility rows

## P2-02 — Dose bands and retrospective detection

Closer review: quantity and scope

- The 0.1 and 1 thresholds are recognizable dose-band conventions, but the paragraph calls them universal Sv-based categories.
- UNSCEAR 2012 Table 1 expresses comparable bands in absorbed dose for low-LET radiation, with low and very-low subdivisions.
- IAEA gives about 0.1 Gy as the detection level for a specified dicentric-chromosome assay. That is not evidence for a universal statement that exposure below 10 mSv cannot be determined after the fact.

**Recommendation:** Keep approximate low/moderate/high terminology but specify absorbed dose and radiation type, and align the three glossary entries. Replace or omit the blanket retrospective-detection sentence; do not substitute the assay threshold as a universal limit.

**Review:** Review the short terminology paragraph and whether a method-specific detection example is worth keeping. You need not arbitrate assay performance; I will not claim a general cutoff from a specific test.

**Source limits:** The source is clear about the assay, but does not establish the textbook’s universal 10 mSv claim. Dose-band boundaries are conventions, not biological discontinuities.

- [UNSCEAR 2012 Annex A](https://www.unscear.org/unscear/uploads/documents/publications/UNSCEAR_2012_Annex-A.pdf) — Printed page 23, Table 1 and footnotes
- [IAEA GSG-7: dicentric chromosome assay](https://nucleus.iaea.org/sites/nss-oui/Published%20Chunks/m_cf1f9f91-f97c-4467-a9e6-e24560302f61/c_465a704d-72b5-4f55-be33-42757d378fb3__1_0.Html) — Paragraphs A–7 and A–8

## P2-03 — Background-dose table and linked figures

Closer review: choose a coherent table scope

- The displayed old totals are consistent with rounding: Australia 2.64→2.6, Germany 2.96→3.0, US 3.53→3.5, world 2.76→2.8 mSv/year. The issue is provenance and comparability, not addition.
- UNSCEAR 2024 reports a global natural-source average of about 3.0 mSv/year: cosmic 0.3, terrestrial 0.4, food/water 0.5, and radon/thoron 1.8.
- This replaces an earlier global natural-source estimate of 2.4 mSv/year. UNSCEAR explicitly attributes the difference to improved methods and data coverage, not necessarily increased exposure.

**Recommendation:** Prefer a dated global natural-background table from one assessment, with medical exposure discussed separately. Retaining all three national columns would require independently dated national estimates and method notes; do not mix them into an apparently simultaneous survey.

**Review:** Review whether the national comparisons are pedagogically important. Source numbers for the global alternative are clear; the structural choice needs your judgment.

**Source limits:** The original national values have no year or source in the table and have not been certified. Do not compare newer 3.0 natural-only with old 2.8 including medical as though the scope were identical.

- [UNSCEAR 2024, Volume I](https://www.unscear.org/unscear/uploads/documents/unscear-reports/UNSCEAR_2024_Report_Vol.I.pdf) — Report to the General Assembly, printed page 11, paragraphs 44–45 and chart

## P2-04 — Aircrew and flight example

Routine sourced update; check wording only

- UNSCEAR 2024 cites an aircrew average of 2.7 mSv/year (range 1.5–4.5), rather than the undated 2 in the text.
- The claimed 0.02–0.03 mSv for a generic 12-hour flight has no route or source. CDC provides a named New York–Los Angeles example of about 0.035 mSv.

**Recommendation:** Use a dated aircrew estimate and replace the generic duration-only flight estimate with a named route example, without implying every flight on that route has exactly that dose.

**Review:** Only review whether the example reads naturally. No unresolved unit conversion; 0.035 mSv = 35 µSv.

**Source limits:** The original 12-hour value is unverified, not proven impossible. Route, altitude and conditions matter; the named-route replacement is an illustrative estimate.

- [UNSCEAR 2024, Volume II](https://www.unscear.org/unscear/uploads/documents/unscear-reports/UNSCEAR_2024_Report_Vol.II.pdf) — Annex B, printed page 53, aircrew and air-travel discussion
- [CDC: Radiation Thermometer](https://www.cdc.gov/radiation-emergencies/causes/radiation-thermometer.html) — Typical high-altitude flight from New York City to Los Angeles

## P2-05 — CT procedure and dose shares

Routine sourced update; denominator must remain explicit

- The current <20% of X-ray procedures / about 50% of annual dose claim gives neither place nor date, and annual dose has an unspecified denominator.
- UNSCEAR’s official 2020/2021 assessment summary gives CT about 10% of medical examinations/procedures and 62% of their collective effective dose worldwide.

**Recommendation:** Use a dated assessment statement with medical-exposure scope: In UNSCEAR’s 2020/2021 assessment, CT accounted for about 10 percent of medical examinations and procedures worldwide but about 62 percent of their collective effective dose.

**Review:** Review wording only; the percentages are explicitly reported together. Do not describe 62% as a share of natural-plus-medical radiation, or as a current-year measurement.

**Source limits:** The old denominator cannot be recovered from this paragraph. The official summary supports the proposed new denominator. The full-report PDF text extraction failed in this session; the linked official summary slide is directly readable. Nearby carbon-14/fertilizer activities in this same paragraph also lack a clear per-kilogram basis/source and remain a connected open check, not certified by the CT result.

- [UNSCEAR medical-exposure assessment launch, May 2022](https://www.unscear.org/unscear/uploads/res/events/webinars/2022-05_online-launch-of-unscear-2020-2021-report--annex-a_-evaluation-of-medical-exposure-to-ionizing-radiation_html/UNSCEAR_Medical_Exposure_Launch_20220525.pdf) — Slide headed Summary of the 2020/2021 assessment

## P2-06 — Radiopharmaceutical activity table

Closer review: source-to-procedure matches are incomplete

- There are 20 activity rows. An isotope and organ alone often do not identify the preparation, route, or protocol; a label range cannot silently be called the typical activity for every use of that isotope.
- Tc-99m bone value 10 mCi is compatible with the medronate adult label range 10–20 mCi (370–740 MBq). Tc-99m lung value 2 mCi is compatible with the MAA adult range 1–4 mCi (37–148 MBq). These verify only named formulations/procedures.
- For a named brain-perfusion example, Ceretec/exametazime specifies 15–30 mCi (555–1110 MBq), not the generic 7.5 mCi in the book. That is a scope mismatch, not proof that every historical Tc-99m brain study used an incorrect amount.
- The conversion 1 mCi = 3.7 × 10^7 Bq = 37 MBq is correct.

**Recommendation:** Prefer a smaller set of explicitly named diagnostic examples with adult label ranges, in MBq and mCi, rather than retaining an untraceable comprehensive-looking table. Keep the radioisotope diversity/PET discussion, but reconcile any links that currently rely on removed rows.

**Review:** Review the choice of examples and table size. This is the main item where you should consult source headings if you want to inspect a match: product, indication and adult Dosage and Administration must all agree. I am not marking the other 17 existing activity rows as verified.

**Source limits:** Current sources support three named examples; only two match an existing number directly. The remaining original rows are unresolved, not automatically wrong or obsolete. Selecting a reduced table is a structural decision and remains held.

- [DailyMed: technetium Tc-99m medronate](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=3c91d0d8-6cc5-834c-bda0-aa83a873b9fb) — Dosage and Administration, adult bone-imaging activity
- [DailyMed: DRAXIMAGE MAA](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?lang=en&setid=bbefaa05-1dc0-3ae7-7264-ce1eddf0da2b) — Section 2.3, adult lung scintigraphy
- [GE Healthcare: Ceretec prescribing information](https://www.gehealthcare.com/-/jssmedia/GEHC/US/Files/Products/Molecular-Imaging/Ceretec-Cobalt/Ceretec-Cobalt-Prescribing-Information-092018-CERETEC-with-Cobalt-Chloride-BK) — Section 2, Cerebral Scintigraphy adult dosing
