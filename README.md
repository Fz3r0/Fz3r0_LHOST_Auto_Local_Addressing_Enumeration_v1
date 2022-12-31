# Fz3r0 - LHOST Auto Local Addressing Enumeration

_Keywords:_ `Python` `Scapy` `Host Enumeration` `Network Automation` `IP & MAC Addressing` `Networking` `Pentesting`

## Script

- [Descargar/Download Script](https://github.com/Fz3r0/Fz3r0_LHOST_Auto_Local_Addressing_Enumeration_v1/blob/main/00_Fz3r0_LHOST_Auto_Local_Addressing_Enumeration_v1%20.py)

## Descripción

- Obtiene y guarda automaticamente la IPv4 y MAC de LHOST incluyendo interfaz física y túnel VPN
- Esta herramienta obtiene automaticamente la IPv4 del LHOST (Local Host o la Máquina Local), default "eth0"     
- También permite obtener automaticamente la IPv4 del túnel VPN del LHOST, default "tun0"                        
- De la misma manera obtiene la MAC Address del LHOST (la MAC local y real del host)                             
- Al finalizar la función permite guardar las variables por separado para facilitar y eficientar su uso          
- También permite modificar la búsqueda de interfaces locales de manera manual (en caso de usar otra interfaz)  

## Objetivo

- Esta herramienta está pensada como parte de los nuevos módulos que estoy programando para mi proyecto de Arsenal de Networking

## Instalación

- Solo es necesario copiar el archivo `.py` al directorio de trabajo
- En caso de querer utilizar como módulo adicional de otro script utilizar al inicio:

```py
import 00_Fz3r0_LHOST_Auto_Local_Addressing_Enumeration_v1
```


## Modo de uso

- Ejecutar el siguiente comando en Bash:

```py
python 00_Fz3r0_LHOST_Auto_Local_Addressing_Enumeration_v1.py
```
![image](https://user-images.githubusercontent.com/94720207/210156559-e3840b9f-4fd4-43f7-ab97-69f651d93861.png)

- Por ejemplo, en caso de no tener activa la interface de túnel VPN:

![image](https://user-images.githubusercontent.com/94720207/210156537-eca2fbbb-58b6-4c41-8495-e60f3ab8be8a.png)

## Variables obtenidas

- Esta herramienta funionca excelente como módilo adicional para generar las siguientes 5 variables automáticamente de manera sencilla

![image](https://user-images.githubusercontent.com/94720207/210156689-584393f0-6566-4f39-93c6-a4cee788e461.png)

- Resultado:

![image](https://user-images.githubusercontent.com/94720207/210156721-c4112de5-09b5-4793-b0cb-b0ddef15347e.png)



