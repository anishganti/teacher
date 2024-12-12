import { Tabs, rem } from '@mantine/core';
import { IconPhoto, IconMessageCircle, IconSettings } from '@tabler/icons-react';
import { Assistant } from './Assistant';

export function Aside() {  
  const iconStyle = { width: rem(12), height: rem(12) };
  
  return (
    <Tabs color="gray" variant="pills" defaultValue="metadata">
        <Tabs.List>
            <Tabs.Tab value="metadata" leftSection={<IconPhoto style={iconStyle} />}>
            Metadata
            </Tabs.Tab>
            <Tabs.Tab value="notes" leftSection={<IconMessageCircle style={iconStyle} />}>
            Notes
            </Tabs.Tab>
            <Tabs.Tab value="assistant" leftSection={<IconSettings style={iconStyle} />}>
            Assistant
            </Tabs.Tab>
        </Tabs.List>

        <Tabs.Panel value="metadata">
            Metadata tab content
        </Tabs.Panel>

        <Tabs.Panel value="notes">
            Notes tab content
        </Tabs.Panel>

        <Tabs.Panel value="assistant">
            <Assistant />
        </Tabs.Panel>
    </Tabs>    
  );
}