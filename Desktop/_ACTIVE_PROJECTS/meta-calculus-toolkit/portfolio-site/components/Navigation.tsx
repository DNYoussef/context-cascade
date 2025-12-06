'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { useState, useRef, useEffect } from 'react';

interface NavItem {
  href: string;
  label: string;
  children?: { href: string; label: string }[];
}

const navItems: NavItem[] = [
  { href: '/', label: 'Home' },
  {
    href: '/story',
    label: 'Story',
    children: [
      { href: '/story', label: 'Overview' },
      { href: '/story/hunch', label: 'The Hunch' },
      { href: '/story/audits', label: 'AI & Audits' },
      { href: '/story/quantum', label: 'Quantum Tests' },
      { href: '/story/geometry', label: 'Multi-Geometry' },
    ]
  },
  { href: '/results', label: 'Results' },
  {
    href: '/learn',
    label: 'Learn',
    children: [
      { href: '/learn', label: 'Overview' },
      { href: '/learn/textbook', label: 'Textbook' },
      { href: '/learn/proofs', label: 'Proofs' },
      { href: '/learn/lessons', label: 'Lessons Learned' },
    ]
  },
  {
    href: '/tools',
    label: 'Tools',
    children: [
      { href: '/tools', label: 'Overview' },
      { href: '/tools/simulator', label: 'Simulator' },
      { href: '/tools/code', label: 'Source Code' },
    ]
  },
];

export default function Navigation() {
  const pathname = usePathname();
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [openDropdown, setOpenDropdown] = useState<string | null>(null);
  const [mobileOpenDropdown, setMobileOpenDropdown] = useState<string | null>(null);
  const navRef = useRef<HTMLDivElement>(null);

  // Close dropdown when clicking outside
  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (navRef.current && !navRef.current.contains(event.target as Node)) {
        setOpenDropdown(null);
      }
    }
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  // Check if current path is in a sub-section
  const isInSection = (item: NavItem) => {
    if (item.children) {
      return pathname.startsWith(item.href);
    }
    return pathname === item.href;
  };

  const handleDropdownToggle = (href: string) => {
    setOpenDropdown(openDropdown === href ? null : href);
  };

  const handleDropdownEnter = (href: string) => {
    setOpenDropdown(href);
  };

  const handleDropdownLeave = () => {
    setOpenDropdown(null);
  };

  const handleMobileDropdownToggle = (href: string) => {
    setMobileOpenDropdown(mobileOpenDropdown === href ? null : href);
  };

  return (
    <nav
      className="sticky top-0 z-50 border-b border-dark-border bg-dark-surface/80 backdrop-blur-md"
      role="navigation"
      aria-label="Main navigation"
    >
      <div className="section py-4">
        <div className="flex items-center justify-between">
          {/* Logo */}
          <Link href="/" className="flex items-center space-x-2 group">
            <div className="text-2xl font-bold">
              <span className="gradient-text">Meta-Calculus</span>
            </div>
          </Link>

          {/* Desktop Navigation */}
          <div className="hidden md:flex items-center space-x-1" role="menubar" ref={navRef}>
            {navItems.map((item) => {
              const isActive = isInSection(item);
              const isOpen = openDropdown === item.href;

              // Handle dropdown items
              if (item.children) {
                return (
                  <div key={item.href} className="relative">
                    <button
                      onClick={() => handleDropdownToggle(item.href)}
                      onMouseEnter={() => handleDropdownEnter(item.href)}
                      role="menuitem"
                      aria-expanded={isOpen}
                      aria-haspopup="true"
                      className={`
                        px-4 py-2 rounded-lg text-sm font-medium transition-colors inline-flex items-center gap-1
                        focus:outline-none focus:ring-2 focus:ring-primary-400 focus:ring-offset-2 focus:ring-offset-dark-surface
                        ${
                          isActive
                            ? 'bg-primary-600 text-white'
                            : 'text-gray-300 hover:text-white hover:bg-dark-border'
                        }
                      `}
                    >
                      {item.label}
                      <svg
                        className={`w-4 h-4 transition-transform ${isOpen ? 'rotate-180' : ''}`}
                        fill="none"
                        stroke="currentColor"
                        viewBox="0 0 24 24"
                      >
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
                      </svg>
                    </button>

                    {/* Dropdown menu */}
                    <div
                      className={`
                        absolute top-full left-0 mt-1 w-48 py-2 bg-dark-surface border border-dark-border rounded-lg shadow-xl
                        transition-all duration-200 origin-top-left
                        ${isOpen ? 'opacity-100 scale-100' : 'opacity-0 scale-95 pointer-events-none'}
                      `}
                      onMouseLeave={handleDropdownLeave}
                      role="menu"
                    >
                      {item.children.map((child) => {
                        const isChildActive = pathname === child.href;
                        return (
                          <Link
                            key={child.href}
                            href={child.href}
                            role="menuitem"
                            onClick={() => setOpenDropdown(null)}
                            className={`
                              block px-4 py-2 text-sm transition-colors
                              ${
                                isChildActive
                                  ? 'bg-primary-600/20 text-primary-400'
                                  : 'text-gray-300 hover:text-white hover:bg-dark-border/50'
                              }
                            `}
                          >
                            {child.label}
                          </Link>
                        );
                      })}
                    </div>
                  </div>
                );
              }

              // Regular nav items
              return (
                <Link
                  key={item.href}
                  href={item.href}
                  role="menuitem"
                  aria-current={isActive ? 'page' : undefined}
                  className={`
                    px-4 py-2 rounded-lg text-sm font-medium transition-colors
                    focus:outline-none focus:ring-2 focus:ring-primary-400 focus:ring-offset-2 focus:ring-offset-dark-surface
                    ${
                      isActive
                        ? 'bg-primary-600 text-white'
                        : 'text-gray-300 hover:text-white hover:bg-dark-border'
                    }
                  `}
                >
                  {item.label}
                </Link>
              );
            })}
          </div>

          {/* Mobile Menu Button */}
          <button
            className="md:hidden p-2 rounded-lg hover:bg-dark-border text-gray-300 focus:outline-none focus:ring-2 focus:ring-primary-400"
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            aria-label={mobileMenuOpen ? 'Close menu' : 'Open menu'}
            aria-expanded={mobileMenuOpen}
            aria-controls="mobile-menu"
          >
            <svg
              className="w-6 h-6"
              fill="none"
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              viewBox="0 0 24 24"
              stroke="currentColor"
              aria-hidden="true"
            >
              {mobileMenuOpen ? (
                <path d="M6 18L18 6M6 6l12 12" />
              ) : (
                <path d="M4 6h16M4 12h16M4 18h16" />
              )}
            </svg>
          </button>
        </div>

        {/* Mobile Navigation */}
        <div
          id="mobile-menu"
          className={`${mobileMenuOpen ? '' : 'hidden'} md:hidden mt-4 pb-2`}
          role="menu"
          aria-label="Mobile navigation"
        >
          <div className="flex flex-col space-y-2">
            {navItems.map((item) => {
              const isActive = isInSection(item);
              const isMobileOpen = mobileOpenDropdown === item.href;

              // Handle items with children (expandable section)
              if (item.children) {
                return (
                  <div key={item.href}>
                    <button
                      onClick={() => handleMobileDropdownToggle(item.href)}
                      className={`
                        w-full px-4 py-2 rounded-lg text-sm font-medium transition-colors
                        flex items-center justify-between
                        focus:outline-none focus:ring-2 focus:ring-primary-400
                        ${
                          isActive
                            ? 'bg-primary-600 text-white'
                            : 'text-gray-300 hover:text-white hover:bg-dark-border'
                        }
                      `}
                    >
                      {item.label}
                      <svg
                        className={`w-4 h-4 transition-transform ${isMobileOpen ? 'rotate-180' : ''}`}
                        fill="none"
                        stroke="currentColor"
                        viewBox="0 0 24 24"
                      >
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
                      </svg>
                    </button>

                    {/* Expandable sub-menu */}
                    <div
                      className={`
                        overflow-hidden transition-all duration-200
                        ${isMobileOpen ? 'max-h-96 opacity-100' : 'max-h-0 opacity-0'}
                      `}
                    >
                      <div className="pl-4 mt-2 space-y-1 border-l-2 border-dark-border ml-4">
                        {item.children.map((child) => {
                          const isChildActive = pathname === child.href;
                          return (
                            <Link
                              key={child.href}
                              href={child.href}
                              role="menuitem"
                              className={`
                                block px-4 py-2 rounded-lg text-sm transition-colors
                                ${
                                  isChildActive
                                    ? 'bg-primary-600/20 text-primary-400'
                                    : 'text-gray-400 hover:text-white hover:bg-dark-border/50'
                                }
                              `}
                              onClick={() => setMobileMenuOpen(false)}
                            >
                              {child.label}
                            </Link>
                          );
                        })}
                      </div>
                    </div>
                  </div>
                );
              }

              // Regular items
              return (
                <Link
                  key={item.href}
                  href={item.href}
                  role="menuitem"
                  aria-current={isActive ? 'page' : undefined}
                  className={`
                    px-4 py-2 rounded-lg text-sm font-medium transition-colors
                    focus:outline-none focus:ring-2 focus:ring-primary-400
                    ${
                      isActive
                        ? 'bg-primary-600 text-white'
                        : 'text-gray-300 hover:text-white hover:bg-dark-border'
                    }
                  `}
                  onClick={() => setMobileMenuOpen(false)}
                >
                  {item.label}
                </Link>
              );
            })}
          </div>
        </div>
      </div>
    </nav>
  );
}
