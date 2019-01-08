##AutoGarden
- Author: Rikitaro Suzuki.
- Project Start Date: May 8th, 2016.
- Date: July 10th, 2018.
- Modified: January 8th, 2019.
- Description: 
  -  This project is to develop code that can control the production of produce through individual hydroponic systems.  
     Throughout the world physical geographic conditions limit different communities and their ability to grow specific crops 
     and produce, vital to the nutrition of adults and children. This is observed in desert climates, as well as changing 
     arctic climates in places such as Northern Territories of Canada. Through digitally controlled hydroponic systems built 
     with sustainable technology, it may be possible to overcome these circumstances. Not taken into account of this project 
     is the economic cost of doing so, as well as the willingness of local communities to adopt, such a method as they may 
     prefer other solutions. Progress made so far is a working individual unit that needs major refinements. 
     
     The end goal is to connect systems to the cloud and process data through aggregating hydroponic unit data and improve 
     output levels of these units from input history. This information can be processed and adjust controls of the plants to 
     suite the needs of the individual plant, as well as possibly taking into account physical geographic conditions of where 
     the unit is situated. 

     To effectively create a solution, it is required to define specific variables for inputs (sensors) and outputs (controls) 
     that can be used to monitor and respond to plant growth.

##General Overview:
 - Scopes:
    - Individual System 1.0:
        - Ideally a hydroponic timing system that runs on a schedule for the specific crop. 
        - Variables:
            - Light : set timing of ON/OFF or varying levels on a 24hr cycle and following the life cycle of the plant. 
                      Could also add further control with RGB LEDs.
            - Motor : set timing of pump and possibly change over the course of the life cycle. Possibly not, must do further 
                      research.
            - Fan : Turn on at specific intervals in the day to strengthen plants. 
            - Temperature : 
                INPUT: read sensor data that is optimally placed to get accurate readings of temperature. 
                OUTPUT: respond to INPUT when sensor readings go below a specific threshold. 
                        Must know the rate at which output control heats the space to reach equillibrium. 
            - Humidity :
                INPUT: read sensor data that is optimally placed to get accurate readings of humidity. 
                OUTPUT: respond to INPUT when sensor readings go below a specific threshold. 
                        Must know the rate at which output control humidifies the space to reach equillibrium. 
            - CO2 :
                INPUT: read sensor data that is optimally placed to get accurate readings of CO2. 
                OUTPUT: respond to INPUT when sensor readings go below a specific threshold. 
                        Must know the rate at which output control adds CO2 to the space to reach equillibrium. 
            - Nutrient Ratios : Process should be able to appropriately add hydroponic nutrients to the water resevoir.
                                In addition system should be able to flush past liquid solutions through a draining mechanism.
                                A possible solution may be to use an idea such as a printing cartridge for the users'     
                                conveinece. 
    
        - Scheduling:
            Should be dynamic, however, have an ability to apply weights and drive plant life cycle. Thresholds and 
            equillibrium range
            Will most likely be the thing that changes. However, dynamic aspects would be to see individual through possibly 
            photos and inspect
            the health of the plant. Afterwords set the rate at which thresholds change at rate that reflects healthly plant 
            growth. 
        
        - Should send info to a central server and receieve suggested schedule changes for better plant growth. 
        - An ideal IoT device may be the combination of a Raspberry Pi and Arduino, as the arduino can read analog input   
          information and a Raspberry Pi can be used as a linux system to connect with the server.
          - Cost of making such a device is high, however, a workable unit is the priority and refinement will be done to 
            optimize for cost.

    - Connecting System to Cloud:
        - Retrieve data from multiple hydroponic systems through a REST API that allows for communication. 
        - Develop generalized schedule for a specific plant species that would meet requiresments of good, edible food. 
        - Be able to create schedules for specific scales of operations. must know certain dimesnsions and rates of change. 
