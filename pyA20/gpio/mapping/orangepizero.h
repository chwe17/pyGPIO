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
pin header (26pin 'model A') looks like the following:

								3.3V	|··|	5V
(PA12, TWI0_SDA)				GPIO2	|··|	5V
(PA11, TWI0_SCK)				GPIO3	|··|	GND
(PA6, PMW1)						GPIO4	|··|	GPIO14	(PG6, UART1_TX)
								GND		|··|	GPIO15	(PG7, UART1_RX)
(PA1, UART2_RX)					GPIO17	|··|	GPIO18	(PA7)
(PA0, UART2_TX)					GPIO27	|··|	GND
(PA2, UART2_CTS)				GPIO22	|··|	GPIO23	(PA19, TWI1_SDA)
								3.3V	|··|	GPIO24	(PA18, TWI1 SCK)
(PA15, SPI1_MOSI, UART3_RTS)	GPIO10	|··|	GND
(PA16, SPI1_MISO, UART3_CTS)	GPIO9	|··|	GPIO25	(PA2, UART2_RTS)
(PA14, SPI1_CLK)				GPIO11	|··|	GPIO8	(PA13, SPI1_CS, UART3_TX)
								GND		|··|	GPIO7	(PA10)

*/  
	{"GPIO",
		{
			//'first row'
			{   "PA12",  SUNXI_GPA(12),  2   },
			{   "PA11",  SUNXI_GPA(11),  3   },
			{   "PA6",  SUNXI_GPA(),6  4   },
			{   "PA1",  SUNXI_GPA(1),  17   },
			{   "PA0",  SUNXI_GPA(0),  27   },
			{   "PA2",  SUNXI_GPA(2),  22   },
			{   "PA15",  SUNXI_GPA(15),  10  },
			{   "PA16",  SUNXI_GPA(16),  9  },
			{   "PA14",  SUNXI_GPA(14),  11  },
			//'second row'
			{   "PG6",  SUNXI_GPG(6),  14  },	
			{   "PG7",  SUNXI_GPG(7),  15  },
			{   "PA7",  SUNXI_GPA(7),  18  },
			{   "PA19",  SUNXI_GPA(19),  23  },
			{   "PA18",  SUNXI_GPA(18),  24  },
			{   "PA2",  SUNXI_GPA(2),  25  },
			{   "PA13",  SUNXI_GPA(13),  8   },
			{   "PA10",  SUNXI_GPA(10),  7   },
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
			{   "STATUS_LED",  SUNXI_GPA(17),  2   },
			{
				{   0,  0,  0}
			},
		}
	},
};



#endif