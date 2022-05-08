import random
import socket
import struct
import time
import hashlib

initial_version_command = b'\xf9\xbe\xb4\xd9version\x00\x00\x00\x00\x00V\x00\x00\x00\xed\x01m\xf7\x7f\x11\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x97\xbdIb\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff"P\xe0* \x8d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\x00\x00\x00\x00\x00\x00s\x0bR\xc1\x0f\xb8\x8cg\x00\x00\x00\x00\x00\x01'
transaction = b"\xf9\xbe\xb4\xd9tx\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x00\x00\x00\xa2G\xc4f\x02\x00\x00\x00\x01\xf3\xe6\xf6\x9b@'\xa5M\xb6\x86o\xb5\x1f\x0f\xafz\x8b\x14\x0e_\ts`z\x948x\x7f\xfe\x1e\xe9s\x00\x00\x00\x00\x00\xff\xff\xff\xff\x020\xb1\x0f\x00\x00\x00\x00\x00\x19v\xa9\x14\x95\x9at\xd5\xa6R\xf1\xecg\x91\xc9yyC\xe8p\xa9\x9d\tK\x88\xac\x91f\x05\x01\x00\x00\x00\x00\x16\x00\x14J\xb3V\x8d\x9f\xd1\xebt\x07\xea\x03\xce^f\xd6\xbe\xbb\x84p\xc5\x00\x00\x00\x00"
inv = b'\xf9\xbe\xb4\xd9inv\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc9\x04\x00\x00\x90\x1f\xce\x08"\x01\x00\x00\x00\xf4\xe0\x86\ru\x8b\xb6\xff\x12PM\xe1\x0f\x99s\x87\x876\xf1\xe8\x9amQ+P\x06\xb5\x1c*\x9f\x00D\x01\x00\x00\x00u\n\xe9\xce\xf1\x9e\xd6\x0e\xfa\xa0cq>\xb8\xc8\x19/:\x0e\xe7\xf6u\x0e^\xfaA\x17\xb0\xb7\x81W\xf1\x01\x00\x00\x00Q\xb6R\xff\x9a\xc4\x97\x856\xebN\xdc\x83\xea\xc3\xb6(\t-\xc8\xb4\xfe\xea\x9d8"0\xb1GElk\x01\x00\x00\x00\xf2\x0c\x07\x19\xb6\x0em\xa56i\xcc&\xd7\t\xde\xcf\x1db\xafw.\xf7L\x8b\xf0\xda\x84\xcfL\x83Q\xef\x01\x00\x00\x00\x14\xb7\x82\xc1G}\xd5v\xae\x8d>\xafV\x8b\xc8\xba\xc5\x97I-\xc0<\xd4\x8d\x1e\x93"\x1e\xd1\x8d\x16\xff\x01\x00\x00\x00\xd7\xc2\x0fhL\x13jc\xab\x1aB\xd65\x8b\xff\xa3^+i\xe8_N\x9ex\x83\xabN\xf1\xb9\x0e\xe1\x01\x01\x00\x00\x00\xa86\xa8\x99\xf2\xa2\xa6O\xd8\xa3\xcf\xc8\x12/\xc2E\x87\x0ef\x08\xd9ULX/\xb9\x9c\x84c_4\x8e\x01\x00\x00\x00\xd7]\x04<\xbb9\x87g\x88\x9eC<u\xba\xed\x87\xdc\xf2\xdb\x84-\x99\x88cZa]\xd6\xc1\x03+1\x01\x00\x00\x00\xef\x8c\xd9\xd8\x1b\x08\x86D\x0c@e\x02\n\xab\x03]\x0c\x82\x1a\x9b\x0b\xeca\x13+\x1aB\xa4\xaeX\xd1\xff\x01\x00\x00\x00\xe2tLN\x98KKP\x1f\'=\x8dp\x13.\xf5\xf9\x93\xdf2\xfb\x92XO\xfdl\x98\xf0a\x16\x95\x82\x01\x00\x00\x00\xde\xa1\x1c[\xad*\xac>\xc9\x17\xed|\xc4\x9c<\xc9=!\xdf\x1b\xf1!bZ\x08\xebL6\xbdd-\x02\x01\x00\x00\x00\xe1"Z\xd2\x84) k2\xceJ/\xdb=\xd8T\xd8\x85\'O\x84\x1d\xac\xa9O\x90\xab\xe5\x83\xa7\x85y\x01\x00\x00\x00\xbc\xbc\xf6j\xae\xcdI\xda\x00\xc2d\xe9\x81\x11/{_\xe8\xbf/\xba\xfb\x9f\x08\x8bXQ\x86\x81\x0c\xa7\x9b\x01\x00\x00\x00;X}$\xc3\xfbUs x\xfea\xa69\xe7\xbc\x8b\x9cy3;}\x7f\x8a\xf2:\xbe\x89\xc5\xf4!B\x01\x00\x00\x00\xd8G\xf7\xd2\xa9\xdf\xe8\xd2\x87\x8f\']\x8c\xb8\x91h\xaf\xb3\xb1\x9b\x9b|\x1dj\xb0\xe0W\xee\x00R\xb6\x18\x01\x00\x00\x00\xa2p%aZ=\xf4J\x00\x85$\n\xbd<ju\x92D*\x95\xb0\xad\xc9\x04\'\x1b_}?v\xf1\xf0\x01\x00\x00\x00yU\x02\x915\xa2\xda\xd4\xa4\x96\x1dr\xdd\xf6=\x9b\x9b\x12\xaf\xd9\x98\x8b\nN\xebI\xca\xa4\xf8\x16\x11\x16\x01\x00\x00\x00\xcc\x0c\xef\xd9\xde\r\xc5)\x0e\xf7\xe4[\xc5Fb\xa5\xc8\x91RE\xb6\x04k\x10\xf1A\x8d\x0f\xc5\xb42\xb8\x01\x00\x00\x003\xd4\x87)\x82\xf1\xc1\r\x12M\x10ekC\x8b\x1e\xd97rf$\xd4:\xa6\x98Y\xba\xa8\x06\xf9m\x85\x01\x00\x00\x00@\xcd\xfd\x08-cE\xe0\xf38\x9b\xe3\xcb`\x04\x97\xd5\x96\x89@\xcbi\xf1y\x89\x1cw\xa9\xe9\xf12\xa1\x01\x00\x00\x00\xebO\xdb\xe4Ws\xf6Q\x01\x12b\xd4\xc2-\x9d\xfd\xac\xf4\\\xe1\xe6lu\xe7i\xe3[`g7\xf3F\x01\x00\x00\x00Uu\xea\x98\xa1$\xa5\x05\xf5\x1bA\x01ZR\xa0C\xf03\xc3\xa9\xa5\xed\x11\x93\xed\xd9\xd2\x92\xc8\x9a&2\x01\x00\x00\x00\x8e\xf5;\xb8{\x9b\xddp\x1fv\xdb\xcd\xeb\x1f\xa0\xcbZ\xd6\x10\xf5D\xb8\xf1/a\x15\\\xda#\x10\xfe.\x01\x00\x00\x00\xa8@\xfak\xc5|\x92|%Uvm\xf99[HOHJ>\xc1)\x92\xf7v]\x0cxsq\xcf\x06\x01\x00\x00\x00\x0f\x87\xdc\xfc\xcb5\x0e\xf4\xc5GQ,\x13p%]\x897\xce_\xe9\x07\xc5R\xa0\x94\xbb\xf5\xc2_{\x1f\x01\x00\x00\x00I\xd3\x8a\xb4\xc8\x03\x17\xc3!"\xdc\xcd~\xbf\xd7\xb0,\xa76Z\xcc\'\x1e\x88\xf7\xcc\x8c\xa3\x11s\xf2\xa0\x01\x00\x00\x00\xa4\x126{\xda\xf2\xe2\xa3q%\x87\x9ey\xee\x1f\xc7Pp\xed\xe5\x90\x88\xa0\xecyO7!\x0c\xafi\x99\x01\x00\x00\x00\xb1\xfb,\xe7H\xb4?Zi\xdf\x83\x9e\\q9\xf5\xd0J\x01\xc3\xcd\xcfk\xc5\xf0\xd8\x94\x80*!X\xff\x01\x00\x00\x00\x82|\xd3L9(\xf2\xbd\xa2\xb9]\xc6\xa7\xdfG\xd4\xca\xb8\x10\x16@>\xe9v\xb7\x8bfS\xf9\xfa\x11\x7f\x01\x00\x00\x00f\x0f\xcb\xb2\x1f\xb6\x9b\xc3\xf9_&\xe7=\x16\xd3]d\xf55\xe0\x0b\x0e\x0f\xd8\xfa\x8c9\x86\xb7\xb1]\x83\x01\x00\x00\x00\xb7\x01\x89\x81"\x84\n\xd2o\xdb\x0cGI\x02{\xe1\x03uo\xbb\xc2\xa6\xd4zQ\x87\x9a\x1f\x0b\x82\xc1E\x01\x00\x00\x00\x81\x81\xd5\x0f#\xe9N\\\xf837}\xdf\x11\xc0F\r\xa2f\x86{\x05\xbc?U\xec\xe3\xcdA\xcf!\xb4\x01\x00\x00\x00S\x06\t\xd9\xfb\x13\x19\x86^\x01\xb1\xa2\x84 \xff\xa3\xc0\xf9\xc7+\x9e)lG\x07~\x1f\x1e\xb4a\xb5\xbb\x01\x00\x00\x00G\xf1Ct\x86\xd3qR\xb4\xde\xb7\xe6A69\x07\xe7eX\xd5\xe8\x1d\xfe\x9b\xae\xee^1\x9a\\K\xe0'
block = b"\xf9\xbe\xb4\xd9block\x00\x00\x00\x00\x00\x00\x00h\x01\x00\x00\x85\x9b\xa0\xae\x04\x80&1\xec\xb2Y\xeb\x95\xb6\x11\xcaS08\xa9\xdb\xdcEM\x96|\xde\x8a\xf7`\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x84\xeaJ\xcd\x15\x97\x90\x9b\x89\xb0\x91\xe2\x1b6-2\x03\xd1\xbch2\x1b\x977\xfd\x0c\xdd1Z@Iom\xd6Ib\x97\xd8\t\x17 \x04\x8a\xb1\x01\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xffd\x03\x99$\x0b,\xfa\xbemm\x96\x0f\xac)\xba\xea\xfeY\xdds\x87\x95\xef\xe5\xe3\xed'\xf8\x8a\xf87\x00Yb2\xd2j8\xa3p\x8aQ\x10\x00\x00\x00\xf0\x9f\x90\x9f\t/F2Pool/k\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\n\x00\x00\x00\x00\x00\x00\x00\x03@\xbe@%\x00\x00\x00\x00\x19v\xa9\x14\xc8%\xa1\xec\xf2\xa6\x83\x0cD\x01b\x0c:\x16\xf1\x99PW\xc2\xab\x88\xac\x00\x00\x00\x00\x00\x00\x00\x00&j$Hath#qv\r\x7f\x9e\t/\xa3\xd6\x91\xbc\xbd\nv\x0f\xdcM\xa5\xbb/\x80\x0b\x0e\xe3g \t\xb0\xfbV\xca\x00\x00\x00\x00\x00\x00\x00\x00&j$\xb9\xe1\x1bmg\x1b\xd8\xa4\x129\x8c\xf8\xf3\xffb\xc5\xaay\x9c\x9a\x98\xe6o#~\xd7\x05+Ad\x9e\x05M2\x15Xd\x14\x93>"
ping = b'\xf9\xbe\xb4\xd9ping\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x02\x80\x89\xfe'


def double_sha256(data):
    m = hashlib.sha256(data)
    m = hashlib.sha256(m.digest())
    return m.digest()


# Decodes the magic no., command, length, checksum, and payload
def decode(message):
    magic = struct.unpack('<I', message[0:4])[0]
    # print("Magic No.:", magic)
    command = message[4:16].decode('utf-8').replace("\0", "")
    # print("Command:", command)
    length = struct.unpack('<I', message[16:20])[0]
    # print("Length:", length)
    checksum = struct.unpack('<I', message[20:24])[0]
    # print("Checksum:", checksum)
    payload = message[24:]
    # print("Payload:", payload)
    decode_arr = [magic, command, length, checksum, payload]
    return(decode_arr)


# Function used to handle variable integers in Python
# This was quite hard to find documentation on and thankfull this stackexchange answer gave just enough information to
# be able to create the function:
# https://bitcoin.stackexchange.com/questions/40451/how-does-the-variable-length-integer-work
def var_int(message):
    inv_array = decode(message)
    payload = inv_array[4]
    byte_1 = payload[0]
    payload_length = len(payload)
    if byte_1 < 253:
        count = byte_1
        start_byte = 1
    elif byte_1 == 253:
        count = struct.unpack('<H', message[1:3])[0]
        start_byte = 3
    elif byte_1 == 254:
        count = struct.unpack('<I', message[1:5])[0]
        start_byte = 5
    # Else, byte_1 == 255
    else:
        count = struct.unpack('<Q', message[1:9])[0]
        start_byte = 9
    return start_byte, count, payload_length, payload

# This function takes the inv message as the input and returns a dictionary containing the inv vectors in the form
# {'count': 34, 'Vector_X' : {'type': 1, 'hash': XXXX'}, 'Vector_Y' : {'type': 1, 'hash': YYYY'}}
def parse_inv(message):
    start_byte, count, payload_length, payload = (var_int(message))
    vect_dict = dict()
    vect_dict['count'] = count

    for i in range(0,count):
        vect_dict_mini = dict()
        byte_position = start_byte + i*36
        if struct.unpack('<I', payload[byte_position:byte_position+4])[0] == 1 or struct.unpack('<I', payload[byte_position:byte_position+4])[0] == 2:
            vect_dict_mini['type'] = struct.unpack('<I', payload[byte_position:byte_position+4])[0]
            vect_dict_mini['hash'] = payload[byte_position+4:byte_position+36]
            vect_names = "Vector_" + str(i)
            vect_dict[vect_names] = vect_dict_mini

    # Only return the dictionary if the vectors are not blank
    if len(vect_dict) > 1:
        return vect_dict
    else:
        return "Inv vectors empty!"

# The function for parsing the version messages. This was not fully completed due to time constraints
def parse_ver(message):
    ver_array = decode(message)
    payload = ver_array[4]
    payload_length = len(payload)
    payload_dict = dict()

    payload_dict['version'] = struct.unpack('<i', payload[0:4])[0]
    payload_dict['services'] = struct.unpack('<Q', payload[4:12])[0]
    payload_dict['timestamp'] = struct.unpack('<Q', payload[12:20])[0]

    addr_recv = dict()
    net_addr = payload[20:46]
    addr_recv['services'] = struct.unpack('<Q', net_addr[0:8])[0]
    addr_recv['ipv6_4'] = struct.unpack('<16p', net_addr[8:24])[0]
    addr_recv['port'] = struct.unpack('<H', net_addr[24:26])[0]
    payload_dict['add_recv'] = addr_recv

    addr_from = dict()
    net_addr = payload[46:72]
    addr_from['services'] = struct.unpack('<Q', net_addr[0:8])[0]
    addr_from['ipv6_4'] = struct.unpack('<16p', net_addr[8:24])[0]
    addr_from['port'] = struct.unpack('<H', net_addr[24:26])[0]
    payload_dict['addr_from'] = addr_recv

    payload_dict['nonce'] = struct.unpack('<Q', payload[72:80])[0]

    user_agent = dict()
    byte_1 = payload[80]

    # if byte_1 < 253:
    #     count = byte_1
    #     start_byte = 1
    # elif byte_1 == 253:
    #     count = struct.unpack('<H', message[1:3])[0]
    #     start_byte = 2[]
    # elif byte_1 == 254:
    #     count = struct.unpack('<I', message[1:5])[0]
    #     start_byte = 4
    # elif byte_1 == 255:
    #     count = struct.unpack('<Q', message[1:9])[0]
    #     start_byte = 8

    return(payload_dict)

# The function for parsing the transactions. This was not fully completed due to time constraints
def parse_tx(message):
    ver_array = decode(message)
    payload = ver_array[4]
    payload_dict = dict()

    payload_dict['version'] = struct.unpack('<i', payload[0:4])[0]
    flag = struct.unpack('<H', payload[4:6])[0]
    if flag == 1:
        skip = 2
        payload_dict['flag'] = flag
    else:
        skip = 0

    tx_in_count_1 = payload[4+skip: 4+skip+2]
    print(tx_in_count_1)

    # tx_in_count = struct.unpack('<I', payload[4+skip: 4+skip+1])[0]
    # print("TX_In_Count:",tx_in_count)
    # payload_dict['tx_in_count'] = payload[4+skip:]

    start_byte, count, payload_length, payload = (var_int(message))
    print("Start: ", start_byte)
    print("Count: ", count)
    print("Payload: ", payload)
    print("Payload Length: ", payload_length)

    # Return the dictionary that contains the payload information
    return payload_dict

# Some networking info that is needing to create the version messages
hostname = socket.gethostname()
my_ip = socket.gethostbyname(hostname)
my_port = 8080
peer_ip_address = '103.129.13.34'
peer_tcp_port = 8333

# Create the "version" request payload: https://en.bitcoin.it/wiki/Protocol_documentation#version
# https://bitcoin.stackexchange.com/questions/50444/unable-to-send-version-message-correctly
def create_version_payload():
    version = struct.pack('<i', 70015)
    services = struct.pack('<Q', 0)
    time_now = int(time.time())
    timestamp = struct.pack('<q', time_now)
    addr_recv = services
    addr_ip = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff' + socket.inet_aton(my_ip)
    addr_port = struct.pack('<H', my_port)
    add_from = b'\x00'*26
    nonce = struct.pack('<H', random.randint(0, 9))
    user_agent = b'\x00'
    start_height = b'\x00' * 4
    # relay = struct.pack('<?', 1)

    # Creates the version payload by concatenating the components
    payload = version + services + timestamp + addr_recv + addr_ip + addr_port + add_from + nonce + user_agent + start_height
    return payload


# https://en.bitcoin.it/wiki/Protocol_documentation#Message_structure
# Creates the version message
def create_version_message():
    magic = b'\xf9\xbe\xb4\xd9'
    command = "version".encode('utf-8') + b'\x00' * 5
    payload = create_version_payload()
    checksum = double_sha256(payload)[0:4]
    length = struct.pack('<I', len(payload))

    # Creates the version message by concatenating the components
    message = magic + command + length + checksum + payload
    return message

# https://en.bitcoin.it/wiki/Protocol_documentation#verack
# Create the "verack" request message
def create_verack():
    magic = b'\xf9\xbe\xb4\xd9'
    command = "verack".encode('utf-8') + b'\x00' * 6
    checksum = double_sha256(b'')[0:4]
    payload = b''
    length = struct.pack('<I', len(payload))

    # Creates the verack message by concatenating the components
    message = magic + command + length + checksum + payload
    return message

# This is the primary function that was used to connect and send messages to the node.
def connect_message():
    print("Transaction Viewer Starting")
    print("-" * 40)
    buffer_size = 1024

    # Establish TCP Connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((peer_ip_address, peer_tcp_port))

    # The below are all node IPs that I tested but was unable to get the correct version response.
    # s.connect(('51.89.115.248', 8333))
    # s.connect(('159.65.84.214', 8333))
    # s.connect(('73.53.89.223', 8333))
    # s.connect(('103.129.13.34', 8333))

    # This var was supposed to generate the version message, however it was causing problems that I could not figure out
    # so the below hardcoded message was used instead.
    # msg = create_version_message()

    # The below message was created by Joey Corcoran and used in his program. I included it as a hardcoded value to to
    # test whether my setup was correct and I was still unable to get the expected version response most of the time.
    # I have no idea what is wrong with this as I have been troubleshooting for approximately 6 hours. The responses
    # seem to work intermittently, with no clear pattern.
    msg = b"\xf9\xbe\xb4\xd9version\x00\x00\x00\x00\x00d\x00\x00\x00\x9bJ0\xec\x80\x11\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00W'xb\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xffI5Y\xdf \x8d\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\x7f\x00\x00\x01 \x8d\x01\xb3'\xb9ln\xd3\xa6\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    print("Version Send: ", msg)
    s.send(msg)

    # The response should look like the sent version message, with a verack appended to the end of it.
    response_data = s.recv(1024)

    if response_data != 0:
        print("-" * 40)
        print("Successfully connected to Bitcoin Network")
        print("Version Response:", response_data)
        print("-" * 40)

    # Send and print a verack message
    s.send(create_verack())
    print("Verack Send: ", create_verack())

    # Receive the verack response and print it
    verack_response = s.recv(1024)
    print("Verack Response:", verack_response)

    inv_count = 1
    # The below code is how the final function should look in order to continuously run and continuously print
    # the (decoded) transactions and blocks to the terminal
    while True:
        response_data = b''
        while len(response_data) < 24:
            # time.sleep(.10)
            response_data += s.recv(1)
        # print("Response Data:", response_data)
        decode_response = decode(response_data)
        # decode_response = response_data

        # print(decode_response)
        payload_length = decode_response[2]
        # print(payload_length)
        response_data = b''

        while len(response_data) < payload_length:
            response_data += s.recv(1)
        # Depending on what the message type is, it would be decoded using the specific parsing function similar to the
        # parsing function that was written for the inv messages above. This was not completed as so much time was
        # wasted trying to get the correct response to the version message.
        if decode_response[1] == "inv":
            # The Inv payloads are the only ones that were successfully received, TX and blocks were not as you need to
            # parse/decode the invs and then create a get data message in order to request them.
            print("Inv", inv_count)
            inv_count += 1
        elif decode_response[1] == "tx":
            print("TX")
        elif decode_response[1] == "block":
            print("Block")
        else:
            continue

# Below are print statements that were
# ------------------------------------------------------------------
# print(parse_inv(inv))
# print(parse_tx(transaction))
# print(parse_ver(initial_version_command))
# print(create_version_payload())
# print(create_version_message())

# Warning this may need to be re-run many times in order to run it without an error. I could not establish why this was
# the case, it seemed to be a problem on the bitcoin network side rather than on my code side. Other students also had
# the same problem
connect_message()
