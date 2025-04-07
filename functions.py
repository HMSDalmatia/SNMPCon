from pysnmp.hlapi.v3arch.asyncio import *

async def conn(username, password, encryptionKey, authorization_protocol, encryptionProtocol, contDat=ContextData(),
               ip='127.0.0.1'):
    # Auth is to authenticate, priv=encryption (default enryption)
    UsmUserData(
        userName=username,
        authKey=password,
        privKey=encryptionKey,
        authProtocol=authorization_protocol,
        privProtocol=encryptionProtocol,
    )
    # place where connection is being made
    connection = await get_cmd(SnmpEngine(), CommunityData('public'),
                               ObjectType(ObjectIdentity('1.3.6.1.2.1.1.5.0')),
                               UdpTransportTarget((ip, 161)),
                               contextData=contDat)
    print(connection)
