/** @jsxImportSource @emotion/react */


import { Fragment, useCallback, useContext } from "react"
import { EventLoopContext, StateContexts } from "/utils/context"
import { Event, getBackendURL, getRefValue, getRefValues, isTrue } from "/utils/state"
import { WifiOffIcon as LucideWifiOffIcon } from "lucide-react"
import { keyframes } from "@emotion/react"
import { Button as RadixThemesButton, Dialog as RadixThemesDialog, DropdownMenu as RadixThemesDropdownMenu, Flex as RadixThemesFlex, Heading as RadixThemesHeading, Link as RadixThemesLink, Separator as RadixThemesSeparator, Text as RadixThemesText, TextField as RadixThemesTextField, Theme as RadixThemesTheme } from "@radix-ui/themes"
import env from "/env.json"
import Script from "next/script"
import NextLink from "next/link"
import { Button, Image as ChakraImage, Text } from "@chakra-ui/react"
import { Root as RadixFormRoot } from "@radix-ui/react-form"
import "@radix-ui/themes/styles.css"
import theme from "/utils/theme.js"
import NextHead from "next/head"



export function Flex_17c4e5da16aa95542ff0d1cae9798fc6 () {
  const state__product_state = useContext(StateContexts.state__product_state)



  return (
    <RadixThemesFlex align={`start`} direction={`column`} gap={`2`}>
  {state__product_state.products.map((product, index_2491102c2805a2521c9c8e42b5efc93b) => (
  <RadixThemesFlex align={`start`} direction={`column`} key={index_2491102c2805a2521c9c8e42b5efc93b} gap={`2`}>
  <img>
  {product.product_path}
</img>
  <RadixThemesText as={`p`}>
  {product.product_name}
</RadixThemesText>
  <RadixThemesText as={`p`}>
  {product.product.price}
</RadixThemesText>
</RadixThemesFlex>
))}
</RadixThemesFlex>
  )
}

export function Root_865924382b3edfb69ea65db9df388303 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  
    const handleSubmit_4b9f9e0658d970e30a73ce739234a8c5 = useCallback((ev) => {
        const $form = ev.target
        ev.preventDefault()
        const form_data = {...Object.fromEntries(new FormData($form).entries()), ...{}}

        addEvents([Event("state.login_state.log_in", {form_data:form_data})])

        if (true) {
            $form.reset()
        }
    })
    

  return (
    <RadixFormRoot className={`Root`} onSubmit={handleSubmit_4b9f9e0658d970e30a73ce739234a8c5}>
  <RadixThemesFlex direction={`column`} gap={`6`}>
  <RadixThemesFlex direction={`column`} gap={`3`}>
  <RadixThemesTextField.Input name={`username`} placeholder={`Email`} required={true}/>
  <RadixThemesTextField.Input name={`password`} placeholder={`Contraseña`} required={true} type={`password`}/>
</RadixThemesFlex>
  <RadixThemesFlex direction={`column`}>
  <Button_958def1c016ad93565dfe5aaf53b4ca4/>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixFormRoot>
  )
}

export function Root_7e91dfe5debb77266b0acdf93703fa87 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  
    const handleSubmit_b3899a14f019ff03465610ab68fcbdd0 = useCallback((ev) => {
        const $form = ev.target
        ev.preventDefault()
        const form_data = {...Object.fromEntries(new FormData($form).entries()), ...{}}

        addEvents([Event("state.register_state.handle_submit", {form_data:form_data})])

        if (true) {
            $form.reset()
        }
    })
    

  return (
    <RadixFormRoot className={`Root`} onSubmit={handleSubmit_b3899a14f019ff03465610ab68fcbdd0}>
  <RadixThemesFlex direction={`column`} gap={`6`}>
  <RadixThemesFlex direction={`column`} gap={`3`}>
  <RadixThemesTextField.Input name={`name`} placeholder={`Nombre`}/>
  <RadixThemesTextField.Input name={`surname`} placeholder={`Apellidos`}/>
  <RadixThemesTextField.Input name={`phone_number`} placeholder={`Teléfono`}/>
  <RadixThemesTextField.Input name={`email`} placeholder={`Email`}/>
  <RadixThemesTextField.Input name={`password`} placeholder={`Contraseña`} type={`password`}/>
  <RadixThemesTextField.Input name={`address`} placeholder={`Calle`}/>
  <RadixThemesFlex direction={`row`} gap={`3`}>
  <RadixThemesTextField.Input name={`city`} placeholder={`Ciudad`}/>
  <RadixThemesTextField.Input name={`autonomous_community`} placeholder={`Comunidad`}/>
  <RadixThemesTextField.Input name={`postal_code`} placeholder={`Código postal`}/>
</RadixThemesFlex>
</RadixThemesFlex>
  <RadixThemesFlex direction={`column`}>
  <Button_40c66e80e7ef24c7332b77f505b33d18/>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixFormRoot>
  )
}

export function Text_e91c5026ee6607eb6f967e944db0ce96 () {
  const state__login_state = useContext(StateContexts.state__login_state)



  return (
    <RadixThemesText as={`p`}>
  {state__login_state.username}
</RadixThemesText>
  )
}

export function Dialog__root_0b786497bff051ae727ec079353fa490 () {
  const state__register_state = useContext(StateContexts.state__register_state)



  return (
    <RadixThemesDialog.Root open={state__register_state.show}>
  <RadixThemesDialog.Content>
  <RadixThemesFlex css={{"display": "flex", "alignItems": "center", "justifyContent": "center"}}>
  <RadixThemesDialog.Title>
  {`Registrarme`}
</RadixThemesDialog.Title>
</RadixThemesFlex>
  <Root_7e91dfe5debb77266b0acdf93703fa87/>
  <RadixThemesFlex direction={`row`}>
  <RadixThemesDialog.Close>
  <RadixThemesFlex direction={`column`}>
  <Button_a39036dfd7161d8d87a38f1e2572819b/>
</RadixThemesFlex>
</RadixThemesDialog.Close>
</RadixThemesFlex>
</RadixThemesDialog.Content>
</RadixThemesDialog.Root>
  )
}

export function Button_da09327585c1cfe25b64191e111e62c3 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  const on_click_f441e1257efca9a58137da1e4e0d1153 = useCallback((_e) => addEvents([Event("_redirect", {path:`/products/tshirt`,external:false})], (_e), {}), [addEvents, Event])


  return (
    <RadixThemesButton css={{"width": "100%", "height": "100%", "padding": "0.5em", "borderRadius": "0.5em", "color": "#000000", "backgroundColor": "#83d3f4", "whiteSpace": "normal", "textAlign": "start", "&:hover": {"backgroundColor": "#087ec4"}}} onClick={on_click_f441e1257efca9a58137da1e4e0d1153}>
  {`Camisetas`}
</RadixThemesButton>
  )
}

export function Button_40c66e80e7ef24c7332b77f505b33d18 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  const on_click_8bf74d25796e74cea279979675a7748f = useCallback((_e) => addEvents([Event("state.register_state.change", {})], (_e), {}), [addEvents, Event])


  return (
    <RadixThemesButton onClick={on_click_8bf74d25796e74cea279979675a7748f} type={`submit`}>
  {`Registrarme`}
</RadixThemesButton>
  )
}

export function Button_b2319b29b70cf2fbce8f046689d10edb () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  const on_click_c462cd8fcac7274b3118fa248911efdf = useCallback((_e) => addEvents([Event("state.login_state.change", {})], (_e), {}), [addEvents, Event])


  return (
    <RadixThemesButton color={`red`} onClick={on_click_c462cd8fcac7274b3118fa248911efdf}>
  {`Cancelar`}
</RadixThemesButton>
  )
}

export function Button_958def1c016ad93565dfe5aaf53b4ca4 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  const on_click_c462cd8fcac7274b3118fa248911efdf = useCallback((_e) => addEvents([Event("state.login_state.change", {})], (_e), {}), [addEvents, Event])


  return (
    <RadixThemesButton onClick={on_click_c462cd8fcac7274b3118fa248911efdf} type={`submit`}>
  {`Iniciar sesión`}
</RadixThemesButton>
  )
}

const pulse = keyframes`
    0% {
        opacity: 0;
    }
    100% {
        opacity: 1;
    }
`


export function Fragment_9b41d37e4761d9a127d83abb1f29a533 () {
  const state__login_state = useContext(StateContexts.state__login_state)
  const [addEvents, connectErrors] = useContext(EventLoopContext);



  return (
    <Fragment>
  {isTrue(((state__login_state.login_cookie) === (""))) ? (
  <Fragment>
  <RadixThemesDropdownMenu.Content>
  <RadixThemesDropdownMenu.Item onClick={(_e) => addEvents([Event("state.login_state.change", {})], (_e), {})}>
  {`Iniciar sesión`}
</RadixThemesDropdownMenu.Item>
  <RadixThemesDropdownMenu.Item onClick={(_e) => addEvents([Event("state.register_state.change", {})], (_e), {})}>
  {`Registrarme`}
</RadixThemesDropdownMenu.Item>
</RadixThemesDropdownMenu.Content>
</Fragment>
) : (
  <Fragment>
  <RadixThemesDropdownMenu.Content>
  <RadixThemesDropdownMenu.Item onClick={(_e) => addEvents([Event("_redirect", {path:`/my_account`,external:false})], (_e), {})}>
  {`Mi cuenta`}
</RadixThemesDropdownMenu.Item>
  <RadixThemesDropdownMenu.Item onClick={(_e) => addEvents([Event("state.login_state.log_out", {})], (_e), {})}>
  {`Cerrar sesión`}
</RadixThemesDropdownMenu.Item>
</RadixThemesDropdownMenu.Content>
</Fragment>
)}
</Fragment>
  )
}

export function Fragment_6499b51736be44284c15de43340cb16c () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);



  return (
    <Fragment>
  {isTrue(connectErrors.length >= 2) ? (
  <Fragment>
  <RadixThemesDialog.Root css={{"zIndex": 9999}} open={connectErrors.length >= 2}>
  <RadixThemesDialog.Content>
  <RadixThemesDialog.Title>
  {`Connection Error`}
</RadixThemesDialog.Title>
  <RadixThemesText as={`p`}>
  {`Cannot connect to server: `}
  {(connectErrors.length > 0) ? connectErrors[connectErrors.length - 1].message : ''}
  {`. Check if server is reachable at `}
  {getBackendURL(env.EVENT).href}
</RadixThemesText>
</RadixThemesDialog.Content>
</RadixThemesDialog.Root>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  )
}

export function Button_a39036dfd7161d8d87a38f1e2572819b () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  const on_click_8bf74d25796e74cea279979675a7748f = useCallback((_e) => addEvents([Event("state.register_state.change", {})], (_e), {}), [addEvents, Event])


  return (
    <RadixThemesButton color={`red`} onClick={on_click_8bf74d25796e74cea279979675a7748f}>
  {`Cancelar`}
</RadixThemesButton>
  )
}

export function Dialog__root_c4d1f87e53e7a3fc389b0ca80a3d656e () {
  const state__login_state = useContext(StateContexts.state__login_state)



  return (
    <RadixThemesDialog.Root open={state__login_state.show}>
  <RadixThemesDialog.Content>
  <RadixThemesFlex css={{"display": "flex", "alignItems": "center", "justifyContent": "center"}}>
  <RadixThemesDialog.Title>
  {`Iniciar sesión`}
</RadixThemesDialog.Title>
</RadixThemesFlex>
  <Root_865924382b3edfb69ea65db9df388303/>
  <RadixThemesFlex direction={`column`}>
  <RadixThemesDialog.Close>
  <RadixThemesFlex direction={`column`}>
  <Button_b2319b29b70cf2fbce8f046689d10edb/>
</RadixThemesFlex>
</RadixThemesDialog.Close>
</RadixThemesFlex>
</RadixThemesDialog.Content>
</RadixThemesDialog.Root>
  )
}

export function Fragment_cb5edf864ed730e6ef1545318d0da5a2 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);



  return (
    <Fragment>
  {isTrue(connectErrors.length > 0) ? (
  <Fragment>
  <LucideWifiOffIcon css={{"color": "crimson", "zIndex": 9999, "position": "fixed", "bottom": "30px", "right": "30px", "animation": `${pulse} 1s infinite`}} size={32}/>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  )
}

export default function Component() {

  return (
    <Fragment>
  <Fragment>
  <div css={{"position": "fixed", "width": "100vw", "height": "0"}}>
  <Fragment_cb5edf864ed730e6ef1545318d0da5a2/>
</div>
  <Fragment_6499b51736be44284c15de43340cb16c/>
</Fragment>
  <RadixThemesFlex align={`start`} direction={`column`} gap={`2`}>
  <Script strategy={`afterInteractive`}>
  {`document.documentElement.lang='es'`}
</Script>
  <RadixThemesFlex align={`start`} css={{"width": "100%"}} direction={`column`} gap={`2`}>
  <RadixThemesFlex align={`start`} css={{"width": "100%", "paddingTop": "1.5em", "paddingBottom": "0.8em"}} direction={`row`} justify={`center`} gap={`2`}>
  <RadixThemesFlex align={`start`} css={{"position": "absolute", "left": "4em"}} direction={`column`} gap={`2`}>
  <RadixThemesText as={`p`}>
  {`Icono`}
</RadixThemesText>
</RadixThemesFlex>
  <RadixThemesFlex align={`start`} direction={`column`} gap={`2`}>
  <RadixThemesLink asChild={true} css={{"paddingInlineStart": "0.5em", "paddingInlineEnd": "0.5em"}}>
  <NextLink href={`/`} passHref={true}>
  <RadixThemesHeading>
  {`I&N Shop`}
</RadixThemesHeading>
</NextLink>
</RadixThemesLink>
</RadixThemesFlex>
  <RadixThemesFlex align={`start`} css={{"position": "absolute", "right": "4em"}} direction={`row`} gap={`2`}>
  <RadixThemesFlex align={`start`} css={{"paddingRight": "0.8em"}} direction={`column`} gap={`2`}>
  <RadixThemesDropdownMenu.Root>
  <RadixThemesDropdownMenu.Trigger>
  <ChakraImage src={`/icons/spainIcon.png`} sx={{"width": "1.5em", "height": "1.5em"}}/>
</RadixThemesDropdownMenu.Trigger>
</RadixThemesDropdownMenu.Root>
</RadixThemesFlex>
  <RadixThemesFlex align={`start`} direction={`column`} gap={`2`}>
  <Text_e91c5026ee6607eb6f967e944db0ce96/>
</RadixThemesFlex>
  <RadixThemesFlex align={`start`} css={{"paddingInlineStart": "0.8em", "paddingInlineEnd": "0.8em"}} direction={`column`} gap={`2`}>
  <RadixThemesDropdownMenu.Root>
  <RadixThemesDropdownMenu.Trigger>
  <img css={{"width": "1.5em", "height": "1.5em"}} src={`/icons/userIcon.png`}/>
</RadixThemesDropdownMenu.Trigger>
  <Fragment_9b41d37e4761d9a127d83abb1f29a533/>
</RadixThemesDropdownMenu.Root>
  <Dialog__root_c4d1f87e53e7a3fc389b0ca80a3d656e/>
  <Dialog__root_0b786497bff051ae727ec079353fa490/>
</RadixThemesFlex>
  <RadixThemesFlex align={`start`} css={{"paddingInlineStart": "0.8em", "paddingInlineEnd": "0.8em"}} direction={`column`} gap={`2`}>
  <RadixThemesLink css={{"variant": "ghost"}}>
  <img css={{"width": "1.5em", "height": "1.5em"}} src={`/icons/shoppingIcon.png`}/>
</RadixThemesLink>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesFlex>
  <RadixThemesSeparator css={{"borderColor": "black", "width": "100%", "colorScheme": "mint"}} size={`4`}/>
  <RadixThemesFlex align={`start`} css={{"width": "100%"}} direction={`row`} justify={`center`} gap={`2`}>
  <RadixThemesFlex align={`start`} css={{"paddingInlineStart": "2em", "paddingInlineEnd": "2em"}} direction={`column`} gap={`2`}>
  <Button_da09327585c1cfe25b64191e111e62c3/>
</RadixThemesFlex>
  <RadixThemesFlex css={{"height": "2em", "display": "flex", "alignItems": "center", "justifyContent": "center"}}>
  <RadixThemesSeparator css={{"borderColor": "black", "colorScheme": "mint"}} orientation={`vertical`} size={`4`}/>
</RadixThemesFlex>
  <RadixThemesFlex align={`start`} css={{"paddingInlineStart": "2em", "paddingInlineEnd": "2em"}} direction={`column`} gap={`2`}>
  <RadixThemesButton css={{"width": "100%", "height": "100%", "padding": "0.5em", "borderRadius": "0.5em", "color": "#000000", "backgroundColor": "#83d3f4", "whiteSpace": "normal", "textAlign": "start", "&:hover": {"backgroundColor": "#087ec4"}}}>
  {`Pantalones`}
</RadixThemesButton>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesFlex>
  <RadixThemesSeparator css={{"borderColor": "black", "colorScheme": "mint"}} size={`4`}/>
  <Flex_17c4e5da16aa95542ff0d1cae9798fc6/>
  <RadixThemesFlex align={`center`} css={{"background": "#0C151D", "width": "100%", "color": "#FFFFFF"}} direction={`column`} gap={`2`}>
  <RadixThemesFlex align={`start`} direction={`row`} gap={`9`}>
  <Button variant={`unstyled`}>
  {`Envíos`}
</Button>
  <Button variant={`unstyled`}>
  {`Devoluciones`}
</Button>
  <Button variant={`unstyled`}>
  {`Contacto`}
</Button>
</RadixThemesFlex>
  <RadixThemesFlex align={`start`} direction={`row`} gap={`2`}>
  <Text>
  {`Icono`}
</Text>
</RadixThemesFlex>
  <RadixThemesFlex align={`start`} direction={`row`} gap={`2`}>
  <Text>
  {`© 2023-2024 I&N Shop`}
</Text>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesFlex>
  <NextHead>
  <title>
  {`Ecommerce | Products/[Product Type]`}
</title>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
