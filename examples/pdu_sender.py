import socket
import time

from io import BytesIO

from opendis.DataOutputStream import DataOutputStream
from opendis.dis7 import EntityStatePdu
from opendis.RangeCoordinates import GPS

def send_dis7_entity_state_pdu(lat, lon, alt, speed = 0, climb = 0, heading = 360, iaco = 'n/a', callsign = '', address = "127.0.0.1", port= 1999 ):

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udpSocket:
        udpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    
        pdu = EntityStatePdu()
        pdu.entityID.entityID = 1999
        pdu.entityID.siteID = 17
        pdu.entityID.applicationID = 23
    
        if lat != '':
        	pdu.entityLocation.x = float(lat)
        
        if lon != '':
        	pdu.entityLocation.y = float(lon)
        
        if alt != '':
        	pdu.entityLocation.z = float(alt)
        if speed != '':
        	pdu.entityLinearVelocity.x = float(speed)
        if climb != '':
        	pdu.entityLinearVelocity.y = float(climb)
        if heading != '':
        	pdu.entityOrientation.Psi = float(heading)
        if iaco != '':
        	pdu.entityMarkings = iaco
        if callsign != '':
        	pdu.entityMarkings = iaco
        memoryStream = BytesIO()
        outputStream = DataOutputStream(memoryStream)
        pdu.serialize(outputStream)
        data = memoryStream.getvalue()
    
        udpSocket.sendto(data, (address, port))

