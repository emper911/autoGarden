#Author: Rikitaro Suzuki
#Date: July 10th, 2018. Wednesday
#Description: 
This project is to develop code that can control the production of agricultural produce in hydroponic systems.
Requires needing to define specific variables for inputs (sensors) and outputs (controls) that can be used to monitor plant growth.
Would like to connect systems to the cloud and process data through agrigrating hydroponic IoTs and improve output levels from input history.

Could you decentralize this process? the data set will most likely be centralized and completely open. 
Could you token this? Possibly? ... Maybe exchanging tokens for work of processing information with their own personal computing power?
Or paid through personal ownership of a hydroponic system connected by an API submitting information, or being part of the experiment.
Able to buy food with this token? I dunno probably not. 

Plan:
 - Scopes:
    - Individual System:
        - A hydroponic timing system that runs on a schedule for the specific crop. 
        - Variables:
            - Light : set timing of ON/OFF or varying levels on a 24hr cycle and following the life cycle of the plant. 
                      Could also add further control with RGB LEDs.
            - Motor : set timing of pump and possibly change over the course of the life cycle. Possibly not must do further research.
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
    
        - Scheduling:
            Should be dynamic, however, have an ability to apply weights and drive plant life cycle. Thresholds and equillibrium range
            Will most likely be the thing that changes. However, dynamic aspects would be to see individual through possibly photos and inspect
            the health of the plant. Afterwords set the rate at which thresholds change at rate that reflects healthly plant growth. 
        
        - Should send info to a central server and receieve suggested schedule changes for better plant growth. 


    - Connecting System to Cloud:
        - Retrieve data from multiple hydroponic systems through a REST API that allows for communication. 
        - Develop generalized schedule for a specific plant species that would meet requiresments of good, edible food. 
        - Be able to create schedules for specific scales of operations. must know certain dimesnsions and rates of change. 


"""