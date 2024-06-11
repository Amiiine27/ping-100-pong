import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ModifierTournoiComponent } from './modifier-tournoi.component';

describe('ModifierTournoiComponent', () => {
  let component: ModifierTournoiComponent;
  let fixture: ComponentFixture<ModifierTournoiComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ModifierTournoiComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ModifierTournoiComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
