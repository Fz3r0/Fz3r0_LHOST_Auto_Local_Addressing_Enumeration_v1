#######################################################################################################################
#                                                                                                                     #
#           @@@@@@@@@@@@@@@@@@                Author:......... Fz3r0                                                  #
#         @@@@@@@@@@@@@@@@@@@@@@@                                                                                     #
#       @@@@@@@@@@@@@@@@@@@@@@@@@@@           Cyber-Weapon:... LHOST: Auto Local Addressing Enumeration               #
#      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@                                                                                  #
#     @@@@@@@@@@@@@@@/      \@@@/   @         Version:........ 1.0                                                    #
#    @@@@@@@@@@@@@@@@\      @@  @___@                                                                                 #
#    @@@@@@@@@@@@@ @@@@@@@@@@  | \@@@@@       Github:......... github.com/Fz3r0                                       #
#    @@@@@@@@@@@@@ @@@@@@@@@\__@_/@@@@@                                                                               #
#     @@@@@@@@@@@@@@@/,/,/./'/_|.\'\,\        Twitter:........ @Fz3r0_OPs                                             #
#       @@@@@@@@@@@@@|  | | | | | | | |                                                                               #
#                     \_|_|_|_|_|_|_|_|       Youtube:........ @Fz3r0_OPs                                             #
#                                                                                                                     #
#    DESCRIPCIÓN:                                                                                                     #
#                                                                                                                     #
#    - Esta herramienta obtiene automaticamente la IPv4 del LHOST (Local Host o la Máquina Local)                     #
#    - También permite obtener automaticamente la IPv4 del túnel VPN del LHOST                                        #
#    - De la misma manera obtiene la MAC Address del LHOST (la MAC local y real del host)                             #
#    - Al finalizar la función permite guardar las variables por separado para facilitar y eficientar su uso          #
#    - La idea es que sea utilizado como módulo para proyectos más grandes de Network Security y Pentesting           #
#                                                                                                                     #
#    INSTRUCCIONES:                                                                                                   #
#                                                                                                                     #
#    - Solo basta escribir el siguiente comando para que el script detecte tanto las interfaces activas como          #
#      su direccionamiento IPv4 y MAC, incluyendo interfaces locales y túnel VPN.                                     #
#                                                                                                                     #
#          python 00_Fz3r0_LHOST_Auto_Local_Addressing_Enumeration_v1.py                                              #
#                                                                                                                     #
#    USAR COMO MÓDULO ADICIONAL DESDE OTRO SCRIPT PYTHON:                                                             #
#                                                                                                                     #
#    - Nota: El archivo ".py" se debe poner en misma carpeta, dentro de ese script importar como cualquier módulo:    #
#                                                                                                                     #
#         import 00_Fz3r0_LHOST_Auto_Local_Addressing_Enumeration_v1                                                  #
#                                                                                                                     #
#######################################################################################################################

# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
#
# <<< --- INICIA ---|||  LHOST: Auto Local Addressing Enumeration @ Fz3r0
#
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

# MÓDULOS NECESARIOS 

# scapy: Packet Forgey
import scapy.all as scapy
# psutil: Obtiene información del Sistema (utilizada para buscar interfaz activa)
import psutil

# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

# SECCIONES PRINCIPALES: A y B

    # 1. SECCIÓN A - OBTENER STATUS DE INTERFACES ETHERNET Y TUNEL VPN ACTIVAS DE LHOST 
    #
    #    - Esta secćón permite obtener de manera automática las interfaces de red activas en el LHOST
    #    - Al obtener una IPv4 la detectará activa y será la interfaz que se utilizará en la siguiente función
    #    - La función permite obtener tanto la IP de Ethernet local como la IP de túnel VPN en caso de existir

# Obtenemos la información de las interfaces de red
interfaces_informacion_lhost = psutil.net_if_addrs()

# Inicializamos las variables que almacenarán las interfaces activas
f0_eth_interface_lhost = "N/A "
f0_tun_interface_lhost = "N/A "

# Recorremos las interfaces
for interfaz, direcciones in interfaces_informacion_lhost.items():
    # Si la interfaz es una interfaz ethernet y tiene al menos una dirección IP válida,
    # la guardamos como la interfaz local activa
    if "eth" in interfaz and any(addr.address != "0.0.0.0" and addr.address != "127.0.0.1" for addr in direcciones):
        f0_eth_interface_lhost = interfaz
        break

# Recorremos de nuevo las interfaces
for interfaz, direcciones in interfaces_informacion_lhost.items():
    # Si la interfaz es una interfaz de túnel VPN y tiene al menos una dirección IP válida,
    # la guardamos como la interfaz de túnel activa
    if "tun" in interfaz and any(addr.address != "0.0.0.0" and addr.address != "127.0.0.1" for addr in direcciones):
        f0_tun_interface_lhost = interfaz
        break

    # 2. SECCIÓN B - FUNCIÓN PARA UTILIZAR EL STATUS OBTENIDO EN "1." PARA OBTENER EL DIRECCIONAMIENTO IP Y MAC TANTO DE ETH COMO TUNEL
    #
    # - Esta función permite obtener de manera automática la Interfaz de red activa en el LHOST
    # - Al obtener una IPv4 la detectará activa y será la interfaz que se utilizará en la siguiente función

def obtener_info_interfaz(f0_eth_interface_lhost , f0_tun_interface_lhost):
  # Obtener la dirección IP de la interfaz especificada
  try:
    f0_ip_local_lhost = scapy.get_if_addr(f0_eth_interface_lhost)
  except Exception:
    f0_ip_local_lhost = "No se pudo obtener la dirección IPv4 de la interfaz: {}".format(f0_eth_interface_lhost)
  
  # Obtener la dirección IP de la interfaz de túnel (por ejemplo VPN) especificada
  try:
    f0_ip_tunel_lhost = scapy.get_if_addr(f0_tun_interface_lhost)
  except Exception:
    f0_ip_tunel_lhost = "No se pudo obtener la dirección IPv4 de la interfaz: {}".format(f0_tun_interface_lhost)
  
  # Obtener la dirección MAC de la interfaz especificada
  try:
    f0_mac_local_lhost = scapy.get_if_hwaddr(f0_eth_interface_lhost)
  except Exception:
    f0_mac_local_lhost = "No se pudo obtener la dirección MAC de la interfaz: {}".format(f0_eth_interface_lhost)
  
  # Obtener los valores obtenidos durante la función para ser guardados en memoria, así se pueden usar libremente
  return (f0_ip_local_lhost, f0_ip_tunel_lhost, f0_mac_local_lhost)

# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

# OBTENER RESULTADOS DE DIRECCIONAMIENTO FUERA DE LA FUNCIÓN:

# Asigna a las 3 variables mostradas, el resultado de las 3 variables obtenidas por la función
# Por fines prácticos tienen los mismos nombres, pero en realidad se podrían usar 3 variables nuevas para recibir esos datos de la funcón:
(f0_ip_local_lhost, f0_ip_tunel_lhost, f0_mac_local_lhost) = obtener_info_interfaz(f0_eth_interface_lhost, f0_tun_interface_lhost)

# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

# RESULTADOS: VARIABLES EN MEMORIA 

    # - Ahora ya se pueden utilizar los valores se las 5 variables totales obtenidas de manera automática.
    # - En este ejemplo se imprimen los resultados en consola, pero pueden ser guardados para mandarlos llamar a conveniencia

# Imprimimos la información de las interfaces activas
print()
if f0_eth_interface_lhost != "N/A ":
    print("[🟢] Interfaz ethernet local activa:...<( {} )>".format(f0_eth_interface_lhost))
else:
    print("[🔴] IInterfaz ethernet local no disponible")

if f0_tun_interface_lhost != "N/A ":
    print("[🟢] Interfaz de túnel VPN activa:.....<( {} )>".format(f0_tun_interface_lhost))
else:
    print("[🔴] Interfaz de túnel VPN no disponible")

# Ejemplo para imprimir la información obtenida con lineas combinadas:
print()
print("[🔵] Dirección IP de <( {} )>:.......<( {} )>".format(f0_eth_interface_lhost, f0_ip_local_lhost))
print("[🟣] Dirección IP de <( {} )>:.......<( {} )>".format(f0_tun_interface_lhost, f0_ip_tunel_lhost))
print("[🔵] Dirección MAC:....................<( {} )>".format(f0_mac_local_lhost))

# Ejemplo para imprimir únicamente los valores obtenidos de las variables:
print()
print(" >> Variables guardadas en memoria:")
print()
print(f0_eth_interface_lhost)
print(f0_tun_interface_lhost)
print()
print(f0_ip_local_lhost)
print(f0_ip_tunel_lhost)
print(f0_mac_local_lhost)

# Promoción desvergonzada del padrino: 
print()
print("[💀] Twitter: @Fz3r0_Ops  ||  Github: Fz3r0  ||  Youtube: @Fz3r0_Ops")

# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
#
# --- >>> TERMINA ---|||  LHOST: Auto Local Addressing Enumeration @ Fz3r0
#
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
