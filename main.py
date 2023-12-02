

def entrar(self):
    
        obtener_pickle(self, 'abrir')
        
        seguir = True
        
        
        
        while seguir==True: 
        
            match pregunta:
                
                case 1:
                    '''Registro de cliente'''
                    nombre,usuario,dni,contacto,fecha_nac,mail,contrasena = infoPersonas (self.clientes,self.empleados)
                    cliente=Cliente(nombre,usuario,dni,contacto,fecha_nac,mail,contrasena,'nivel 1',[])
                    self.clientes[usuario]=cliente
                    print('Su usuario se ha creado con exito. Si desea seguir en el programa ingrese sesión. ')
                    pregunta=menuPPL()
                
                case 2:
                    '''Inicio de sesion'''
                    entrar=input('Tiene usted un usuario creado? Ingrese si en caso de tenerlo, y no en lo contrario: ')
                    imprimir='Error. Ingrese "si" si ya tiene un usuario creado y "no" de lo contrario: '
                    entrar=valSiNo(entrar,imprimir)
                    if entrar:
                        usuario, contrasena = valSignIn (self.clientes, self.empleados)
                        cliente,empleado,tipo = valTipoUsuario(usuario,self.clientes,self.empleados)
                    
                        '''Menu del cliente'''
                        if cliente:
                            pregcliente=input('Elija una de las siguientes opciones: \n 1. Hacer una reserva \n 2. Hacer un pedido en el buffet \n 3. Modificar una reserva \n 4. Cancelar una reserva \n 5. Realizar check-in \n 6. Realizar check-out \n 7. Cerrar Sesión \n')
                            imprimir='Error. Elija una de las siguientes opciones: \n 1. Hacer una reserva \n 2. Hacer un pedido en el buffet \n 3. Modificar una reserva \n 4. Cancelar una reserva \n 5. Realizar check-in \n 6. Realizar check-out \n 7. Cerrar Sesión \n'
                            pregcliente=val_opc(pregcliente,1,7,imprimir)
                            cliente:Cliente = self.clientes.get(usuario)
                            while pregcliente != 7:
                                match pregcliente:

                                    case 1:
                                        '''Hacer una reserva'''
                                        self.cobros = cliente.realizar_reserva(self.habitaciones, self.reservas, self.cobros)
                                        
                                    case 2:
                                        '''Pedir algo de buffet'''
                                        imprimir = 'Usted no tiene una reserva asi que no puede hacer un pedido en el buffet'
                                        if usuarioEnReservas(cliente,self.reservas,imprimir):
                                            self.cobros=cliente.realizarPedidoBuffet (self.pedidosBuffet,self.buffet,self.cobros,self.reservas)
                                        
                                    case 3:
                                        '''Modificar una reserva'''
                                        imprimir = 'Usted no tiene una reserva'
                                        if usuarioEnReservas(cliente,self.reservas,imprimir):
                                            self.cobros = cliente.modificar_reserva(self.reservas, self.habitaciones, self.cobros)
                                        
                                    case 4:
                                        '''Cancelar una reserva'''
                                        if cliente.cancelar_reserva(self.reservas, self.habitaciones) == None:
                                            pass
                      
                                    case 5:
                                        '''Check-in'''
                                        cliente.check_in()
                                       
                                    case 6:
                                        '''Check-out'''
                                        cliente.check_out()
                                        
                                pregcliente=input('Elija una de las siguientes opciones: \n 1. Hacer una reserva \n 2. Hacer un pedido en el buffet \n 3. Modificar una reserva \n 4. Cancelar una reserva \n 5. Realizar check-in \n 6. Realizar check-out \n 7. Cerrar Sesión \n')
                                imprimir='Error. Elija una de las siguientes opciones: \n 1. Hacer una reserva \n 2. Hacer un pedido en el buffet \n 3. Modificar una reserva \n 4. Cancelar una reserva \n 5. Realizar check-in \n 6. Realizar check-out \n 7. Cerrar Sesión \n'
                                pregcliente=val_opc(pregcliente,1,7,imprimir)
                            
                            if pregcliente == 7:
                                pregunta=menuPPL() 
                            
                        
                    else:
                        pregunta=menuPPL()                
                            
                case 3:
                    seguir = False
                    break
                                   
        obtener_pickle(self, 'cerrar')
        print('Se ha cerrado la sesión con éxito.')
        
if __name__ == "__main__":
    hotel=Hotel('POO')
    hotel.entrar()