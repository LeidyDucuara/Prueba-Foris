from unittest import TestCase
from asistencia_foris.impl import Impl_serv_presence as prese
from asistencia_foris.impl import Impl_serv_asistence as asis
from asistencia_foris.impl import Imp_serv_student as estu

class Test_impl_serv(TestCase):
    
    def setUp(self):
        # Este código se ejecutará antes de cada test, y nos ayuda a preparar
        # nuestro un escenario genérico sobre el que ejecutar nuestro testing.
        self.serv_presence = prese.Impl_service_presence()
        self.serv_asis = asis.Impl_service_asistence()
        self.serv_estu = estu.Impl_service_student()
        
    def test_register_estudent_ok(self):
        a = len(self.serv_estu.all_students())
        self.serv_estu.register_student('Juan',self.serv_asis)
        b = len(self.serv_estu.all_students())
        self.assertEqual(b, a+1)
    
    def test_register_not_estudent_repet(self):
        a = len(self.serv_estu.all_students())
        self.serv_estu.register_student('Pedro',self.serv_asis)
        self.serv_estu.register_student('Pedro',self.serv_asis)
        b = len(self.serv_estu.all_students())
        self.assertEqual(a,b)
        
    def test_is_estudent(self):
        self.serv_estu.register_student('Pedro',self.serv_asis)
        self.assertEqual(self.serv_estu.is_student("Pedro"),True)

    def test_cant_min(self):
        self.assertEqual(self.serv_presence.cant_min('12:01', '15:03'), 182)
        
    def test_register_presence_ok(self):
        a = len(self.serv_presence.all_presences())
        self.serv_presence.register_presence('Pedro','1','08:17',"12:00",'F201',self.serv_asis)
        b = len(self.serv_presence.all_presences())
        self.assertNotEqual(b, a)
        
    def test_not_day_register_presence(self):
        a = len(self.serv_presence.all_presences())
        self.serv_presence.register_presence('Pedro','12','08:17',"12:00",'F201',self.serv_asis)
        b = len(self.serv_presence.all_presences())
        self.assertEqual(b, a)
        
    def test_not_min_register_presence(self):
        a = len(self.serv_presence.all_presences())
        self.serv_presence.register_presence('Pedro','2','12:17',"12:19",'F201',self.serv_asis)
        b = len(self.serv_presence.all_presences())
        self.assertEqual(b, a)

    
