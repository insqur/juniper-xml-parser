# Converts a raw Juniper CLI XML output to an Etree Object
Python Modul, which provides a trivial routine for converting router output to etree object, without namespaces

Juniper CLI Input Example
-------------------------

    sl@M320-TEST-re0> show version | display xml | no-more
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
    sl@M320-TEST-re0>

Usage
-----
    from juniperXmlParser import parse
    tree = parse(cliXmlString)
    print (tree.xpath ('//rpc-reply/software-information/junos-version')[0].text)
    
    output: 
    13.3R5.9


