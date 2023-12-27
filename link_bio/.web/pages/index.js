
/** @jsxImportSource @emotion/react */import { Fragment } from "react"
import { Fragment_fd0e7cb8f9fb4669a6805377d925fba0 } from "/utils/stateful_components"
import { Avatar, Button, HStack, Image as ChakraImage, Link, Text, VStack } from "@chakra-ui/react"
import "focus-visible/dist/focus-visible"
import NextLink from "next/link"
import NextHead from "next/head"



export default function Component() {

  return (
    <Fragment>
  <Fragment_fd0e7cb8f9fb4669a6805377d925fba0/>
  <VStack>
  <HStack sx={{"position": "sticky", "bg": "black", "paddingX": "16px", "paddingY": "8px", "zIndex": "999"}}>
  <Text sx={{"height": "40px"}}>
  {`vikusS3dev`}
</Text>
</HStack>
  <VStack>
  <Avatar name={`vikusS3 dev`} size={`xl`}/>
  <Text>
  {`@vikusS3dev`}
</Text>
  <Text>
  {`Hola ✌ MI NOMBRE ES VIKUS`}
</Text>
  <Text>
  {`Soy tecnico en sistemas y programador con mas de un año de experiencia.
                Actualmente trabajo como freelance full-stack developer python, php y ASP.NET.
                Ademos de ser un apasionado por la tecnologia, me gusta mucho la musica y los videojuegos.`}
</Text>
</VStack>
  <VStack>
  <Link as={NextLink} href={`https://www.twitch.tv/vikussss3`} isExternal={true}>
  <Button>
  {`Twitch`}
</Button>
</Link>
  <Link as={NextLink} href={`https://www.youtube.com/channel/UCWTqiQVIA08vVTJhwy1SaDQ`} isExternal={true}>
  <Button>
  {`Youtube`}
</Button>
</Link>
  <Link as={NextLink} href={`https://www.linkedin.com/in/felix-saul-orellana-contreras-971b042a6/`} isExternal={true}>
  <Button>
  {`Linkedin`}
</Button>
</Link>
  <Link as={NextLink} href={`https://twitter.com/Vikus3S`} isExternal={true}>
  <Button>
  {`Twitter`}
</Button>
</Link>
</VStack>
  <VStack>
  <ChakraImage src={`favicon.ico`}/>
  <Link as={NextLink} href={`https://www.linkedin.com/in/felix-saul-orellana-contreras-971b042a6/`} isExternal={true}>
  {`© 2021-2023 VikusS3dev V1 By Felix Orellana`}
</Link>
  <Text>
  {`Building with Reflex and Python`}
</Text>
</VStack>
</VStack>
  <NextHead>
  <title>
  {`Reflex App`}
</title>
  <meta content={`A Reflex app.`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
