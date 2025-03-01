#!/usr/bin/env python
'''
these tables are generated from the STM32 datasheet stm32wb55rg.pdf
'''

# additional build information for ChibiOS
build = {
    "CHIBIOS_STARTUP_MK"  : "os/common/startup/ARMCMx/compilers/GCC/mk/startup_stm32wbxx.mk",
    "CHIBIOS_PLATFORM_MK" : "os/hal/ports/STM32/STM32WBxx/platform.mk"
    }

pincount = {
    'A': 16,
    'B': 16,
    'C': 16,
    'D': 2,
    'E': 0,
    'F': 0,
    'G': 0,
    'H': 0,
    'I': 0,
    'J': 0,
    'K': 0
}


# MCU parameters
mcu = {
    # ram map, as list of (address, size-kb, flags)
    # flags of 1 means DMA-capable
    # flags of 2 means faster memory for CPU intensive work
    'RAM_MAP' : [
        # use 2nd mapping of SRAM2 to allow a single memory space
        (0x20000000, 256, 1), # SRAM1/SRAM2 
    ],
    # source for SRAM sizes was DS11929 Rev 16 page 20/194

    'EXPECTED_CLOCK' : 32000000,

    'DEFINES' : {
        'STM32WB' : '1',
    }
}

DMA_Map = {
	# format is (DMA_TABLE, StreamNum, Channel)
	# extracted from tabula-STM32L431-DMA.csv
    "ADC1"    	:	[(1,1,0),(2,3,0)],
	"ADC2"    	:	[(1,2,0),(2,4,0)],
	"AES_IN"  	:	[(2,1,6),(2,5,6)],
	"AES_OUT" 	:	[(2,2,6),(2,3,6)],
	"DAC_CH1" 	:	[(1,3,6),(2,4,3)],
	"DAC_CH2" 	:	[(1,4,5),(2,5,3)],
	"DFSDM1_FLT0"	:	[(1,5,0)],
	"DFSDM1_FLT1"	:	[(1,6,0)],
	"I2C1_RX" 	:	[(1,7,3),(2,6,5)],
	"I2C1_TX" 	:	[(1,6,3),(2,7,5)],
	"I2C2_RX" 	:	[(1,5,3)],
	"I2C2_TX" 	:	[(1,4,3)],
	"I2C3_RX" 	:	[(1,3,3)],
	"I2C3_TX" 	:	[(1,2,3)],
	"I2C4_RX" 	:	[(2,1,0)],
	"I2C4_TX" 	:	[(2,2,0)],
	"LPUART1_RX"	:	[(2,7,4)],
	"LPUART1_TX"	:	[(2,6,4)],
	"QUADSPI" 	:	[(1,5,5),(2,7,3)],
	"SAI1_A"  	:	[(2,1,1),(2,6,1)],
	"SAI1_B"  	:	[(2,2,1),(2,7,1)],
	"SAI2_A"  	:	[(1,6,1)],
	"SAI2_B"  	:	[(1,7,1)],
	"SDMMC1"  	:	[(2,4,7),(2,5,7)],
	"SPI1_RX" 	:	[(1,2,1),(2,3,4)],
	"SPI1_TX" 	:	[(1,3,1),(2,4,4)],
	"SPI2_RX" 	:	[(1,4,1)],
	"SPI2_TX" 	:	[(1,5,1)],
	"SPI3_RX" 	:	[(2,1,3)],
	"SPI3_TX" 	:	[(2,2,3)],
	"SWPMI1_RX"	:	[(2,1,4)],
	"SWPMI1_TX"	:	[(2,2,4)],
	"TIM15_CH1"	:	[(1,5,7)],
	"TIM15_COM"	:	[(1,5,7)],
	"TIM15_TRIG"	:	[(1,5,7)],
	"TIM15_UP"	:	[(1,5,7)],
	"TIM16_CH1,TIM16_UP"	:	[(1,3,4),(1,6,4)],
	"TIM1_CH1"	:	[(1,2,7)],
	"TIM1_CH2"	:	[(1,3,7)],
	"TIM1_CH3"	:	[(1,7,7)],
	"TIM1_CH4"	:	[(1,4,7)],
	"TIM1_COM"	:	[(1,4,7)],
	"TIM1_TRIG"	:	[(1,4,7)],
	"TIM1_UP" 	:	[(1,6,7)],
	"TIM2_CH1"	:	[(1,5,4)],
	"TIM2_CH2,TIM2_CH4"	:	[(1,7,4)],
	"TIM2_CH3"	:	[(1,1,4)],
	"TIM2_UP" 	:	[(1,2,4)],
	"TIM3_CH1"	:	[(1,6,5)],
	"TIM3_CH3"	:	[(1,2,5)],
	"TIM3_CH4"	:	[(1,3,5)],
	"TIM3_TRIG"	:	[(1,6,5)],
	"TIM3_UP" 	:	[(1,3,5)],
	"TIM6_UP" 	:	[(1,3,6),(2,4,3)],
	"TIM7_UP" 	:	[(2,5,3)],
	"TIM7_UP."	:	[(1,4,5)],
	"UART4_RX"	:	[(2,5,2)],
	"UART4_TX"	:	[(2,3,2)],
	"USART1_RX"	:	[(1,5,2),(2,7,2)],
	"USART1_TX"	:	[(1,4,2),(2,6,2)],
	"USART2_RX"	:	[(1,6,2)],
	"USART2_TX"	:	[(1,7,2)],
	"USART3_RX"	:	[(1,3,2)],
	"USART3_TX"	:	[(1,2,2)],
}

AltFunction_map = {
	# format is PIN:FUNCTION : AFNUM
	# extracted from pinouts.txt
	"PA0:COMP1_OUT"     	:	12,
	"PA0:SAI1_EXTCLK"   	:	13,
	"PA0:TIM2_CH1"      	:	1,
	"PA0:TIM2_ETR"      	:	14,
	"PA1:I2C1_SMBA"     	:	4,
	"PA1:LCD_SEG0"      	:	11,
	"PA1:SPI1_SCK"      	:	5,
	"PA1:TIM2_CH2"      	:	1,
	"PA2:COMP2_OUT"     	:	12,
	"PA2:LCD_SEG1"      	:	11,
	"PA2:LPUART1_TX"    	:	8,
	"PA2:QUADSPI_BK1_NCS"	:	10,
	"PA2:RCC_LSCO"      	:	0,
	"PA2:TIM2_CH3"      	:	1,
	"PA3:LCD_SEG2"      	:	11,
	"PA3:LPUART1_RX"    	:	8,
	"PA3:QUADSPI_CLK"   	:	10,
	"PA3:SAI1_CK1"      	:	3,
	"PA3:SAI1_MCLK_A"   	:	13,
	"PA3:TIM2_CH4"      	:	1,
	"PA4:LCD_SEG5"      	:	11,
	"PA4:LPTIM2_OUT"    	:	14,
	"PA4:SAI1_FS_B"     	:	13,
	"PA4:SPI1_NSS"      	:	5,
	"PA5:LPTIM2_ETR"    	:	14,
	"PA5:SAI1_SD_B"     	:	13,
	"PA5:SPI1_SCK"      	:	5,
	"PA5:TIM2_CH1"      	:	1,
	"PA5:TIM2_ETR"      	:	2,
	"PA6:LCD_SEG3"      	:	11,
	"PA6:LPUART1_CTS"   	:	8,
	"PA6:QUADSPI_BK1_IO3"	:	10,
	"PA6:SPI1_MISO"     	:	5,
	"PA6:TIM16_CH1"     	:	14,
	"PA6:TIM1_BKIN"     	:	12,
	"PA7:COMP2_OUT"     	:	12,
	"PA7:I2C3_SCL"      	:	4,
	"PA7:LCD_SEG4"      	:	11,
	"PA7:QUADSPI_BK1_IO2"	:	10,
	"PA7:SPI1_MOSI"     	:	5,
	"PA7:TIM17_CH1"     	:	14,
	"PA7:TIM1_CH1N"     	:	1,
	"PA8:LCD_COM0"      	:	11,
	"PA8:LPTIM2_OUT"    	:	14,
	"PA8:RCC_MCO"       	:	0,
	"PA8:SAI1_CK2"      	:	3,
	"PA8:SAI1_SCK_A"    	:	13,
	"PA8:TIM1_CH1"      	:	1,
	"PA8:USART1_CK"     	:	7,
	"PA9:I2C1_SCL"      	:	4,
	"PA9:LCD_COM1"      	:	11,
	"PA9:SAI1_D2"       	:	3,
	"PA9:SAI1_FS_A"     	:	13,
	"PA9:SPI2_SCK"      	:	5,
	"PA9:TIM1_CH2"      	:	1,
	"PA9:USART1_TX"     	:	7,
	"PA10:CRS_SYNC"     	:	10,
	"PA10:I2C1_SDA"     	:	4,
	"PA10:LCD_COM2"     	:	11,
	"PA10:SAI1_D1"      	:	3,
	"PA10:SAI1_SD_A"    	:	13,
	"PA10:TIM17_BKIN"   	:	14,
	"PA10:TIM1_CH3"     	:	1,
	"PA10:USART1_RX"    	:	7,
	"PA11:SPI1_MISO"    	:	5,
	"PA11:TIM1_BKIN2"   	:	12,
	"PA11:TIM1_CH4"     	:	1,
	"PA11:USART1_CTS"   	:	7,
	"PA11:USART1_NSS"   	:	7,
	"PA11:USB_DM"       	:	10,
	"PA12:LPUART1_RX"   	:	8,
	"PA12:SPI1_MOSI"    	:	5,
	"PA12:TIM1_ETR"     	:	1,
	"PA12:USART1_DE"    	:	7,
	"PA12:USART1_RTS"   	:	7,
	"PA12:USB_DP"       	:	10,
	"PA13:IR_OUT"       	:	8,
	"PA13:SAI1_SD_B"    	:	13,
	"PA13:JTMS-SWDIO"		:	0,
	"PA13:USB_NOE"      	:	10,
	"PA14:I2C1_SMBA"    	:	4,
	"PA14:LCD_SEG5"     	:	11,
	"PA14:LPTIM1_OUT"   	:	1,
	"PA14:SAI1_FS_B"    	:	13,
	"PA14:JTCK-SWCLK"		:	0,
	"PA15:LCD_SEG17"    	:	11,
	"PA15:RCC_MCO"      	:	6,
	"PA15:SPI1_NSS"     	:	5,
	"PA15:SYS_JTDI"     	:	0,
	"PA15:TIM2_CH1"     	:	1,
	"PA15:TIM2_ETR"     	:	2,
	"PA15:TSC_G3_IO1"   	:	9,
	"PB0:COMP1_OUT"     	:	12,
	"PB0:RF_TX_MOD_EXT_PA"	:	6,
	"PB1:LPTIM2_IN1"    	:	14,
	"PB1:LPUART1_DE"    	:	8,
	"PB1:LPUART1_RTS"   	:	8,
	"PB2:I2C3_SMBA"     	:	4,
	"PB2:LCD_VLCD"      	:	11,
	"PB2:LPTIM1_OUT"    	:	1,
	"PB2:SAI1_EXTCLK"   	:	13,
	"PB2:SPI1_NSS"      	:	5,
	"PB3:LCD_SEG7"      	:	11,
	"PB3:SAI1_SCK_B"    	:	13,
	"PB3:SPI1_SCK"      	:	5,
	"PB3:SYS_JTDO-SWO"  	:	0,
	"PB3:TIM2_CH2"      	:	1,
	"PB3:USART1_DE"     	:	7,
	"PB3:USART1_RTS"    	:	7,
	"PB4:I2C3_SDA"      	:	4,
	"PB4:LCD_SEG8"      	:	11,
	"PB4:SAI1_MCLK_B"   	:	13,
	"PB4:SPI1_MISO"     	:	5,
	"PB4:SYS_JTRST"     	:	0,
	"PB4:TIM17_BKIN"    	:	14,
	"PB4:TSC_G2_IO1"    	:	9,
	"PB4:USART1_CTS"    	:	7,
	"PB4:USART1_NSS"    	:	7,
	"PB5:COMP2_OUT"     	:	12,
	"PB5:I2C1_SMBA"     	:	4,
	"PB5:LCD_SEG9"      	:	11,
	"PB5:LPTIM1_IN1"    	:	1,
	"PB5:LPUART1_TX"    	:	8,
	"PB5:SAI1_SD_B"     	:	13,
	"PB5:SPI1_MOSI"     	:	5,
	"PB5:TIM16_BKIN"    	:	14,
	"PB5:TSC_G2_IO2"    	:	9,
	"PB5:USART1_CK"     	:	7,
	"PB6:I2C1_SCL"      	:	4,
	"PB6:LCD_SEG6"      	:	11,
	"PB6:LPTIM1_ETR"    	:	1,
	"PB6:RCC_MCO"       	:	0,
	"PB6:SAI1_FS_B"     	:	13,
	"PB6:TIM16_CH1N"    	:	14,
	"PB6:TSC_G2_IO3"    	:	9,
	"PB6:USART1_TX"     	:	7,
	"PB7:I2C1_SDA"      	:	4,
	"PB7:LCD_SEG21"     	:	11,
	"PB7:LPTIM1_IN2"    	:	1,
	"PB7:TIM17_CH1N"    	:	14,
	"PB7:TIM1_BKIN"     	:	3,
	"PB7:TSC_G2_IO4"    	:	9,
	"PB7:USART1_RX"     	:	7,
	"PB8:I2C1_SCL"      	:	4,
	"PB8:LCD_SEG16"     	:	11,
	"PB8:QUADSPI_BK1_IO1"	:	10,
	"PB8:SAI1_CK1"      	:	3,
	"PB8:SAI1_MCLK_A"   	:	13,
	"PB8:TIM16_CH1"     	:	14,
	"PB8:TIM1_CH2N"     	:	1,
	"PB9:I2C1_SDA"      	:	4,
	"PB9:IR_OUT"        	:	8,
	"PB9:LCD_COM3"      	:	11,
	"PB9:QUADSPI_BK1_IO0"	:	10,
	"PB9:SAI1_D2"       	:	3,
	"PB9:SAI1_FS_A"     	:	13,
	"PB9:SPI2_NSS"      	:	5,
	"PB9:TIM17_CH1"     	:	14,
	"PB9:TIM1_CH3N"     	:	1,
	"PB10:COMP1_OUT"    	:	12,
	"PB10:I2C3_SCL"     	:	4,
	"PB10:LCD_SEG10"    	:	11,
	"PB10:LPUART1_RX"   	:	8,
	"PB10:QUADSPI_CLK"  	:	10,
	"PB10:SAI1_SCK_A"   	:	13,
	"PB10:SPI2_SCK"     	:	5,
	"PB10:TIM2_CH3"     	:	1,
	"PB10:TSC_SYNC"     	:	9,
	"PB11:COMP2_OUT"    	:	12,
	"PB11:I2C3_SDA"     	:	4,
	"PB11:LCD_SEG11"    	:	11,
	"PB11:LPUART1_TX"   	:	8,
	"PB11:QUADSPI_BK1_NCS"	:	10,
	"PB11:TIM2_CH4"     	:	1,
	"PB12:I2C3_SMBA"    	:	4,
	"PB12:LCD_SEG12"    	:	11,
	"PB12:LPUART1_DE"   	:	8,
	"PB12:LPUART1_RTS"  	:	8,
	"PB12:SAI1_FS_A"    	:	13,
	"PB12:SPI2_NSS"     	:	5,
	"PB12:TIM1_BKIN"    	:	3,
	"PB12:TSC_G1_IO1"   	:	9,
	"PB13:I2C3_SCL"     	:	4,
	"PB13:LCD_SEG13"    	:	11,
	"PB13:LPUART1_CTS"  	:	8,
	"PB13:SAI1_SCK_A"   	:	13,
	"PB13:SPI2_SCK"     	:	5,
	"PB13:TIM1_CH1N"    	:	1,
	"PB13:TSC_G1_IO2"   	:	9,
	"PB14:I2C3_SDA"     	:	4,
	"PB14:LCD_SEG14"    	:	11,
	"PB14:SAI1_MCLK_A"  	:	13,
	"PB14:SPI2_MISO"    	:	5,
	"PB14:TIM1_CH2N"    	:	1,
	"PB14:TSC_G1_IO3"   	:	9,
	"PB15:LCD_SEG15"    	:	11,
	"PB15:RTC_REFIN"    	:	0,
	"PB15:SAI1_SD_A"    	:	13,
	"PB15:SPI2_MOSI"    	:	5,
	"PB15:TIM1_CH3N"    	:	1,
	"PB15:TSC_G1_IO4"   	:	9,
	"PC0:I2C3_SCL"      	:	4,
	"PC0:LCD_SEG18"     	:	11,
	"PC0:LPTIM1_IN1"    	:	1,
	"PC0:LPTIM2_IN1"    	:	14,
	"PC0:LPUART1_RX"    	:	8,
	"PC1:I2C3_SDA"      	:	4,
	"PC1:LCD_SEG19"     	:	11,
	"PC1:LPTIM1_OUT"    	:	1,
	"PC1:LPUART1_TX"    	:	8,
	"PC1:SPI2_MOSI"     	:	3,
	"PC2:LCD_SEG20"     	:	11,
	"PC2:LPTIM1_IN2"    	:	1,
	"PC2:SPI2_MISO"     	:	5,
	"PC3:LCD_VLCD"      	:	11,
	"PC3:LPTIM1_ETR"    	:	1,
	"PC3:LPTIM2_ETR"    	:	14,
	"PC3:SAI1_D1"       	:	3,
	"PC3:SAI1_SD_A"     	:	13,
	"PC3:SPI2_MOSI"     	:	5,
	"PC4:LCD_SEG22"     	:	11,
	"PC5:LCD_SEG23"     	:	11,
	"PC5:SAI1_D3"       	:	3,
	"PC6:LCD_SEG24"     	:	11,
	"PC10:LCD_COM4"     	:	11,
	"PC10:LCD_SEG28"    	:	11,
	"PC10:LCD_SEG40"    	:	11,
	"PC10:SYS_TRACED1"  	:	0,
	"PC10:TSC_G3_IO2"   	:	9,
	"PC11:LCD_COM5"     	:	11,
	"PC11:LCD_SEG29"    	:	11,
	"PC11:LCD_SEG41"    	:	11,
	"PC11:TSC_G3_IO3"   	:	9,
	"PC12:LCD_COM6"     	:	11,
	"PC12:LCD_SEG30"    	:	11,
	"PC12:LCD_SEG42"    	:	11,
	"PC12:RCC_LSCO"     	:	6,
	"PC12:SYS_TRACED3"  	:	0,
	"PC12:TSC_G3_IO4"   	:	9,
	"PD0:SPI2_NSS"      	:	5,
	"PD1:SPI2_SCK"      	:	5,
	"PH3:RCC_LSCO"      	:	0,
}

ADC1_map = {
	# format is PIN : ADC1_CHAN
    "PA0"	:	5,
    "PA1"	:	6,
    "PA2"	:	7,
    "PA3"	:	8,
    "PA4"	:	9,
    "PA5"	:	10,
    "PA6"	:	11,
    "PA7"	:	12,
    "PC4"   :   13,
    "PC5"   :   14,
    "PB0"   :   15,
    "PB1"   :   16,
    "PC0"   :   1,
    "PC1"   :   2,
    "PC2"   :   3,
    "PC3"   :   4,
}
    
