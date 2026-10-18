# Glossary wording for maintainer review

All groups in this document are now approved and applied. This document retains the reviewed wording as a decision record. The approved batch applied 27 groups; G17 and G33 were held because the surrounding explanation needs a larger revision. The original 14 decision groups follow those two cases. Equation numbers, exercise numbers, and established anchors would be preserved.

## G17 — Lever arm: held from the approved batch

**Applied:** approved simplified wording; pending preview refresh.

**Decision:** distinguish perpendicular lever arm from the radius used in the circular-motion derivation. Section 6.3 currently defines the lever arm as a distance to the application point and immediately writes torque as radius times force. Correcting only the glossary would leave this ambiguity.

**Proposed glossary:**

> **lever arm:** the perpendicular distance from the axis of rotation to the line along which a force acts

**Proposed replacement for the torque introduction in Section 6.3**, beginning “The turning effectiveness of force…” and ending immediately before the existing derivation:

> The turning effect of a force is called torque. Its magnitude is the force multiplied by its lever arm: the perpendicular distance from the axis of rotation to the force’s line of action. A larger lever arm gives a larger torque for the same force. For example, a lighter child on a seesaw can balance a heavier child by sitting farther from the pivot. In the circular-motion example considered here, the force is tangent to the circle, so its lever arm equals the radius r and the torque magnitude is τ = rF. Multiplying both sides of the preceding force equation by r therefore gives the torque on the left-hand side.

**Figure check:** the existing circular-motion figure and caption already specify that the applied force stays perpendicular to the radius. The proposed qualification matches that example; no figure edit is needed. The distinction between radius and perpendicular lever arm would be made explicit in the prose.

## G33 — Breeding and criticality: held from the approved batch

**Applied:** approved simplified wording; pending preview refresh.

**Decision:** approve replacing the general safety/Chernobyl claims as well as correcting the definitions. The current paragraph treats reactors made to produce plutonium as breeders and describes Chernobyl in that context. That historical/safety discussion should not be silently retained beneath a different technical definition.

**Proposed glossary entries:**

- **breeding:** production of new fissile material from fertile material by neutron capture and subsequent nuclear transformations
- **breeder reactors:** reactors designed to produce more fissile material than they consume
- **criticality:** the condition in which each generation of fissions produces, on average, one succeeding generation of the same size
- **supercriticality:** the condition in which the fission chain reaction grows because each generation produces more fissions in the next
- **critical mass:** the minimum mass of fissile material needed for a self-sustaining chain reaction under specified conditions of composition, shape, density, and surroundings

**Proposed breeding introduction**, placed before the existing uranium-to-plutonium reaction sequence:

> Neutron capture can convert fertile material, such as uranium-238, into fissile material, such as plutonium-239. This production of new fissile material is called breeding. The following reaction sequence shows how uranium-238 can be converted into plutonium-239 in a reactor.

**Proposed replacement for the paragraph following that sequence:**

> Some plutonium-239 is produced when uranium-238 in reactor fuel captures neutrons. A breeder reactor is designed to produce more fissile material than it consumes.

**Proposed criticality explanation**, replacing the corresponding definition sentences while keeping the control-rod discussion:

> A chain reaction is critical when, on average, each fission leads to one further fission. Its average rate then remains steady. It is subcritical when the rate decreases and supercritical when the rate increases. Whether a sample sustains a chain reaction depends on neutron production, absorption, and escape. Critical mass therefore depends on the material’s composition, shape, density, and surroundings, including neutron moderators and reflectors.

These distinctions follow the NRC definitions of [breeder](https://www.nrc.gov/reading-rm/basic-ref/glossary/breeder) and [criticality](https://www.nrc.gov/education-regulatory-research/glossary/criticality). The proposal removes the Chernobyl aside here rather than adding a new historical account.

## G05 — Electric and magnetic field strength

**Applied:** approved simplified wording; pending preview refresh.

**Recommendation:** define the field magnitudes directly. Move the glossary associations to Sections 9.4 and 10.5. Later electromagnetic-wave uses become cross-references. No discussion of H is proposed.

**Glossary:**

> **electric field strength:** the magnitude of the electric field, equal to the electric force per unit positive test charge

> **magnetic field strength:** the magnitude B of the magnetic field, measured in teslas

**Prose to add at the B introduction in Section 10.5:**

> The magnetic field strength is the magnitude B, measured in teslas.

**Simplification approved:** omit the H terminology aside and define B directly.

## G20 — Ampère’s law and the Biot–Savart law

**Applied:** approved wording and glossary definitions, with the stable linked section title below. Pending preview refresh.

**Recommendation:** give qualitative statements without introducing integral notation. Replace the paragraph in Section 10.8 that begins “The magnetic field of a long straight wire has more implications…” with:

> Each small segment of a steady current contributes to the magnetic field. The Biot–Savart law gives the size and direction of that contribution; adding the contributions from all segments gives the total field. Ampère’s law provides another relationship: for steady currents, the accumulated component of the magnetic field along a closed path is proportional to the net current passing through a surface bounded by that path. This is especially useful for highly symmetric current arrangements. Maxwell later extended this law to include changing electric fields, as discussed in [Maxwell’s Equations: Electromagnetic Waves Predicted and Observed](https://intro-1-1.coaphys.xyz/sections/maxwells-equations-electromagnetic-waves-predicted-and-observed/).

**Glossary:**

- **Biot–Savart law:** a law giving the magnetic-field contribution of a small segment of steady current
- **Ampère’s law:** for steady currents, a relationship between the magnetic field accumulated along a closed path and the net current passing through a surface bounded by the path

The equation derivations already present would remain. “Accumulated component” is the conceptual description of a line integral; no new calculation technique is proposed.

## G22 — Temperature and absolute zero

**Applied:** proposed temperature definition and simple absolute-zero wording; quantum caveat rejected by maintainer. Pending preview refresh.

**Approved approach:** use thermal equilibrium to explain temperature and omit the quantum caveat. In Section 8.2, replace the thermometer-only definition with:

> Temperature describes a system’s thermal state. Systems in thermal equilibrium have the same temperature. When systems at different temperatures can exchange energy as heat, the net transfer is from higher to lower temperature. A thermometer measures temperature by reaching thermal equilibrium with the system being measured.

At the Kelvin-scale introduction, replace any statement that all motion stops at absolute zero with:

> Absolute zero, 0 K, is the lower limit of the Kelvin temperature scale.

**Glossary:**

- **temperature:** a quantity describing thermal state; equal temperatures characterize thermal equilibrium, and temperature differences determine the direction of spontaneous heat transfer
- **absolute zero:** 0 K, the lower limit of the Kelvin temperature scale

**Maintainer decision:** remove “all motion ceases” and explain absolute zero directly, without introducing quantum mechanics at this stage.

## G27 — Lepton family numbers

**Applied:** approved simplified wording; pending preview refresh.

**Recommendation:** retain the existing decay examples but qualify the conservation statements. Preserve the approved italic family subscripts in Section 14.13.

**Replacement introduction before the electron-family decay example:**

> Leptons occur in electron, muon, and tau families. For each family, assign +1 to its charged lepton and neutrino, −1 to their antiparticles, and zero to other particles. Adding these values gives the corresponding family number, L_e, L_μ, or L_τ. The decay reactions considered here conserve each family number: the total before the reaction equals the total afterward.

**Replacement for the final universal-conservation discussion:**

> These family numbers are useful for analyzing the decay reactions shown here. However, they are not universally conserved: neutrino oscillations change the flavor composition of a neutrino as it propagates.

**Glossary:**

- **electron family number:** the number of electron-family leptons minus their antiparticles, with other particles contributing zero
- **muon family number:** the number of muon-family leptons minus their antiparticles, with other particles contributing zero
- **tau family number:** the number of tau-family leptons minus their antiparticles, with other particles contributing zero
- **conservation of total electron family number:** equality of the total electron family number before and after a process; applicable to the decay examples here, but not a universal law because of neutrino oscillations
- **conservation of total muon family number:** equality of the total muon family number before and after a process; applicable to the decay examples here, but not a universal law because of neutrino oscillations

In Section 14.5, qualify the existing electron-family conservation sentence by adding “in these beta-decay reactions.” The detailed family introduction remains in 14.13.

## G28 — Gauge bosons and Feynman diagrams

**Applied:** proposed prose and glossary definitions; maintainer approved “gauge field.” Pending preview refresh.

**Recommendation:** align the prose with the simplified figures without treating their lines as observed particle trajectories.

**Section 14.12, replacing the sentence that defines a Feynman diagram as a graph of time versus position:**

> A Feynman diagram represents a contribution to a quantum interaction calculation. Lines represent particles or their propagation, and vertices represent interactions. The diagrams shown here use position and time to help visualize particle exchange, but the lines should not be interpreted as measured trajectories.

**Section 14.13, replacing the generic carrier-particle naming sentence:**

> The photon, gluons, and W and Z bosons are gauge bosons: the particles associated with the electromagnetic, strong, and weak interactions in the Standard Model. The hypothetical graviton is discussed separately as a proposed carrier of gravity.

**Glossary:**

- **Feynman diagram:** a diagram representing a contribution to the calculation of a quantum interaction
- **gauge boson:** a particle associated with a gauge field; the Standard Model gauge bosons are the photon, gluons, and W and Z bosons

**Maintainer decision:** retain “gauge field” in the glossary definition.

## G29 — QCD, electroweak theory, and proposed unification

**Applied:** approved simplified wording; pending preview refresh.

**Recommendation:** retain the already revised Standard Model paragraph. Revise the later speculative discussion so that proposed unification is not stated as established fact.

**Glossary:**

- **quantum chromodynamics:** the theory of the strong interaction between quarks and gluons, based on color charge
- **electroweak theory:** the unified theory describing electromagnetic and weak interactions
- **grand unified theory:** a proposed theory that places the strong and electroweak interactions within a single framework
- **superstring theory:** a proposed theoretical framework in which fundamental particles correspond to different vibrational states of strings and which incorporates supersymmetry

**Replacement transition into the high-energy unification discussion in Section 14.14:**

> Electroweak theory and quantum chromodynamics are established parts of the Standard Model. Grand unified theories and superstring theories explore further unification that has not yet been experimentally established. Grand unified theories connect the strong and electroweak interactions at much higher energies; superstring theories pursue a broader framework that can also include gravity. Specific energy and length scales depend on the model.

**Your decision:** recommend replacing the paragraph’s asserted numerical unification scales with this qualitative account. Retaining those numbers would require identifying a particular model and labeling its assumptions.

## G34 — Quantum uncertainty and probability waves

**Applied:** approved simplified wording; pending preview refresh.

**Recommendation:** replace the measurement-disturbance explanation with intrinsic spreads, while retaining the existing position–momentum inequality and examples.

**Replacement core explanation in Section 12.5:**

> A quantum state generally does not assign one definite value to every measurable quantity. If we prepare many systems in the same state and measure position, the results have a distribution; measurements of momentum have another distribution. The spreads in position and momentum obey Heisenberg’s uncertainty principle. A state with a very narrow position distribution must have a broad momentum distribution. This restriction is a property of quantum states, not merely a consequence of imperfect instruments or a disturbance caused by measurement.

**Replacement probability-wave explanation:**

> A wave function describes a quantum state and is used to calculate probabilities for measurement outcomes. For position measurements, the squared magnitude of the wave function gives a probability density. The phrase “probability wave” refers to this wave-like probability amplitude.

**Energy–time qualification:**

> A short-lived unstable state has a spread of energies related to its lifetime. A shorter lifetime corresponds to a larger energy spread.

**Glossary:**

- **Heisenberg’s uncertainty principle:** the quantum restriction on the simultaneous spreads of certain pairs of quantities, such as position and momentum
- **uncertainty in position:** the spread of position measurement outcomes for systems prepared in the same quantum state
- **uncertainty in momentum:** the spread of momentum measurement outcomes for systems prepared in the same quantum state
- **probability wave:** an informal name for a wave function, whose squared magnitude gives a probability density for position

The distinction is supported by [OpenStax’s university-level uncertainty treatment](https://openstax.org/books/university-physics-volume-3/pages/7-2-the-heisenberg-uncertainty-principle). This is a coordinated replacement, not a glossary-only change.

## G36 — Mass, inertia, energy, and time

**Applied:** approved simplified wording; pending preview refresh.

**Recommendation:** keep these introductions operational and concise.

**Section 2.3, replacing the mass/inertia definition sentences:**

> Inertia is an object’s resistance to a change in velocity. Mass measures inertia: a larger mass requires a larger net force to produce the same acceleration. Mass is a property of the object; its weight is the gravitational force acting on it.

**Section 3.2, replacing the “ability to do work” definition:**

> Energy is a quantity that we use to track physical changes and transfers between systems. Work transfers energy when a force acts through a displacement. Energy can take different forms, but the total energy of an isolated system remains constant.

**Section 1.4, replacing “time is change” and its immediate definition:**

> Time allows us to describe the order of events and the intervals between them. We measure a time interval by comparing it with a repeating process, such as the oscillations used in a clock.

**Glossary:**

- **mass:** a measure of an object’s inertia
- **inertia:** resistance to a change in velocity
- **energy:** a conserved quantity that can be transferred between systems and converted between forms
- **time:** the physical quantity used to describe when events occur and the intervals between them

**Your decision:** this replaces familiar textbook shorthand with operational descriptions. The purpose is clarity, without pretending to derive these foundational quantities from simpler concepts.

## G39 — Forms of energy

**Applied:** approved simplified wording; pending preview refresh.

**Recommendation:** revise the relevant sentences in Section 3.5 together, then use the same distinction in Chapter 8.

**Replacement energy-form explanation:**

> Electrical energy is associated with electric charges and fields; it can be stored, as in a charged capacitor, or transferred through a circuit. Chemical energy is associated with the arrangement and interactions of atoms and electrons. A chemical reaction releases energy when its products have less energy than its reactants; breaking a bond by itself requires energy. Thermal energy is associated with the disordered microscopic motion and interactions of matter. It is part of a system’s internal energy, which includes microscopic kinetic and potential energies.

**Chapter 8 clarification at the internal-energy introduction:**

> Internal energy is energy associated with the system’s microscopic constituents and their interactions. It excludes the kinetic energy of the system’s overall motion and the potential energy associated with its position in an external field. Heat and work are ways of transferring energy.

**Glossary:**

- **electrical energy:** energy associated with electric charges and electric fields
- **chemical energy:** internal energy associated with the arrangement and interactions of atoms and electrons
- **thermal energy:** the part of internal energy associated with disordered microscopic motion and interactions
- **internal energy:** the total microscopic kinetic and potential energy of a system’s constituents

**Your decision:** “thermal energy” has less uniform usage than “internal energy.” This proposal uses it as a useful introductory category without equating it with all internal energy.

## G42 — Entropy

**Applied:** approved simplified wording; pending preview refresh.

**Recommendation:** introduce the thermodynamic quantity first in 8.13; give the microscopic interpretation in 8.14. Retain the existing examples but revise statements that treat “disorder” as a precise definition.

**Section 8.13 introduction:**

> Entropy is a property of a system’s state that helps us describe the direction of spontaneous processes. For reversible heat transfer at a constant absolute temperature, the entropy change is the heat transferred into the system divided by that temperature. The total entropy of an isolated system cannot decrease: it remains constant for an ideal reversible process and increases for an irreversible process.

**Section 8.14 bridge:**

> A macroscopic state can correspond to many microscopic arrangements. Entropy increases with the number of microscopic arrangements compatible with that state. This provides a more precise interpretation than the everyday word “disorder.” Spontaneous changes overwhelmingly favor macroscopic states compatible with more microscopic arrangements.

**Glossary:**

> **entropy:** a thermodynamic state quantity whose change for reversible heat transfer at constant temperature equals the heat transferred into the system divided by the absolute temperature; microscopically, it is related to the number of compatible microscopic arrangements

**Your decision:** approve a coordinated pass through the two sections, including their “disorder” wording, rather than only the opening definition. The thermodynamic starting point follows [OpenStax’s thermodynamics summary](https://openstax.org/books/university-physics-volume-2/pages/4-summary).

## G46 — Polarization

**Applied:** approved simplified wording; pending preview refresh.

**Recommendation:** explicitly limit the existing directional examples to linear polarization. No new calculation or treatment of elliptical polarization is needed.

**Replacement introductory explanation in Section 11.11:**

> Polarization describes how the direction of a transverse wave’s oscillation varies. For light, we describe it using the electric field. In linearly polarized light, the electric field oscillates along a fixed direction perpendicular to propagation.

**Replacement unpolarized-light explanation:**

> Unpolarized light has no persistent preferred polarization direction. Its polarization fluctuates irregularly, so a polarizer transmits only part of its average intensity.

**Replacement birefringence definition sentence:**

> A birefringent material has different refractive indices for different polarization modes. In suitable directions this can split an incident beam into two beams with different polarizations.

**Glossary:**

- **polarization:** the pattern of directions of a transverse wave’s oscillation; for light, described by the electric field
- **direction of polarization:** for linearly polarized light, the fixed direction along which its electric field oscillates
- **horizontally polarized:** linearly polarized with a horizontal electric-field direction, perpendicular to propagation
- **vertically polarized:** linearly polarized with a vertical electric-field direction, perpendicular to propagation
- **unpolarized:** having no persistent preferred polarization direction
- **birefringent:** having different refractive indices for different polarization modes

For the rope analogy, use “displacement” in place of “electric field.” Keep its horizontal/vertical examples.

## G47 — Quantum and atomic-model terminology

**Applied:** approved simplified wording; pending preview refresh.

**Recommendation:** distinguish ideal models from modern physical descriptions. The hydrogen-spectrum-wavelength glossary entry was already removed under G14 and would stay removed.

**Section 12.2, replacement blackbody introduction:**

> A blackbody is an ideal absorber of all electromagnetic radiation incident on it. In thermal equilibrium it emits a spectrum determined by its temperature. This blackbody radiation is described by Planck’s law. Real objects can approximate this spectrum, but their emission also depends on their material and surface properties.

**Section 12.6, replacement planetary-model definition sentences:**

> The planetary model pictures electrons orbiting a small, massive nucleus. It was an important historical step, but classical orbiting electrons cannot explain stable atoms. Quantum mechanics describes electrons using quantum states rather than definite planetary trajectories.

**Section 12.7, replacement Bohr-radius definition sentence:**

> The Bohr radius is the radius of the lowest-energy electron orbit in the Bohr model of hydrogen.

**Glossary:**

- **blackbody radiation:** the thermal electromagnetic radiation emitted by an ideal blackbody, with a spectrum determined by its temperature
- **Planck law:** the law describing the spectrum of blackbody radiation as a function of temperature and wavelength or frequency
- **planetary model of the atom:** a historical model in which electrons orbit a small, massive nucleus
- **Bohr radius:** the ground-state orbital radius of hydrogen in the Bohr model, also a characteristic atomic length scale
- **work function:** the minimum energy required to remove an electron from a material’s surface into vacuum
- **correspondence principle:** the requirement that a newer theory reproduce the successful predictions of an older theory in the conditions where the older theory applies

At the photoelectric-effect introduction, use the same minimum-removal-energy wording for work function. At the correspondence-principle introduction, add: “Quantum mechanics reproduces classical predictions in the appropriate limit.”

## G49 — Fusion gain, ignition, and confinement

**Applied:** approved simplified wording; pending preview refresh.

**Recommendation:** identify which input energy is being counted and separate self-heating from useful power production.

**Replacement break-even/ignition explanation in Section 14.9:**

> Fusion experiments compare fusion energy output with energy supplied at a specified stage of the experiment. Break-even means that those two quantities are equal; the comparison must state which input is counted. For example, energy delivered to a fusion target is different from the electrical energy used by the whole facility. Ignition refers to conditions in which energy deposited by fusion products sustains the fuel’s heating against its losses. Neither target-level gain nor ignition by itself establishes that a facility produces net useful electrical energy.

**Replacement inertial-confinement explanation:**

> In inertial confinement, a small fuel target is rapidly compressed and heated. The fuel’s inertia keeps it dense for a very short time before it expands, allowing fusion reactions to occur during that interval.

**Glossary:**

- **break-even:** equality of fusion energy output and a specified energy input; the boundary used to count input energy must be stated
- **ignition:** fusion conditions in which heating by fusion products sustains the hot fuel against energy losses
- **inertial confinement:** brief confinement of rapidly compressed fusion fuel by its own inertia before it expands
- **proton-proton cycle:** a sequence of fusion reactions whose net effect is to convert four protons into a helium-4 nucleus, with positrons, electron neutrinos, and released energy

**Your decision:** use this definition-only update without a dated milestone, or also update the experimental-status discussion. A dated account needs a separate current-source check. The distinction between target input and facility input matters when interpreting the [DOE’s NIF ignition announcement](https://www.energy.gov/articles/doe-national-laboratory-makes-history-achieving-fusion-ignition).

## G51 — Optional vocabulary

**Applied:** approved simplified wording; pending preview refresh.

**Recommendation:** remove these separate glossary headwords and their formal-definition styling, while retaining useful local explanations: **statistical analysis, TV, laser printer, ink-jet printer, simple circuit**. They are methods, familiar applications, or labels for examples rather than concepts requiring their own glossary entries here.

Retain these two with clearer definitions:

> **human metabolism:** the chemical processes in the human body that transform matter and energy to sustain life

> **magnetized:** having a net magnetization, with microscopic magnetic moments sufficiently aligned to produce an overall magnetic effect

**Local wording for “simple circuit,” replacing the universal-sounding definition in Section 9.9:**

> The simple circuit considered here contains one voltage source and one resistor. We neglect the resistance of the connecting wires or include it in the stated resistance.

**Your decision:** approve the five removals and two retained definitions, or specify any of the seven that you prefer to keep/remove differently.

## Approved scope after simplification

The maintainer approved and applied all remaining proposals, including the G51 removals. G17’s perpendicular lever-arm distinction and G49’s explicit input-energy accounting are retained.

- **G42:** a coordinated entropy revision across both sections remains a substantial pedagogical change. Recommend the proposed thermodynamic-first treatment, with the microscopic explanation in the following section.
- **G39:** the boundary between thermal energy and internal energy uses the approved consistent textbook convention. Recommend the proposed wording, while checking adjacent examples before application.
- **G49:** recommend the definition-only update for now; any experimental-status update is a separate current-source task.
- **G51:** the proposed five removals and two retained definitions were approved.
- **G34:** the conceptual replacement is clear, but its implementation must be checked against the surrounding examples and energy–time equations so that the explanation is consistent.

No additional significant physics uncertainty was identified in the other proposals. These remaining questions concern teaching scope and consistency.

## Applied batch and validation

Applied groups: G01, G02, G03, G10, G11, G12, G13, G16, G18, G21, G23, G24, G25, G26, G30, G31, G32, G35, G37, G38, G40, G41, G43, G44, G45, G48, G50.

The applied changes are recorded separately in `glossary-quality-applied-batch.json` and reversible source proposals. Validation: all changed XML parsed; existing source anchors, equation IDs and exercise IDs/order were preserved; 19 new or changed targeted cross-references resolved; 501 standalone glossary entries remain with no exact duplicate headwords. The complete course build passed with 6,660 MathML expressions and no reported issues. No preview publication was requested for this batch. Source checks include the [BIPM SI description](https://www.bipm.org/en/measurement-units/), [2018 SI resolution](https://www.bipm.org/en/committees/cg/cgpm/26-2018/resolution-1), and [FDA’s curie conversion](https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/inspection-technical-guides/radiation-protection-terminology).

Final validation: 496 standalone glossary entries, no exact duplicate headwords; source anchors, equation and exercise IDs/order preserved. Fusion experimental-status text is unchanged. Next review: scan hard-coded chapter/section references and use stable linked section titles where appropriate before renumbering.

Unification consistency sources: [CERN unified forces](https://home.web.cern.ch/science/physics/unified-forces/) and [Super-Kamiokande proton-decay search](https://www-sk.icrr.u-tokyo.ac.jp/en/news/detail/264). No updated numerical lifetime limit was inserted.

Final full course build passed: 6,628 MathML expressions, no reported issues, 8,741 search passages. All 51 review groups have recorded decisions.
