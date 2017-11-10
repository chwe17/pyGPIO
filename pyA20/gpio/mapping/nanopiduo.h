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
    #define PIN_PG0		SUNXI_GPG(0)
*/  {"J1",
        {
            {   "PA4",  SUNXI_GPA(4),  2   },
            {   "PA5",  SUNXI_GPA(5),  1   },
            {   "PA11",  SUNXI_GPA(11),  4   },
            {   "PA12",  SUNXI_GPA(12),  5   },
            {   "PA13",  SUNXI_GPA(13),  6   },
            {   "PA14",  SUNXI_GPA(14),  7  },
            {   "PA15",  SUNXI_GPA(15),  9  },
            {   "PA16",  SUNXI_GPA(16),  8  },
			{   "PG6",  SUNXI_GPG(6),  11  },
            {   "PG7",  SUNXI_GPG(7),  10  },
            {
                {   0,  0,  0}
            },
        }
    },
	{"J2",
        {
            {   "PG11",  SUNXI_GPG(11),  6   },
            {   "PL11",  SUNXI_GPL(11),  5   },
            {
                {   0,  0,  0}
            },
        }
    },	

/*
    #define PIN_PG0		SUNXI_GPG(0)
*/  {"LED",
        {
            {   "POWER_LED",  SUNXI_GPL(9),  1   },
            {   "STATUS_LED",  SUNXI_GPA(10),  2   },
            {
                {   0,  0,  0}
            },
        }
    },
};



#endif