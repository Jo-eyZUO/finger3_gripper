// Float voltage control version

#include <Wire.h>
#include "MCP4728.h"

char control_name;
int flag = 0;
float float_b = 1.0;
float float_c = 1.0;
float float_d = 1.0;
MCP4728 dac;

void setup()
{
    Serial.begin(9600);  // initialize serial interface for print()
    Wire.begin();
    dac.attach(Wire, 14);
    dac.readRegisters();
    dac.selectVref(MCP4728::VREF::VDD, MCP4728::VREF::VDD, MCP4728::VREF::INTERNAL_2_8V, MCP4728::VREF::INTERNAL_2_8V);
    dac.selectPowerDown(MCP4728::PWR_DOWN::GND_100KOHM, MCP4728::PWR_DOWN::GND_100KOHM, MCP4728::PWR_DOWN::GND_500KOHM, MCP4728::PWR_DOWN::GND_500KOHM);
    dac.selectGain(MCP4728::GAIN::X1, MCP4728::GAIN::X1, MCP4728::GAIN::X2, MCP4728::GAIN::X2);
    dac.enable(true);
    dac.readRegisters();
//    printStatus();
    delay(100);
}

void loop()
{
   if (Serial.available())
   {
      control_name = Serial.read();
      if (control_name != '\n')
      {
        Serial.print("Controling name: ");
        Serial.println(control_name);
      }
      
      // vol = Serial.readStringUntil('\n');
      // Serial.print("Voltage value: ");
      // Serial.println(vol);

      switch(control_name)
      {
      case 'o':
          flag = 0;
          break;
      case 'c':
          flag = 1;
          break;
      case '\n':
          break;
      default:
          Serial.println("Wrong Input!");
          break;  
      }
   }
//   dac.analogWrite(MCP4728::DAC_CH::A, 5000*4/5.0); 4 but 1.27
  if (flag == 1)
  {
   dac.analogWrite(MCP4728::DAC_CH::B, 4000);
   dac.analogWrite(MCP4728::DAC_CH::C, 4000);
   dac.analogWrite(MCP4728::DAC_CH::D, 4000);
  }
  else 
  {
   dac.analogWrite(MCP4728::DAC_CH::B, 0);
   dac.analogWrite(MCP4728::DAC_CH::C, 0);
   dac.analogWrite(MCP4728::DAC_CH::D, 0);
  }
}     
