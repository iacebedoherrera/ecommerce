/** @jsxImportSource @emotion/react */


import { Fragment, useCallback, useContext } from "react"
import { Fragment_fd0e7cb8f9fb4669a6805377d925fba0 } from "/utils/stateful_components"
import { Box, Button, Center, Divider, Heading, HStack, Image as ChakraImage, Input, Menu, MenuButton, MenuItem, MenuList, Modal, ModalBody, ModalContent, ModalFooter, ModalHeader, ModalOverlay, Text, VStack } from "@chakra-ui/react"
import Script from "next/script"
import "focus-visible/dist/focus-visible"
import { EventLoopContext, StateContexts } from "/utils/context"
import { Event, getRefValue, getRefValues, set_val } from "/utils/state"
import NextHead from "next/head"



export function Menuitem_e63102572022b9a8c0192d984059847d () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_0bead96693dc81bc0fb57c006951df53 = useCallback((_e) => addEvents([Event("state.log_in_state.change_log_in", {})], (_e), {}), [addEvents, Event])

  return (
    <MenuItem onClick={on_click_0bead96693dc81bc0fb57c006951df53}>
  {`Iniciar sesión`}
</MenuItem>
  )
}

export function Box_8998530a5e5bca50c6043b05a973f2b6 () {
  const [addEvents, connectError] = useContext(EventLoopContext);
  
    const handleSubmit_db279fd4df0f81d9d9ff04b44a817203 = useCallback((ev) => {
        const $form = ev.target
        ev.preventDefault()
        const form_data = {...Object.fromEntries(new FormData($form).entries()), ...{}}

        addEvents([Event("state.register_state.handle_submit", {form_data:form_data})])

        if (true) {
            $form.reset()
        }
    })
    


  return (
    <Box as={`form`} onSubmit={handleSubmit_db279fd4df0f81d9d9ff04b44a817203}>
  <VStack>
  <Input name={`name`} placeholder={`Nombre`} type={`text`}/>
  <Input name={`surname`} placeholder={`Apellidos`} type={`text`}/>
  <Input name={`phone_number`} placeholder={`Teléfono`} type={`text`}/>
  <Input name={`email`} placeholder={`Email`} type={`text`}/>
  <Input name={`password`} placeholder={`Contraseña`} type={`text`}/>
  <Button_01c07cf3d3b884bc35b47a3ce975eb4f/>
</VStack>
</Box>
  )
}

export function Button_40de86e881a9d76c7c54f7b6b8ebd0af () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_0bead96693dc81bc0fb57c006951df53 = useCallback((_e) => addEvents([Event("state.log_in_state.change_log_in", {})], (_e), {}), [addEvents, Event])

  return (
    <Button onClick={on_click_0bead96693dc81bc0fb57c006951df53}>
  {`Cerrar`}
</Button>
  )
}

export function Modal_9400cdef736075a6e120b572d42c998a () {
  const state__log_in_state = useContext(StateContexts.state__log_in_state)


  return (
    <Modal isOpen={state__log_in_state.show_log_in}>
  <ModalOverlay>
  <ModalContent>
  <ModalHeader>
  {`Iniciar Sesión`}
</ModalHeader>
  <ModalBody>
  <Box_91457938746a32cc2ea80bbc12efd3cc/>
</ModalBody>
  <ModalFooter>
  <Button_40de86e881a9d76c7c54f7b6b8ebd0af/>
</ModalFooter>
</ModalContent>
</ModalOverlay>
</Modal>
  )
}

export function Button_4d3634a1bbd5b232eb6ebfc511ac156d () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_0bead96693dc81bc0fb57c006951df53 = useCallback((_e) => addEvents([Event("state.log_in_state.change_log_in", {})], (_e), {}), [addEvents, Event])

  return (
    <Button onClick={on_click_0bead96693dc81bc0fb57c006951df53} type={`submit`}>
  {`Iniciar sesión`}
</Button>
  )
}

export function Box_91457938746a32cc2ea80bbc12efd3cc () {
  
    const handleSubmit_605028908bac76490053e5e504d7661b = useCallback((ev) => {
        const $form = ev.target
        ev.preventDefault()
        const form_data = {...Object.fromEntries(new FormData($form).entries()), ...{}}

        addEvents([Event("state.log_in_state.handle_submit", {form_data:form_data})])

        if (true) {
            $form.reset()
        }
    })
    
  const [addEvents, connectError] = useContext(EventLoopContext);


  return (
    <Box as={`form`} onSubmit={handleSubmit_605028908bac76490053e5e504d7661b}>
  <VStack>
  <Input name={`username`} placeholder={`Email`} type={`text`}/>
  <Input name={`password`} placeholder={`Contraseña`} type={`text`}/>
  <Button_4d3634a1bbd5b232eb6ebfc511ac156d/>
</VStack>
</Box>
  )
}

export function Modal_058a829b043b003332cf0fa175f332a5 () {
  const state__register_state = useContext(StateContexts.state__register_state)


  return (
    <Modal isOpen={state__register_state.show}>
  <ModalOverlay>
  <ModalContent>
  <ModalHeader>
  {`Registrarme`}
</ModalHeader>
  <ModalBody>
  <Box_8998530a5e5bca50c6043b05a973f2b6/>
</ModalBody>
  <ModalFooter>
  <Button_5d3c1d53dfdc1afc554ca05896dca768/>
</ModalFooter>
</ModalContent>
</ModalOverlay>
</Modal>
  )
}

export function Menuitem_82da1683df404494f6b17f4015729c35 () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_8bf74d25796e74cea279979675a7748f = useCallback((_e) => addEvents([Event("state.register_state.change", {})], (_e), {}), [addEvents, Event])

  return (
    <MenuItem onClick={on_click_8bf74d25796e74cea279979675a7748f}>
  {`Registrarme`}
</MenuItem>
  )
}

export function Button_5d3c1d53dfdc1afc554ca05896dca768 () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_8bf74d25796e74cea279979675a7748f = useCallback((_e) => addEvents([Event("state.register_state.change", {})], (_e), {}), [addEvents, Event])

  return (
    <Button onClick={on_click_8bf74d25796e74cea279979675a7748f}>
  {`Cerrar`}
</Button>
  )
}

export function Button_01c07cf3d3b884bc35b47a3ce975eb4f () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_8bf74d25796e74cea279979675a7748f = useCallback((_e) => addEvents([Event("state.register_state.change", {})], (_e), {}), [addEvents, Event])

  return (
    <Button onClick={on_click_8bf74d25796e74cea279979675a7748f} type={`submit`}>
  {`Registrarme`}
</Button>
  )
}

export default function Component() {

  return (
    <Fragment>
  <Fragment_fd0e7cb8f9fb4669a6805377d925fba0/>
  <VStack>
  <Script strategy={`afterInteractive`}>
  {`document.documentElement.lang='es'`}
</Script>
  <VStack sx={{"width": "100%"}}>
  <Center>
  <HStack sx={{"width": "100%", "paddingTop": "1.5em", "paddingBottom": "0.8em"}}>
  <VStack sx={{"position": "fixed", "left": "4em"}}>
  <Text>
  {`Icono`}
</Text>
</VStack>
  <VStack sx={{"paddingX": "0.5em"}}>
  <Heading>
  {`I&N Shop`}
</Heading>
</VStack>
  <HStack sx={{"position": "absolute", "right": "4em"}}>
  <VStack sx={{"paddingRight": "0.8em"}}>
  <Menu>
  <MenuButton>
  <ChakraImage src={`/icons/spainIcon.png`} sx={{"width": "1.5em", "height": "1.5em"}}/>
</MenuButton>
</Menu>
</VStack>
  <VStack sx={{"paddingX": "0.8em"}}>
  <Menu>
  <MenuButton>
  <ChakraImage src={`/icons/userIcon.png`} sx={{"width": "1.5em", "height": "1.5em"}}/>
</MenuButton>
  <MenuList>
  <Menuitem_e63102572022b9a8c0192d984059847d/>
  <Modal_9400cdef736075a6e120b572d42c998a/>
  <Menuitem_82da1683df404494f6b17f4015729c35/>
  <Modal_058a829b043b003332cf0fa175f332a5/>
  <MenuItem>
  {`Mi cuenta`}
</MenuItem>
</MenuList>
</Menu>
</VStack>
  <VStack sx={{"paddingX": "0.8em"}}>
  <Button variant={`unstyled`}>
  <ChakraImage src={`/icons/shoppingIcon.png`} sx={{"width": "1.5em", "height": "1.5em"}}/>
</Button>
</VStack>
</HStack>
</HStack>
</Center>
  <Divider sx={{"borderColor": "black", "width": "100%"}}/>
  <HStack>
  <VStack sx={{"paddingX": "2em"}}>
  <Menu>
  <MenuButton>
  {`Camisetas`}
</MenuButton>
  <MenuList>
  <MenuItem>
  {`Manga corta`}
</MenuItem>
  <MenuItem>
  {`Manga larga`}
</MenuItem>
</MenuList>
</Menu>
</VStack>
  <Center sx={{"height": "2em"}}>
  <Divider orientation={`vertical`} sx={{"borderColor": "black"}}/>
</Center>
  <VStack sx={{"paddingX": "2em"}}>
  <Menu>
  <MenuButton>
  {`Pantalones`}
</MenuButton>
  <MenuList>
  <MenuItem>
  {`Jogger`}
</MenuItem>
  <MenuItem>
  {`Skinny`}
</MenuItem>
</MenuList>
</Menu>
</VStack>
</HStack>
</VStack>
  <Divider sx={{"borderColor": "black"}}/>
  <HStack sx={{"paddingTop": "2em", "paddingBottom": "20em"}}>
  <VStack>
  <Button variant={`unstyled`}>
  <ChakraImage src={`/icons/men.avif`} sx={{"height": "20em"}}/>
</Button>
</VStack>
  <VStack>
  <Button variant={`unstyled`}>
  <ChakraImage src={`/icons/women.avif`} sx={{"height": "20em"}}/>
</Button>
</VStack>
</HStack>
  <VStack sx={{"bg": "#0C151D", "width": "100%", "color": "#FFFFFF"}}>
  <HStack>
  <Button variant={`unstyled`}>
  {`Envíos`}
</Button>
  <Button variant={`unstyled`}>
  {`Devoluciones`}
</Button>
  <Button variant={`unstyled`}>
  {`Contacto`}
</Button>
</HStack>
  <HStack>
  <Text>
  {`Icono`}
</Text>
</HStack>
  <HStack>
  <Text>
  {`© 2023-2024 I&N Shop`}
</Text>
</HStack>
</VStack>
</VStack>
  <NextHead>
  <title>
  {`I&N Shop`}
</title>
  <meta content={`A Reflex app.`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
