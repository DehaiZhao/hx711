This is weight server running on raspberrypi.

How to use them:

1.To start the service in background, please run:
'nohup python weight_server.py >/dev/null 2>&1 &'
Here is a script 'start.sh' to start this service
conveniently.

2.To revise weight coefficients, please firstly
clean all the boxes, modify 'config.py' and set
'unit = [1,1,1,1,1,1,1,1,1]', then restart weight
service and run: 'python weight_regression.py'. 
You can follow the guides to put weights in boxes.
If you only want to modify a specified
channel, just add channel after the script. Here
takes channel 3 for example:
'python weight_regression.py 3'. Note that the
first channel is channel 0.

3.To revise temperature linear drift coefficients,
please firstly clean all the boxes and run:
'python temperature_regression.py'. Then you could
do nothing but wait for over 12 hours until the 
sensors collect enough data to regress accurate
coefficient. Note that during this process, do not
touch any box and just leave the shelf alone, do 
not intensively keep environment temperature too
stable, or you could not get good results.

4.The coefficients revised by stpe2 and step3
would be saved as 'config_n.py'. Every time after
you revise coefficients, please check if the
modifications are OK. If you think they are OK,
Then you can run 'copy config_n.py config.py'
to replace configuration file. Note that you should
restart weight service after updating configuration.

5.Generally, revision steps only happen during
distribution process. Once you complete the step
above, raspberry pi would provide stable service.
If you think the data is not accurate enough, please
firstly check hardware then do step2 to step4.

Description of each file is as follows:

1.'config.py': Configuration of import parameters,
in which 'Channels' are pins on raspberrypi in BCM
mode. They are chosen by circuit design and should
be selected manually. Please refer to 'pin.jpg'. 
'unit' are weight coefficients and 'temperature_offset' 
are temperature linear drift coefficients. Both of 
them would be revised by program automatically.

2.'hx711.py': HX711 AD chip library. Genearlly, it
 should not be modified.

3.'tempearture.py': DS18B20 temperature chip library. 
Generally, it should not be modified. Before using 
it, please run 'sudo pip install w1thermsensor'.

4.'temperature_regression.py': Revise temperature
linear drift coefficients automatically. 

5.'weight_server.py': Collect all the data from sensors
and put them on websit using flask.

6.'sensors.py': Read data from weight sensors and
temperature sensors.

7.'weight_regression.py': Revise weight unit
coefficients.
