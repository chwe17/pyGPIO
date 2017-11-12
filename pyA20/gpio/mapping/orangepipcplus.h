/*
 *
 * This file is part of pyA20.
 * mapping.h is python GPIO extension.
 *
 * Copyright (c) 2014 Stefan Mavrodiev @ OLIMEX LTD, <support@olimex.com>
 *
 * pyA20 is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 *
 * mapping.h from: https://github.com/wdmomoxx/orangepi_ZERO_gpio_pyH2
 *
 */

#ifndef __MAPPING_H
#define __MAPPING_H

#include "gpio_lib.h"

/**
Structure that describe all gpio
*/
typedef struct _pin {
	char name[10];          // The processor pin
	int offset;             // Memory offset for the pin
	int pin_number;         // Number on the connector
}pin_t;

typedef struct _gpio {
	char connector_name[10];
	pin_t pins[41];
}gpio_t;


gpio_t gpio[] = {

/*
Description of Pinheader, please don't change pinnumer to keep this library consistent! A 'RPi compatible'
pin header (40pin) looks like the following:

								3.3V	|··|	5V
(PA12, TWI0_SDA)				GPIO2	|··|	5V
(PA11, TWI0_SCK)				GPIO3	|··|	GND
(PA6, PMW1)						GPIO4	|··|	GPIO14	(PA13, UART3_TX)
								GND		|··|	GPIO15	(PA14, UART3_RX)
(PA1, UART2_RX)					GPIO17	|··|	GPIO18	(PD14)
(PA0, UART2_TX)					GPIO27	|··|	GND
(PA3, UART2_CTS)				GPIO22	|··|	GPIO23	(PC4,)
								3.3V	|··|	GPIO24	(PC7,)
(PC0, SPI0_MOSI)				GPIO10	|··|	GND
(PC1, SPI0_MISO)				GPIO9	|··|	GPIO25	(PA2, UART2_RTS)
(PC2, SPI0_CLK)					GPIO11	|··|	GPIO8	(PC3, SPI0_CS0)
								GND		|··|	GPIO7	(PA21)
(PA19, TWI1_SDA)				GPIO28*	|··|	GPIO29*	(PA18, TWI1_SCK)
(PA7)							GPIO5	|··|	GND
(PA8)							GPIO6	|··|	GPIO12	(PG8, UART1_RTS)
(PA9)							GPIO13	|··|	GND
(PA10)							GPIO19	|··|	GPIO16	(PG9, UART1_CTS)
(PA20)							GPIO26	|··|	GPIO20	(PG6, UART1_TX)
								GND		|··|	GPIO21	(PG7, UART1_RX)
								

(*) on the RPi those two pins are used for official HATS (read out eeprom), since this is never depoyed 
on SUNXI boards we can use this GPIOs too. ;)
 
*/  
	{"GPIO",
		{
			//'first row'
			{   "PA12",  SUNXI_GPA(12),  2   },
			{   "PA11",  SUNXI_GPA(11),  3   },
			{   "PA6",  SUNXI_GPA(6),  4   },
			{   "PA1",  SUNXI_GPA(1),  17  },
			{   "PA0",  SUNXI_GPA(0),  27  },
			{   "PA3",  SUNXI_GPA(3),  22  },
			{   "PC0",  SUNXI_GPC(0),  10  },
			{   "PC1",  SUNXI_GPC(1),  9   },
			{   "PC2",  SUNXI_GPC(2),  11  },
			{   "PA19",  SUNXI_GPA(19), 28   },
			{   "PA7",  SUNXI_GPA(7),  5   },
			{   "PA8",  SUNXI_GPA(8),  6  },
			{   "PA9",  SUNXI_GPA(9),  13  },
			{   "PA10",  SUNXI_GPA(10),  19  },
			{   "PA20",  SUNXI_GPA(20),  26  },
			//'second row'
			{   "PA13",  SUNXI_GPA(13),  14  },	
			{   "PA14",  SUNXI_GPA(14),  15  },
			{   "PD14",  SUNXI_GPD(14),  18  },
			{   "PC4",  SUNXI_GPC(4),  23  },
			{   "PC7",  SUNXI_GPC(7),  24  },
			{   "PA2",  SUNXI_GPA(2),  25  },
			{   "PC3",  SUNXI_GPC(3),  8   },
			{   "PA21",  SUNXI_GPA(21),  7   },
			{   "PA18",  SUNXI_GPA(18),  29   },
			{   "PG8",  SUNXI_GPG(8),  12  },
			{   "PG9",  SUNXI_GPG(9),  16  },
			{   "PG6",  SUNXI_GPG(6),  20  },
			{   "PG7",  SUNXI_GPG(7),  21  },
			{
				{   0,  0,  0}
			},
		}
		},
  /*
    #define PIN_PG0		SUNXI_GPG(0)
*/
	{"LED",
		{
			{   "POWER_LED",  SUNXI_GPL(10),  1   },
			{   "STATUS_LED",  SUNXI_GPA(15),  2   },
			{
				{   0,  0,  0}
			},
		}
	},
};