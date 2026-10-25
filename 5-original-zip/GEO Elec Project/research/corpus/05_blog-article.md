<!-- Blog article | Using treated and recycled water in Indian data centre cooling | https://blog.se.com/datacenter/2026/09/29/using-treated-and-recycled-water-in-indian-data-centre-cooling/ -->
<!-- html_title: Using treated and recycled water in Indian data centre cooling - Schneider Electric Blog | meta: {"description": "Discover how data centre water recycling and closed-loop liquid cooling can help Indian data centres reduce freshwater use and support overall water resilience.", "og:title": "Using treated and recycled water in Indian data centre cooling", "og:description": "Discover how data centre water recycling and closed-loop liquid cooling can help Indian data centres reduce freshwater use and support overall water resilience.", "article:published_time": "2026-09-29T04:30:00+00:00", "article:modified_time": "2026-10-02T07:34:54+00:00", "author": "Guest Blogger", "time_elements": ["2026-09-29T00:30:00-0400"]} | jsonld: ['Article', 'BreadcrumbList', 'CommentAction', 'EntryPoint', 'ImageObject', 'ListItem', 'Person', 'PropertyValueSpecification', 'ReadAction', 'SearchAction', 'WebPage', 'WebSite'] -->

Data Centers

# Using treated and recycled water in Indian data centre cooling

- September 29, 2026
- 173 views
- 6 min read
- Guest Blogger

Author: Anuj Kudesia, Managing Director SEPSL & Direct BD

Summary

- Water availability is becoming an infrastructure constraint for India’s data centre growth. Site selection and cooling design increasingly need to account for local water availability, source, quality, and long-term resilience.
- Liquid cooling can use more liquid while consuming less water. Closed-loop direct-to-chip systems recirculate coolant rather than continually losing water through evaporation, helping reduce consumptive demand.
- Recycled water only solves part of the problem. Operators should first reduce overall water demand, then determine how appropriately treated wastewater, greywater, or other non-potable sources can meet the remaining requirement.
- Cooling and water strategy should be designed together from day one. Water quality, heat rejection, coolant temperatures, future rack density, treatment requirements, and water source all influence the right thermal architectu

India has around 18% of the world’s population but only 4% of its freshwater resources. This makes data centre water recycling more than a sustainability metric. Its availability, source, and quality can influence site selection, cooling architecture, and long-term resilience.

Substituting recycled water for freshwater in an unchanged cooling system addresses only part of the problem. A stronger approach is to reduce consumptive water demand first, then use appropriately treated and recycled water for the remaining requirements. Closed-loop liquid cooling is ideal for this model.

## Why water availability constrains infrastructure

Around 75% of India’s data centre facilities are concentrated in Maharashtra, Tamil Nadu, Karnataka, Telangana and Uttar Pradesh, with many located in areas experiencing high or extremely high water stress.

This tension is already visible locally, where water availability can affect project viability and social license to operate. For architects, MEP consultants, specifiers, and contractors, water sourcing should be considered in conjunction with power availability, thermal loads, and heat rejection during early facility design.

Higher compute density does not have to mean higher freshwater consumption. Much depends on the cooling architecture. Design teams should ask three questions:

- How much water does the cooling system actually consume?
- Where will that water come from?
- How can dependence on potable freshwater be reduced from the outset?

## The data centre water recycling paradox: More liquid can mean less water consumption

“Liquid cooling” can create a misleading impression: if more liquid is used to cool IT equipment, the data centre must consume more water. The important distinction is between liquid circulating through a cooling system and water being consumed by it.

Evaporative cooling rejects heat by evaporating water into the atmosphere, creating an ongoing requirement for replacement water. Closed-loop direct-to-chip cooling works differently. Coolant passes through cold plates attached to GPUs and CPUs, absorbs heat, and recirculates through the system.

Closed-loop liquid cooling can recirculate more than 95% of its coolant, with relatively small losses associated with maintenance or leaks. Direct-to-chip systems can also operate at higher supply and return temperatures, which, depending on facility design and local conditions, can reduce reliance on deep mechanical chilling and expand heat-rejection options that use less or no evaporative water.

Mixed-density facilities may use both air and liquid cooling. Rather than simply choosing between the two, it is critical to consider how the overall thermal architecture can meet increasing cooling requirements while minimizing consumptive water use.

## Data centre water recycling requires the right water source

Once consumptive demand has been reduced, the next question is whether the remaining water requirements need to rely on potable freshwater. Treated municipal wastewater is one increasingly relevant alternative. AWS, for example, has announced plans to use treated sewage water instead of drinking water at upcoming data centre sites in Mumbai and Hyderabad. Depending on the site, operators may also evaluate on-site treated wastewater or greywater and rainwater harvesting.

The appropriate source for data centre water recycling depends on local availability, reliability, water quality, and the cooling architecture. Crucially, treated water is not automatically ready for cooling.

![Waste water treatment plant.](img)

### Recycled water has to be engineered for the cooling system

Water quality parameters such as total dissolved solids, hardness, and suspended solids must be controlled because they can contribute to scaling, fouling, and corrosion. Depending on incoming water quality and system requirements, additional treatment may include filtration, ultrafiltration, reverse osmosis, or other polishing processes.

Design teams should establish where reclaimed water will enter the thermal system, the water-quality requirements at that point, and how those conditions will be maintained over the facility lifecycle. Reduce consumptive demand first, then determine how much of the remaining requirement can be supplied from appropriately treated non-potable sources.

## India’s policy direction increasingly favours water reuse

National guidance and state policies increasingly favour greater data centre water recycling. The Bureau of Energy Efficiency’s 2023 District Cooling Guidelines encourage using treated wastewater instead of freshwater for cooling-tower makeup where feasible. State policies are also evolving: Rajasthan’s 2025 data centre policy incorporates wastewater recycling, zero liquid discharge (ZLD), rainwater harvesting and groundwater recharge.

Requirements for large water users are tightening as well. Rules introduced in 2025 require bulk users consuming more than 5,000 litres per day to increase wastewater treatment and reuse.

Design for the direction of water policy, not simply today’s minimum requirement. During site selection and early mechanical design, teams should consider treated-water availability, potential reuse requirements, and cooling-system water demand before the architecture is fixed.

## Go beyond WUE: measure where the water comes from

Water Usage Effectiveness (WUE) measures a data centre’s water consumption relative to the energy consumed by its IT equipment. It is a useful efficiency metric, but it does not distinguish between potable and recycled water.

Two facilities could therefore report the same WUE even if one relies primarily on drinking water and the other uses appropriately treated municipal wastewater. For data centre water recycling strategies, WUE should be considered alongside water source and consumptive use. Where practical, reporting can also distinguish consumptive water use from water or coolant circulating within closed loops.

## Design the complete cooling and water path

For Indian data centre projects, water strategy and cooling architecture should be designed together. Coolant temperatures, water quality, heat rejection, and future rack density all influence how much water a facility needs, where it can come from, and how it must be treated.

Look beyond individual cooling products to the complete thermal path. Depending on the application, this can include direct-to-chip accessories, Coolant Distribution Units (CDUs), Heat Dissipation Units (HDUs), and rear-door heat exchangers (RDHx), connected to appropriate chillers and heat-rejection infrastructure on the facility side. Prefabricated modular IT pods can also support projects where a modular deployment approach is appropriate.

Not every facility needs every technology. Select an architecture that supports the required densities while controlling energy use, consumptive water demand, and operational complexity.

Schneider Electric offers a comprehensive, end-to-end liquid cooling portfolio that spans the thermal path, allowing cooling, water sourcing, and heat rejection to be considered as parts of the same system rather than separate equipment decisions.

## Make water sourcing a Day One cooling decision

India’s data centre sector must add computing capacity within significant water constraints. Effective data centre water recycling starts by reducing consumptive demand, not simply substituting recycled water into an unchanged cooling architecture. A stronger strategy follows these steps:

- Reduce consumptive water demand
- Identify appropriate non-potable sources
- Establish treatment requirements
- Design the cooling and heat-rejection architecture accordingly
- Measure both water consumption and water source

Schneider Electric’s Liquid Cooling Hub provides more detail on comprehensive thermal architectures. For a closer look at how to select and design the right system for your facility, download the Liquid Cooling System Architecture Guide.

## Add a comment Cancel reply

## Top picks

![](img)

## Powering the industrial comeback: Can America’s grid keep pace with the manufacturing resurgence and AI boom?

![](img)

## Closed-loop cooling data center strategies for the new wave of U.S. state water rules

![](img)

## Commercial Battery Energy Storage Systems: A strategic advantage for C&I businesses

![](img)

## Four accelerators of supply chain transformation in Europe