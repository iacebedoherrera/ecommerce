/** @jsxImportSource @emotion/react */


import { Fragment } from "react"
import { Fragment_fd0e7cb8f9fb4669a6805377d925fba0 } from "/utils/stateful_components"
import { Heading, HStack, Menu, MenuButton, MenuItem, MenuList, VStack } from "@chakra-ui/react"
import "focus-visible/dist/focus-visible"
import NextHead from "next/head"



export default function Component() {

  return (
    <Fragment>
  <Fragment_fd0e7cb8f9fb4669a6805377d925fba0/>
  <VStack>
  <HStack>
  <Heading>
  {`I&N Shop`}
</Heading>
</HStack>
  <HStack>
  <VStack sx={{"paddingX": "2em"}}>
  <Menu>
  <MenuButton>
  {`Camisetas`}
  <MenuList>
  <MenuItem>
  {`Manga corta`}
</MenuItem>
  <MenuItem>
  {`Manga larga`}
</MenuItem>
</MenuList>
</MenuButton>
</Menu>
</VStack>
  <VStack>
  <Menu>
  <MenuButton>
  {`Camisetas`}
  <MenuList>
  <MenuItem>
  {`Manga corta`}
</MenuItem>
  <MenuItem>
  {`Manga larga`}
</MenuItem>
</MenuList>
</MenuButton>
</Menu>
</VStack>
</HStack>
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
