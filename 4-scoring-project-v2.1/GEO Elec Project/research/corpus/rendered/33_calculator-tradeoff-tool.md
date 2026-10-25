<!-- RENDERED | Calculator / TradeOff Tool | Data center power sizing calculator | https://www.se.com/ww/en/work/solutions/data-centers-and-networks/trade-off-tools/data-center-power-sizing-calculator/ -->
<!-- {"url": "https://www.se.com/ww/en/work/solutions/data-centers-and-networks/trade-off-tools/data-center-power-sizing-calculator/", "title": "Data center power sizing calculator | Schneider Electric", "h1": ["Data center power sizing calculator"], "words_visible": 423, "words_hidden": 1224, "repeated_blocks": 65, "repeated_words": 146} -->

# Data center power sizing calculator

Use this TradeOff Tool to estimate the power required by a data center with traditional, or AI/HPC servers. Configure different server, storage, and design attributes to explore different scenarios.

[iframe start]

[hidden] Go to Application Webpage

[hidden] About

[hidden] EcoStruxure

[hidden] Version 1.11

[hidden] Lorum ipsum

[hidden] This is an option

[hidden] Dividers

[hidden] Main layer

[hidden] Panel layer

[hidden] Nav layer

[hidden] Accessory layer

[hidden] Subsection panel

[hidden] Pop up layer

[hidden] Subtitle

[hidden] Section Title

[hidden] Kicker

[hidden] Slider

[hidden] Option 1

[hidden] Created with sketchtool.

[hidden] Standard

[hidden] Small

[hidden] Dropdown

[hidden] Enter text

[hidden] Text Input

[hidden] Value Input

[hidden] Radio button

[hidden] Checkbox

[hidden] Link

[hidden] Button

[hidden] Subdued button

[hidden] Emphasized button

[hidden] Standard button

[hidden] Tab 1

[hidden] Tab menu

[hidden] 100%

Allocation of input power

External storage: 7.2% (81 kW)

Networking: 4.2% (47 kW)

Mainframe: 0.9% (10 kW)

GPU servers: 9.3% (104 kW)

CPU servers: 38% (421 kW)

Safety margin: 12% (132 kW)

Physical infrastructure: 29% (320 kW)

Requirements

Data center IT capacity rating

790 kW

Utility input power

1,110 kW

Results

Safety margin for IT load

20%

Power usage effectiveness (PUE)

1.40

Design attributes

Mainframe quantity

100,000

External storage [TB]

Typical

CPU internal storage

Storage & mainframe

8+ CPU / GPU

90%

1-2 CPU / GPU

10%

4 CPU / GPU

Server mix

1,000

Traditional

AI / HPC

Server quantity

Servers

Inputs

[hidden] About this tool

[hidden] Learn more

[hidden] Assumptions

[hidden] Legal information

[hidden] Privacy policy

[hidden] Cookie notice

[hidden] Change your cookie settings

[hidden] The donut chart represents an itemized breakdown of the elements that make up the total required utility input power.

[hidden] – Is the total power required by the IT load.

[hidden] Utility input power – Is the required power to support the data center. Final projected loads should be used for sizing the utility input power. Note that the purpose of this tool is NOT to properly size the building’s utility power service entrance, since this tool does not account for electrical loads of the entire building, such as office space, restrooms, kitchens, etc.

[hidden] PUE (power usage effectiveness) is a common metric for measuring data center efficiency. PUE is the total power coming into the data center divided by the power going to the IT. Smaller PUE values indicate a more efficient data center.A PUE of 1.8 would be considered typical value.

[hidden] Click on the question mark at the top right corner to learn more about these metrics.

[hidden] The 'safety margin' is held in reserve above and beyond the as-configured load, as insurance against error in calculating the maximum load, or as insurance against the unauthorized addition of IT equipment. A value of 10-20% is typical.

[hidden] – The number of physical servers in the data center (as opposed to the number of virtual server images).

[hidden] Server mix – Describes the population of servers in the data center. These server groupings are differentiated and categorized by the number of CPU / GPU chips per server (and not by the number of 'cores'). The data should be presented as a percentage of the total servers in the data center.

[hidden] Traditional servers – Servers used for general purpose tasks, these employ CPUs only.

[hidden] AI / HPC servers – Servers with high performance computing capacity equiped with GPU accelerators in addition to CPUs.

[hidden] CPU internal storage – The data storage capacity installed on the CPU servers.

[hidden] External storage – The installed capacity of data storage external to CPU / GPU servers in terabytes (TB).

[hidden] Mainframe quantity – The number of mainframe servers. The tool considers these as separate from traditional and AI/HPC-based servers.

[hidden] PUE (power usage effectiveness) – Is a common metric for measuring data center efficiency. PUE is the total power coming into the data center divided by the power going to the IT. Smaller PUE values indicate a more efficient data center. A PUE of 1.4 would be considered typical value. Click on the 'Learn more' tab in the menu at the top right corner to learn more about these metrics.

[hidden] Safety margin for IT load – Held in reserve above and beyond the as-configured load, as insurance against error in calculating the maximum load, or as insurance against the unauthorized addition of IT equipment. A value of 10-20% is typical.

[hidden] SCHNEIDER ELECTRIC SHALL NOT BE LIABLE FOR YOUR USE OR ANY THIRD PARTY ACTING ON YOUR BEHALF OF THIS WEB TOOL OF ANY DATA YOU OR SUCH THIRD PARTY UPLOAD TO OR DOWNLOAD FROM THIS WEB TOOL OR CREATE OR MODIFY IN CONNECTION WITH THE USE OF THIS WEB TOOL, NOR FOR ANY DECISION, ACT OR OMISSION, SUCH AS BUT NOT LIMITED TO ANY ELECTRICAL ASSEMBLY, INSTALLATION OR MAINTENANCE, THAT YOU OR ANY THIRD-PARTY ACTING ON YOUR BEHALF MAY MAKE ON BASIS OF THE USE OF THIS WEB TOOL.

[hidden] The purpose of this tool is to define the basic characteristics of a data center's IT load and to calculate how much utility input power would be required to support such a load. The interactive nature of the tool allows the user to experiment with "what if" scenarios by modifying the characteristics of the load. Total load is then calculated and the tool generates a corresponding utility power requirement.

[hidden] TT1 Version 4 – 10-September-2024 – © 2024 by Schneider Electric

[hidden] Email the Data Center Science Center at dcsc@se.com with feedback or questions

[hidden] Contact Schneider Electric

[hidden] White Paper 158, Guidance for Calculation of Efficiency (PUE) in Data Centers

[hidden] White Paper 3, Calculating Total Power Requirements for Data Centers

[hidden] Related white papers & tools

[hidden] TradeOff Tools™ are based upon a series of mathematical models developed by the Schneider Electric Data Center Science Center. Fundamental research principles for development of these tools can be accessed via the Schneider Electric white paper library.

[hidden] Key assumptions of this calculator include:

[hidden] – Baseline CPU server (traditional) power draw is estimated at 290 watts/socket.

[hidden] – 'Low' CPU internal storage adds 6% of the CPU server power (equivalent to one drive), 'typical' adds 15% (equivalent to 2-3 drives), and 'high' adds 25% (equivalent to 6 drives).

[hidden] – GPU server (AI/HPC) power draw is estimated at 1,300 watts/socket. This is derived from NVIDIA H100 Hopper tensor cores, with 8 GPUs per server. This value includes power drawn within the server for internal storage and CPUs.

[hidden] – External storage power draw is estimated using a rate of 0.8 watts/TB, which is typical of external SSD drives in 2024. This value was derived from Dell PowerScale F910 All-Flash storage nodes.

[hidden] – Networking is estimated at 10% of the server power for CPUs, and 8.8% for GPUs. The GPU value was derived from the 127-node NVIDIA DGX SuperPOD Data Center Design.

[hidden] – Mainframe power is estimated to be 10,000 watts/mainframe.

[iframe end]

## Explore our related white papers, blogs, and solutions

- White papers

- Blogs

- Solutions

- Calculating total power requirements for data centers White paper 3 presents methods for calculating power and cooling requirements and provides guidelines for determining the total electrical power capacity needed to support the data center, including IT equipment, cooling equipment, lighting, and power backup. Learn more

- Guidance for calculation of efficiency (PUE) in data centers White paper 158 explains how to assess the data center efficiency (PUE) including what power consumptions to consider for each category (IT loads, physical infrastructure loads) in a standardized methodology. Discover more

- The AI disruption: Challenges and guidance for data center design White paper 110 explains relevant attributes and trends of AI workloads, and describes the resulting data center challenges, providing guidance to address these challenges for each physical infrastructure category including power, cooling, racks, and software management. Download now

[hidden] ### Data processing power is rising to incredible levels to enable AI

[hidden] AI servers require special accelerators that handle high data rates needed for AI model training and inference. These specialized servers enable new services and interactions that increase value to many businesses yet bring new challenges into the data center ecosystem.

[hidden] Read now

[hidden] ### Good decision making is crucial in data center planning: TradeOff Tools can help

[hidden] These interactive web-based calculators allow you to experiment with “what if” scenarios so you can estimate the impact on cost, reliability, electrical efficiency, carbon footprint, etc. They let you weigh your options, side by side, to make educated decisions based on real science, quickly and easily.

[hidden] Dive in

[hidden] ### Schneider Electric blogs

[hidden] Find expert perspectives on the trends and technologies driving your business.

[hidden] Check out now

[hidden] ### Data center reference designs

[hidden] Every data center project has its own unique requirements. Documented and validated reference designs facilitate discussions in the early planning phase and are a great starting point for detailed design work.

[hidden] Discover further

[hidden] ### Critical power for commercial and industrial

[hidden] Explore critical power solutions for various applications in commercial and industrial environments.

[hidden] Dive deeper

## Related TradeOff Tools

- Data center efficiency and PUE calculator See how alternative power and cooling systems impact energy costs and efficiency. Go to calculator

- Data center capacity and growth calculator See how power, cooling, and growth strategies impact data center design parameters. Start calculation

- TradeOff Tools library Interactive calculators that enable exploration of "what if" scenarios to achieve optimal results. Explore now

## Need help?

### Product Selector

Quickly and easily find the right products and accessories for your applications.

### Get a Quote

Start your sales inquiry online and an expert will connect with you.

### Where to buy?

Easily find the nearest Schneider Electric distributor in your location.

### Help Center

Find support resources for all your needs, in one place.

[iframe cross-origin]