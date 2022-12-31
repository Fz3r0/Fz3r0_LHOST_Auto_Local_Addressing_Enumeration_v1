# Fz3r0 - LHOST Auto Local Addressing Enumeration
Obtiene y guarda automaticamente la IPv4 y MAC de LHOST incluyendo interfaz física y túnel VPN

## Descripción

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

- Comando por default:

```py
python 00_Fz3r0_LHOST_Auto_Local_Addressing_Enumeration_v1.py
```
![image](https://user-images.githubusercontent.com/94720207/210150678-879c15bc-1389-4151-8a07-345790cfd70a.png)

## Flags y Argumentos

## Modificación de variables Default

- 

![image](https://user-images.githubusercontent.com/94720207/210150866-36680b1d-d29d-48ff-9d7e-c2baed9d7f62.png)

