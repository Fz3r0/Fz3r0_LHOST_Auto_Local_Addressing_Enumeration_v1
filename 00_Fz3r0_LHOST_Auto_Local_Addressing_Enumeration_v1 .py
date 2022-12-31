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
#    - Esta herramienta obtiene automaticamente la IPv4 del LHOST (Local Host o la Máquina Local), default "eth0"     # 
#    - También permite obtener automaticamente la IPv4 del túnel VPN del LHOST, default "tun0"                        #
#    - De la misma manera obtiene la MAC Address del LHOST (la MAC local y real del host)                             #
#    - Al finalizar la función permite guardar las variables por separado para facilitar y eficientar su uso          #
#    - También permite modificar la búsqueda de interfaces locales de manera manual (en caso de usar otra interfaz)   #
#                                                                                                                     # 
#######################################################################################################################

# Ejemplo para importar este script dentro de otro de manera completa (se debe poner en misma carpeta):

    # import 00_Fz3r0_LHOST_Auto_Local_Addressing_Enumeration_v1 

# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
#
# <<< --- INICIA ---|||  LHOST: Auto Local Addressing Enumeration @ Fz3r0
#
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

# VARIABLES MODIFICABLES (DEFAULTS)

    # 1. Interfaz Default Física = eth0 [normalmente eth0 es la default en Linux]
    # 2. Interfaz Default Tunel  = tun0 [normalmente tun0 es la default en Linux]

        # En caso de querer localizar por default el direccionamiento de otra interfaz local manualmente por default modificar

lhost_interface_eth_funct_x = "eth0"     # <<<--- Interfaz "Física" - LHOST
lhost_interface_tun_funct_x = "tun0"     # <<<--- Túnel para VPN - LHOST 

# FLAGS PARA COMANDO 

    # Estas flags modificarán la variable de las interfaces eth0 y tun0, en caso de no modificar la flag se tomarán los default

        # -i   --interface        = modificará manualmente la variable default "eth0" (FÍSICA) para utilizar una interfaz diferente

        # -it  --interface_tunel  = modificará manualmente la variable default "tun0" (TÚNEL/VPN) para utilizar una interfaz diferente

# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

# MÓDULOS NECESARIOS 

# scapy: Packet Forgey
import scapy.all as scapy
# argparse: Generador de Argumentos
import argparse

# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

# FUNCIÓN PRINCIPAL - OBTENER INFORMACIÓN DE LA INTERFAZ DE LHOST

def obtener_info_interfaz(interface=lhost_interface_eth_funct_x , interface_tunel=lhost_interface_tun_funct_x):
  # Obtener la dirección IP de la interfaz especificada
  try:
    ip_local_lhost = scapy.get_if_addr(interface)
  except Exception:
    ip_local_lhost = "No se pudo obtener la dirección IPv4 de la interfaz: {}".format(interface)
  
  # Obtener la dirección IP de la interfaz de túnel (por ejemplo VPN) especificada
  try:
    ip_tunel_lhost = scapy.get_if_addr(interface_tunel)
  except Exception:
    ip_tunel_lhost = "No se pudo obtener la dirección IPv4 de la interfaz: {}".format(interface_tunel)
  
  # Obtener la dirección MAC de la interfaz especificada
  try:
    mac_local_lhost = scapy.get_if_hwaddr(interface)
  except Exception:
    mac_local_lhost = "No se pudo obtener la dirección MAC de la interfaz: {}".format(interface)
  
  # Obtener los valores obtenidos durante la función para ser guardados en memoria, así se pueden usar libremente
  return (ip_local_lhost, ip_tunel_lhost, mac_local_lhost)

# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

# DECLARACIÓN DE ARGUMENTOS Y FLAGS (VARIABLES DE COMANDO)

if __name__ == "__main__":
  # Crear un parser de argumentos para permitir al usuario especificar las interfaces
  parser = argparse.ArgumentParser()
  parser.add_argument("-i", "--interface", help="Nombre de la interfaz local a consultar, ej. eth0", default=lhost_interface_eth_funct_x)
  parser.add_argument("-it", "--interface_tunel", help="Nombre de la interfaz local de túnel/VPN a consultar, ej. tun0", default=lhost_interface_tun_funct_x)
  args = parser.parse_args()

  # Obtener la información de las interfaces especificadas
  (ip_local_lhost, ip_tunel_lhost, mac_local_lhost) = obtener_info_interfaz(args.interface, args.interface_tunel)

# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

# FUERA DE LA FUNCIÓN ASÍ SE OBTIENEN LOS DATOS:

    # Ahora ya se pueden utilizar esas 3 sencillas variables para llamar en cualquier lugar el direccionamiento local :D 

        # Nota: Estas lineas pueden ser comentadas o borradas en caso de utilizar la función en otro script

# Ejemplo para imprimir la información obtenida con lineas combinadas:
print()
print("[🔴] Dirección IP de  {}:....... {}".format(args.interface, ip_local_lhost))
print("[🔵] Dirección IP de  {}:....... {}".format(args.interface_tunel, ip_tunel_lhost))
print("[🟢] Dirección MAC de {}:....... {}".format(args.interface, mac_local_lhost))

# Ejemplo para imprimir la información obtenida de manera sencilla:
print()
print(ip_local_lhost)
print(ip_tunel_lhost)
print(mac_local_lhost)

# Promoción desvergonzada del padrino: 
print()
print("[💀] Twitter: @Fz3r0_Ops  ||  Github: Fz3r0  ||  Youtube: @Fz3r0_Ops")

# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
#
# --- >>> TERMINA ---|||  LHOST: Auto Local Addressing Enumeration @ Fz3r0
#
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
