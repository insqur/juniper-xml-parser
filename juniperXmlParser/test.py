from juniperXmlParser import parse
if __name__ == "__main__":
    cliXmlString = """sliebert@M320-TEST-re0> show version | display xml | no-more
<rpc-reply xmlns:junos="http://xml.juniper.net/junos/13.3R5/junos">
    <software-information>
        <host-name>M320-TEST-re0</host-name>
        <product-model>m320</product-model>
        <product-name>m320</product-name>
        <junos-version>13.3R5.9</junos-version>
    </software-information>
    <cli>
        <banner>{master}</banner>
    </cli>
</rpc-reply>
 
{master}
sliebert@M320-TEST-re0>"""
    tree = parse(cliXmlString)
    print (tree.xpath ('//rpc-reply/software-information/junos-version')[0].text)