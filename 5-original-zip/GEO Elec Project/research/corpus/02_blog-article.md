<!-- Blog article | Data center community opposition: How cooling design affects water, noise, and permitting | https://blog.se.com/datacenter/2026/10/08/data-center-community-opposition-how-cooling-design-affects-water-noise-and-permitting/ -->
<!-- html_title: Data center community opposition: How cooling design affects water, noise, and permitting - Schneider Electric Blog | meta: {"description": "Data center community opposition is putting water use, noise, and permitting under greater scrutiny across the US. See how cooling design shapes local approvals.", "og:title": "Data center community opposition: How cooling design affects water, noise, and permitting", "og:description": "Data center community opposition is putting water use, noise, and permitting under greater scrutiny across the US. See how cooling design shapes local approvals.", "article:published_time": "2026-10-08T12:00:00+00:00", "article:modified_time": "2026-10-16T05:46:42+00:00", "author": "Guest Blogger", "time_elements": ["2026-10-08T08:00:00-0400"]} | jsonld: ['Article', 'BreadcrumbList', 'CommentAction', 'EntryPoint', 'ImageObject', 'ListItem', 'Person', 'PropertyValueSpecification', 'ReadAction', 'SearchAction', 'WebPage', 'WebSite'] -->

Data Centers

# Data center community opposition: How cooling design affects water, noise, and permitting

- October 8, 2026
- 119 views
- 7 min read
- Guest Blogger

Author: Andrew Whitmore, VP of Sales of Motivair, Motivair by Schneider Electric

Summary

- Data center approvals reflect a broad set of infrastructure and community concerns. Power demand, utility capacity, land use, backup generation, water use, noise, and other site impacts can all shape local review; cooling is one of the technical decisions that directly affects water and acoustic impacts.
- The full heat-rejection path determines much of the site impact. Closed-loop direct-to-chip cooling may reduce water use and air movement inside the data hall, but outdoor chillers, cooling towers, dry coolers, fans, and pumps still shape the facility’s water and acoustic profile.
- Permitting assumptions need to carry through design and construction. Water-demand estimates, acoustic models, equipment orientation, controls, setbacks, and other approval conditions should be translated into specifications, procurement requirements, and commissioning criteria.
- Cooling and power planning should be part of the broader approval strategy. A system-level approach can help operators balance higher-density workloads with local water, noise, site, and community constraints.

Data center community opposition and local approvals are becoming bigger constraints on capacity development. The issues shaping project review extend well beyond cooling and can include power availability, utility capacity, transmission infrastructure, backup generation, land use changes, property-value concerns, water resources, and permitting complexity.

## Why are communities so opposed to data centers?

In a March 2026 Gallup survey, among respondents who opposed a local AI data center, water and energy were each cited by 18%, while 16% cited pollution, a category that included noise along with air and water pollution. The survey does not predict the outcome of individual projects, but it shows why resource use and site impacts are receiving closer scrutiny.

Cooling design is one of several technical decisions that can affect site impacts, particularly water use and noise, alongside broader concerns such as power demand, utility infrastructure, land use, and backup generation. Closed-loop direct-to-chip cooling may recirculate coolant at the rack, while the facility’s overall water and acoustic profile depends heavily on how heat is ultimately rejected outdoors. Permitability should be built into cooling decisions early, before site plans, equipment schedules, and public commitments become immutable.

![](img)

## Cooling design is a critical aspect of data center community opposition and permitting

There is no single U.S. permitting pathway for a data center. Requirements vary by state, municipality, zoning status, water source, utility infrastructure, and environmental conditions. Large projects may face zoning hearings, water and wastewater reviews, stormwater requirements, acoustic studies, and post-construction verification.

Cooling architecture can affect several of those reviews. Officials may request information on annual and peak-day water demand, potable versus reclaimed water, drought operations, wastewater discharge, and treatment. Acoustic review may address nighttime operation, tonal and low-frequency sound, cumulative campus buildout, and maximum fan or compressor duty.

For design teams, early assumptions can become permit commitments. A noise study may depend on low-noise fans, equipment orientation, barriers, or setbacks. A water-feasibility study may depend on a specific heat-rejection method or operating temperature. Equipment changes later in the project can alter those assumptions.

The most useful way to evaluate cooling for permitting is to follow the complete heat path from the CPU or GPU and cold plate, through the Coolant Distribution Unit (CDU) and facility loop, to the equipment that rejects heat outdoors. That final stage often determines the water and acoustic profile that officials and communities will see and can affect how the project is evaluated during local review.

## Water use depends on the full heat-rejection path

In a direct-to-chip system, coolant circulates through cold plates then returns through a CDU. In a closed-loop cooling system, the fluid recirculates at the rack. The CDU transfers the captured heat into the facility-side cooling system while maintaining required temperature, flow, pressure, and fluid quality.

Schneider Electric White Paper 211 reports that direct-to-chip liquid cooling can reduce cooling energy use by up to 60% and water use by up to 60% in appropriate applications, though actual results depend on operating temperature, facility design, climate, and heat-rejection strategy.

Site water consumption depends heavily on what happens next. Dry coolers and air-cooled chillers can minimize routine onsite cooling-water consumption by rejecting heat to ambient air. Cooling towers require makeup water for evaporation and blowdown. Hybrid and adiabatic systems use water selectively, with annual and peak-day use influenced by climate, controls, and thermal set points. Site-level water consumption varies with climate, load, operating temperature, heat-rejection design, and local conditions.

Those options involve trade-offs beyond water use. Cooling towers can deliver strong thermal efficiency but consume more water; dry coolers minimize water use but rely more heavily on fans, which can increase energy use and noise; and adiabatic systems sit between those approaches, improving efficiency while still using some water. Noise mitigation measures such as lower-speed fans and acoustic enclosures can reduce community impacts but may require more space or capital. Higher supply-water temperatures can improve efficiency and heat-rejection flexibility but must remain within equipment and operating constraints. Rather than optimizing for a single metric, design teams need to balance water use, noise, energy efficiency, footprint, and cost against site-specific conditions and permitting requirements.

Developers and design teams should document water source, annual and peak-day demand, drought operating modes, blowdown, discharge, and reuse early enough to inform equipment selection and permitting.

## Mitigating data center community opposition with cooling architecture

Moving more heat through liquid can reduce dependence on high-velocity air movement inside the data hall. Outdoor heat rejection still creates acoustic sources that may include dry coolers, chillers, cooling towers, pumps, compressors, and large fan arrays.

Different liquid-cooling architectures shift those sources rather than removing them. Heat Dissipation Units (HDUs), for example, can support liquid-cooled IT where building water is unavailable by rejecting heat to air, which keeps fans in the acoustic model. Rear-door heat exchangers (RDHx) can reduce room-level air-cooling demand in some configurations, while the broader facility cooling system remains part of the site analysis.

Some U.S. jurisdictions are also examining sound beyond a single dBA value. Prince William County, Virginia, added C-weighted limits for steady tonal equipment sound after identifying low-frequency sound as a concern. Fairfax County requires data center noise studies at multiple stages of approval. These are local examples, rather than national requirements.

Depending on the jurisdiction, acoustic modeling may need to address nighttime operation, tonal or octave-band characteristics, maximum fan and compressor duty, nearby sensitive receptors, and cumulative campus phases. If approval depends on low-noise fans, variable-speed controls, equipment orientation, enclosures, or setbacks, those requirements should carry through procurement and commissioning.

## Carry permitting assumptions into specifications and commissioning

Local approval may occur early in development, while the design continues to change through procurement and construction. That creates a handoff risk amid potential data center community opposition.

If a water study assumes a particular heat-rejection architecture, an equipment substitution can change peak-day consumption or discharge. If an acoustic model depends on fan selection, orientation, setbacks, or enclosures, later value engineering can affect the basis of approval.

Developers, consulting engineers, specifiers, contractors, and suppliers should carry those assumptions into measurable requirements. Before equipment is finalized, teams should establish:

- annual and peak-day water assumptions, including drought operating modes where relevant
- acoustic criteria based on worst-case operating conditions and intended campus buildout
- equipment and control requirements needed to meet those criteria
- commissioning and monitoring methods that verify installed performance

Campus-scale developments deserve particular attention because early phases may represent only a fraction of the eventual cooling load. Water and acoustic analysis should reflect planned buildout where local review requires it.

Prefabricated modular pods can support more repeatable coordination between power and cooling systems, especially where multiple phases or standardized deployments are planned. Their role is design consistency and coordination; local approval still depends on the specific site and jurisdiction. For ecosystem partners, permit-related criteria should be treated like any other design requirement: documented, specified, commissioned, and preserved through handover.

## Cooling design belongs in the approval strategy

Data center community opposition can involve power availability, grid impacts, on-site generation, land use, taxes, visual impact, property concerns, and local trust. Water and noise are among the impacts that cooling architecture can directly influence. As AI workloads increase power demand, cooling and power planning become tightly linked considerations in the broader approval process. That makes the full thermal path a useful planning tool: how heat moves from the chip through the facility, how it reaches the outdoors, how much water the system uses, and what acoustic profile it creates under real operating conditions.

Schneider Electric’s comprehensive, end-to-end liquid cooling portfolio, including Motivair by Schneider Electric, spans direct-to-chip heat capture, CDUs, heat dissipation, chillers, and heat rejection. That system-level perspective can help teams evaluate cooling alongside site constraints and permitting requirements. Explore Schneider Electric’s Liquid Cooling solutions and guide to Liquid Cooling Architectures to learn how to plan a cooling architecture that can support higher-density workloads, existing-facility constraints, and evolving resource requirements.

## Add a comment Cancel reply

## Top picks

![](img)

## Congratulations to our 2019 Master-level Critical Power EcoXpert™ Partners

![](img)

## Wired for more: Stories from electricians around the world (part 2)

![](img)

## Liquid cooling fluid management: How to protect AI infrastructure

![](img)

## Partnerships for Innovation: Building the next generation of electrical distribution