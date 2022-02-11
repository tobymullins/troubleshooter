def  engine_start():
     does_it_start = input("Does the engine start now?")
     if does_it_start == "yes":
          quit("Thank you for using Troubleshooter")
     else:
          return

def cylinder_compression():
     print("Perform a cylinder compression test.")
     cyl_comp = input("What is the cylinder compression in PSI?")
     if cyl_comp <= 70:
          print("Cylinder compression is within specifications")
          return
     elif cyl_comp > "100":
          print("Cylinder compression is too high. Check the valve clearance and perform the cylinder compression test again. If compression is still high, remove carbon deposits from the combustion chamber and check the decompressor operation of the camshaft.")
          engine_start()
     else:
          print("Cylinder compression is too low. Perform a leak down test to determine where the cylinder is losing compression. Repair as needed.")
          engine_start()

def ignition_system():
     print("Check the oil level switch and the oil alert unit.")
     oil_switch = input("Is the oil level switch good?")
     if oil_switch == "yes":
          print("Check for continuity between the ignition coil wire connectors.")
          coil_wire = input("Is there continuity?")
          if coil_wire == "yes":
               print("Check the engine stop switch.")
               is_switch_good = input("Is the switch good?")
               if is_switch_good == "yes":
                    print("Check the ignition coil.")
                    ignition_coil = input("Is the ignition coil good?")
                    if ignition_coil == "yes":
                         print("Check the spark plug cap and replace if necessary.")
                         engine_start()
                    else:
                         print("Replace the ignition coil.")
                         engine_start()
               else:
                    print("Replace the stop switch.")
                    engine_start()
          else:
               print("Replace the ignition coil wire.")
               engine_start()
     else:
          print("Replace the oil level switch or oil alert unit.") 
          engine_start() 


def starter_non_op():
     print("Starter motor does not operate.")
     print("Check the battery voltage.")
     batt_voltage = input("Enter the battery voltage:")
     if batt_voltage < "12.0":
          print("Replace with a known good battery.")
          engine_start()
     else:
          print("Check the fuse.")
          is_fuse_good = input("Is the fuse good?")
          if is_fuse_good == "yes":
               print("Check the combination switch.")
               is_switch_good = input("Is the switch good?")
               if is_switch_good == "yes":
                    print("Check the starter solenoid.")
                    starter_solenoid = input("Is the starter solenoid good?")
                    if starter_solenoid == "yes":
                         print("Check the wire harness for shorts or open circuits.")
                         wire_harness = input("Is the wire harness good?")
                         if wire_harness == "yes":
                              engine_start()
                         else:
                              print("Replace or repair the wire harness.")
                              engine_start() 
                    else:
                         print("Replace the starter solenoid.")
                         engine_start()
               else:
                    print("Replace the switch.")
                    engine_start()
          else:
               print("Replace the fuse.")
               engine_start()
               
def no_crank():
     print("Engine does not crank.")
     print("Remove the recoil starter and check whether the engine cranks.")
     does_crank = input("Does the engine crank?")
     if does_crank == "yes":
          print("Inspect the recoil starter.")
          print("Replace the faulty parts.")
          engine_start()
     else:
          starter_non_op()

def cranks_but_no_start():
     print("Engine cranks but will not start.")
     print("Loosen the carburetor drain screw and check the fuel flow from the fuel tank.")
     has_fuel = input("Does fuel flow from the carburetor?")
     if has_fuel == "yes":
          print("Perform a spark test.")
          has_spark = input("Is there spark?")
          if has_spark == "yes":
               cylinder_compression()
               print("Check the spark plug.")
               spark_plug = input("Is the spark plug wet or dry?")
               if spark_plug == "wet":
                    print("If the spark plug is correct, clean and dry the electrode and try to start the engine again, taking care that the choke valve is not closed. If tbhe engine does not start, and the electrodes are wet again, check the carburetor float.")
                    engine_start()
          else:
               print("Troubleshoot the ignition system.")
               ignition_system()
     else:
          print("Check for clogged fuel filter, fuel tank joint, fuel tube, or cup filter.")
          engine_start()

def engine_speed_no_increase_or_stabilize():
     print("Engine speed does not increase or stabilize")
     print("Check the air filter element.")
     air_filter = input("Is the air filter clean?")
     if air_filter == "yes":
          print("Check the valve clearance. If needed, adjust to .006 inches for the intake and .008 inches for the exhaust.")
          valve_clearance = input("Did the valves need to be adjusted?")
          if valve_clearance == "yes":
               engine_start()
          else:
               print("Check the spark plug.")
               spark_plug = input("Is the spark plug in good condition?")
               if spark_plug == "yes":
                    print("Check the carburetor for any blockage.")
                    carb_blockage = input("Is the carburetor clean?")
                    if carb_blockage == "yes":
                         print("Disassemble and clean the carburetor.")
                         engine_start()
                    else:
                         print("Check for secondary air leak")
                         air_leaking = input("Is air leaking?")
                         if air_leaking == "yes":
                              print("replace the insulator and/or carburetor gaskets.")
                              engine_start()
                         else:
                              print("Check cylinder compression.")
                              cylinder_compression()
                         print("Check if the governor system is installed correctly.")
                         governor_system = input("Is the governor system installed correctly?")
                         if governor_system == "yes":
                              print("Check the ignition coil air gap.")
                              ignition_air_gap = input("Is the air gap correct?")
                              if ignition_air_gap == "yes":
                                   print("Check the ignition coil.")
                                   ignition_system()
                              else:
                                   print("Adjust the ignition coil air gap.")
                                   engine_start()
                         else:
                              print("Replace the faulty parts.")
                              engine_start()

               else:
                    print("Replace the spark plug.")
                    engine_start()
     else:
          print("Clean or replace the air filter.")
          engine_start()

def engine_no_stop():
     print("Engine does not stop when combination/engine stop switch is turned off.")
     print("Check the engine stop switch.")
     engine_switch = input("Is the engine stop switch functional?")
     if engine_switch == "yes":
          print("Check the wire harness between the engine stop switch and the ignition coil for open or short circuit.")
          short_circuit = input("Is there an open or short circuit?")
          if short_circuit == "yes":
               print("Replace or repair the wire harness.")
               engine_start()
          else:
               print("Check the ignition coil and replace if needed.")
               engine_start()
     else:
          print("Replace the engine stop switch.")
          engine_start()
print("Welcome to the Honda engines Troubleshooter terminal program.") 
print("This program assumes you have a working knowledge of basic four stroke engine theory.")

will_continue = input("Would you like to proceed?")
if will_continue == "yes":
     print("Great! Then let's get started")
else:
     quit("Thank you for using Troubleshooter.")
a = "a. Engine will not crank."
b = "b. Engine cranks but will not start."
c = "c. Engine speed does not increase or stabilize."
d = "d. Engine does not stop when combination/engine stop switch is turned  off." 

def choose_option():
     choose_option = input("Please choose the option that best describes your problem:")
     if choose_option == "a":
          no_crank()
     elif choose_option == "b":
          cranks_but_no_start()
     elif choose_option == "c":
          engine_speed_no_increase_or_stabilize()
     elif choose_option == "d":
          engine_no_stop()
     else:
          print("Invalid input")
          return

print(a)
print(b)
print(c)
print(d)

choose_option()




