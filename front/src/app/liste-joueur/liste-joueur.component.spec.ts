import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListeJoueurComponent } from './liste-joueur.component';

describe('ListeJoueurComponent', () => {
  let component: ListeJoueurComponent;
  let fixture: ComponentFixture<ListeJoueurComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ListeJoueurComponent]
    });
    fixture = TestBed.createComponent(ListeJoueurComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
